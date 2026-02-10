import json


def load_users(file_path="users.json"):
    """
    Lädt Benutzerinformationen aus einer JSON-Datei mit UTF-8 Kodierung.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # UTF-8 für Kompatibilität
            return json.load(file)
    except FileNotFoundError:
        print("Datei nicht gefunden!")
        return []


def filter_by_age(users, target_age):
    """
    Sucht Benutzer mit einem exakten Alter.
    """
    # Geändert von >= auf == für exakte Treffer
    return [u for u in users if u.get("age") == target_age]


def filter_users_by_name(users, name):
    """Filtert Benutzer nach Namen (Groß-/Kleinschreibung ignoriert)."""
    return [u for u in users if u["name"].lower() == name.lower()]


def filter_by_email(users, search_email):
    """Sucht Benutzer basierend auf der E-Mail-Adresse."""
    return [u for u in users if search_email.lower() in u.get("email", "").lower()]


if __name__ == "__main__":
    users_data = load_users()  # Modularer Aufruf

    option = input("Filter wählen (name, age, email): ").strip().lower()

    results = []
    if option == "age":
        try:
            age_input = int(input("Exaktes Alter eingeben: "))
            results = filter_by_age(users_data, age_input)
        except ValueError:
            print("Bitte eine Zahl eingeben.")
    elif option == "name":
        name_input = input("Name: ")
        results = filter_users_by_name(users_data, name_input)
    elif option == "email":
        email_input = input("E-Mail: ")
        results = filter_by_email(users_data, email_input)

    print(f"\n{len(results)} Treffer gefunden:")
    for user in results:
        print(user)