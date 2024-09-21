import json
import os
import getpass

PROFILES_FILE = 'profiles.json'

def load_profiles():
    if os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, 'r') as file:
            return json.load(file)
        
    return []
def save_profiles(profiles):
    with open(PROFILES_FILE, 'w') as file:
        json.dump(profiles, file, indent=4)

def create_profile(profiles):
    name = input("Enter your name: ")
    password = getpass.getpass("Enter your password: ")
    profiles.append({"name": name, "password":password})
    save_profiles(profiles)
    return name

def select_profile(profiles):
    print("Profiles:")
    for idx, profile in enumerate(profiles, start=1):
        print(f"{idx}. {profile['name']}")
    print(f"{len(profiles) + 1}. Create a new profile")

    choice = int(input("Select a profile: "))
    if choice == len(profiles) + 1:
        return create_profile(profiles)
    elif 1 <= choice <= len(profiles):
        selected_profile = profiles[choice - 1]
        password = getpass.getpass("Enter your password: ")
        if password == selected_profile['password']:
            return selected_profile['name']
        else:
            print("Incorrect password. Please try again.")
            return select_profile(profiles)
    else:
        print("Invalid choice. Please try again.")
        return select_profile(profiles)
def application_start_up():
    profiles = load_profiles()
    if not profiles:
        print("No profiles found. Let us create one.")
        user = create_profile(profiles)
    else:
        print("Who is using the program?")
        user = select_profile(profiles)

    print(f"Welcome, {user}!")
if __name__ == "__main__":
    application_start_up()
