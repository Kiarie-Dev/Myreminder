import json
import os
import getpass

PROFILES_FILE = 'profiles.json'


# A function to load profiles from a file
def load_profiles():
    if os.path.exists(PROFILES_FILE):
        try:
            with open(PROFILES_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading profiles file. Starting with an empty profile list!")
            return []   
    return []

def save_profiles(profiles):
    try:
        with open(PROFILES_FILE, 'w') as file:
            json.dump(profiles, file, indent=4)
    except IOError:
        print("Error saving profiles!")

def create_profile(profiles):
    while True:
        name = input("Enter your name: ")
        if any(profile['name'] == name for profile in profiles):
            print("Profile name already exists. Please choose a different name")
        else:
            break
    while True:
        password = getpass.getpass("Enter your password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        if password == confirm_password:
            break 
        else:
            print("Passwords do not match. Please try again.")

    profiles.append({"name": name, "password":password})
    save_profiles(profiles)
    return name

def select_profile(profiles):
    print("Profiles:")
    for idx, profile in enumerate(profiles, start=1):
        print(f"{idx}. {profile['name']}")
    print(f"{len(profiles) + 1}. Create a new profile")
    while True:
        try:
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
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
