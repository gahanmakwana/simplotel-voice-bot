import os
import streamlit as st
from openai import OpenAI
from src import database
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        pass
# Initialize Client with Groq URL
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

def check_availability(check_in, check_out, room_type):
    # Helper to convert arguments to string for DB if needed, or just pass through
    return str(database.query_availability(check_in, check_out, room_type))

def create_booking(guest_name, room_id, check_in, check_out):
    return database.insert_booking(guest_name, room_id, check_in, check_out)

def get_hotel_policy(topic):
    return database.query_faq(topic)

def chat_with_llm(messages):
    # Define tools (Function calling)
    tools = [
        {
            "type": "function",
            "function": {
                "name": "check_availability",
                "description": "Check if rooms are available",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "check_in": {"type": "string", "description": "YYYY-MM-DD"},
                        "check_out": {"type": "string", "description": "YYYY-MM-DD"},
                        "room_type": {"type": "string", "enum": ["Deluxe", "Suite", "Standard"]}
                    },
                    "required": ["check_in", "check_out", "room_type"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "create_booking",
                "description": "Book a room for a guest",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "guest_name": {"type": "string"},
                        "room_id": {"type": "integer"},
                        "check_in": {"type": "string"},
                        "check_out": {"type": "string"}
                    },
                    "required": ["guest_name", "room_id", "check_in", "check_out"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_hotel_policy",
                "description": "Get answers to FAQs like breakfast or pool",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string"}
                    },
                    "required": ["topic"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", # Free, fast model
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=1024
    )
    
    response_message = response.choices[0].message
    
    # Handle Function Calls
    if response_message.tool_calls:
        messages.append(response_message) # extend conversation with assistant's reply
        
        available_functions = {
            "check_availability": check_availability,
            "create_booking": create_booking,
            "get_hotel_policy": get_hotel_policy,
        }
        
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            import json
            function_args = json.loads(tool_call.function.arguments)
            
            if function_name == "check_availability":
                function_response = function_to_call(
                    check_in=function_args.get("check_in"),
                    check_out=function_args.get("check_out"),
                    room_type=function_args.get("room_type"),
                )
            elif function_name == "create_booking":
                 function_response = function_to_call(
                    guest_name=function_args.get("guest_name"),
                    room_id=function_args.get("room_id"),
                    check_in=function_args.get("check_in"),
                    check_out=function_args.get("check_out"),
                )
            elif function_name == "get_hotel_policy":
                function_response = function_to_call(
                    topic=function_args.get("topic")
                )
                
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": str(function_response),
                }
            )
        
        # Get second response from LLM after function result
        second_response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        return second_response.choices[0].message

    return response_message