"""Alphabetize names by last name then first name."""

from typing import List, Dict


def alphabetize_names(names: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return a new list of names sorted by last name, then first name."""
    return sorted(names, key=lambda name: (name["lastname"].lower(), name["firstname"].lower()))


def main() -> None:
    names = [
        {"lastname": "Smith", "firstname": "John"},
        {"lastname": "Doe", "firstname": "Jane"},
        {"lastname": "Brown", "firstname": "Charlie"},
        {"lastname": "Johnson", "firstname": "Emily"},
        {"lastname": "Williams", "firstname": "Ava"},
        {"lastname": "Jones", "firstname": "Liam"},
        {"lastname": "Garcia", "firstname": "Mia"},
        {"lastname": "Miller", "firstname": "Noah"},
        {"lastname": "Davis", "firstname": "Olivia"},
        {"lastname": "Rodriguez", "firstname": "Isabella"},
        {"lastname": "Martinez", "firstname": "Sophia"},
        {"lastname": "Hernandez", "firstname": "Logan"},
        {"lastname": "Lopez", "firstname": "Lucas"},
        {"lastname": "Gonzalez", "firstname": "Mason"},
        {"lastname": "Wilson", "firstname": "Ethan"},
        {"lastname": "Anderson", "firstname": "Harper"},
        {"lastname": "Thomas", "firstname": "Evelyn"},
        {"lastname": "Taylor", "firstname": "Abigail"},
        {"lastname": "Moore", "firstname": "Elijah"},
        {"lastname": "Jackson", "firstname": "Oliver"},
    ]

    for name in alphabetize_names(names):
        print(f"{name['lastname']},{name['firstname']}")


if __name__ == "__main__":
    main()
