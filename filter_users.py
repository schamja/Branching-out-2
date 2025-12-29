import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(min_age):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        # Logik: Nimm den User, wenn sein Alter >= min_age ist
        filtered = [u for u in users if u.get("age", 0) >= min_age]

        return filtered
    except FileNotFoundError:
        print("Datei nicht gefunden!")
        return []


def filter_by_email(search_email):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        # Logik: Nimm den User, wenn die gesuchte E-Mail in seiner Adresse vorkommt
        filtered = [u for u in users if search_email.lower() in u.get("email", "").lower()]

        return filtered
    except FileNotFoundError:
        return "Datei nicht gefunden."


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")