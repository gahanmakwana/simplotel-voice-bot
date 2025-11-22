import sqlite3
import os


if not os.path.exists("data"):
    os.makedirs("data")

conn = sqlite3.connect("data/hotel.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS faqs;

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    room_number INTEGER,
    room_type TEXT,
    base_price REAL,
    description TEXT,
    capacity INTEGER
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_name TEXT,
    room_id INTEGER,
    check_in_date DATE,
    check_out_date DATE,
    status TEXT,
    total_amount REAL
);

CREATE TABLE faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    question TEXT,
    answer TEXT
);
""")

rooms = [
    (1, 101, "Deluxe", 120.0, "Ocean view with balcony", 2),
    (2, 102, "Suite", 200.0, "Luxury suite with spa", 4),
    (3, 103, "Standard", 80.0, "Cozy room with Wi-Fi", 2),
]
cur.executemany("INSERT INTO rooms VALUES (?, ?, ?, ?, ?, ?)", rooms)

faqs = [
    ("Breakfast", "What time is breakfast?", "Breakfast is served from 7-10 AM."),
    ("Pool", "Is the pool heated?", "Yes, the pool is temperature controlled."),
]
cur.executemany("INSERT INTO faqs (category, question, answer) VALUES (?, ?, ?)", faqs)

conn.commit()
conn.close()
print("Database seeded successfully!")
