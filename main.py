from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today().date()
    current_weekday = today.weekday()
    birthdays = defaultdict(list)

    # Look for birthdays in the next 7 days including today
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        birthday_this_year = birthday.replace(year=today.year).date()

        # Calculate the number of days until the next birthday
        delta_days = (birthday_this_year - today).days
        if delta_days < 0:
            birthday_next_year = birthday.replace(year=today.year + 1).date()
            delta_days = (birthday_next_year - today).days

        # Check if the birthday is within the next week
        if 0 <= delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            if day_of_week >= 5:
                day_of_week = 0

            birthdays[day_of_week].append(name)

    # Sort the days of the week and return results
    for i in range(5):
        if birthdays[i]:
            day_name = (today + timedelta(days=(i - current_weekday) % 7)).strftime(
                "%A"
            )
            names = ", ".join(birthdays[i])

            print(f"{day_name}: {names}")
        else:
            print("No birthdays")


users_example = [
    {
        "name": "Bill Gates",
        "birthday": datetime(1955, 11, 26),
    },
    {
        "name": "Jill Valentine",
        "birthday": datetime(1955, 11, 26),
    },
    {
        "name": "Chris Redfield",
        "birthday": datetime(1955, 11, 28),
    },
    {
        "name": "Albert Wesker",
        "birthday": datetime(1955, 11, 29),
    },
    {
        "name": "Ada Wong",
        "birthday": datetime(1955, 11, 30),
    },
    {
        "name": "Leon Scott Kennedy",
        "birthday": datetime(1955, 12, 1),
    },
    {
        "name": "Claire Redfield",
        "birthday": datetime(1955, 12, 2),
    },
    {
        "name": "John Smith",
        "birthday": datetime(1955, 12, 4),
    },
]

get_birthdays_per_week(users_example)
