import datetime

def parse_date(text):
    try:
        return datetime.datetime.strptime(text, "%Y-%m-%d").date()
    except:
        return None
