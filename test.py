from datetime import datetime, timedelta, date

def string_to_date(date_string):
    # format_data = "%Y.%m.%d"
    # f_date = datetime.strptime(date_string, format_data)
    # date = f_date.date()
    # return date
    return datetime.strptime(date_string, "%Y.%m.%d").date()


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days = days_ahead)
    
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        user["birthday"] = user["birthday"].replace(year=today.year)
    
    