import sqlite3

DB_PATH = "data/hotel.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def query_availability(check_in, check_out, room_type):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT room_id, room_number FROM rooms
        WHERE room_type=? AND room_id NOT IN (
            SELECT room_id FROM bookings
            WHERE (check_in_date <= ? AND check_out_date >= ?)
        )
    """, (room_type, check_out, check_in))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_booking(guest_name, room_id, check_in, check_out):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bookings (guest_name, room_id, check_in_date, check_out_date, status)
        VALUES (?, ?, ?, ?, 'Confirmed')
    """, (guest_name, room_id, check_in, check_out))
    conn.commit()
    conn.close()
    return "Booking confirmed!"

def query_faq(topic):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT answer FROM faqs WHERE category=?", (topic,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "No policy found."
