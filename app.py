import json
import os
import getpass
from typing import List, Dict

PROFILES_FILE = 'profiles.json'

# For clear code, we will initialize variables for constant messages
PROFILE_EXISTS_MSG = "Profile name already exists. Please choose a different name."
PASSWORD_MISMATCH_MSG = "Passwords do not match. Please try again."
ERROR_READING_FILE_MSG = "Error reading profiles file. Starting with an empty profile list!"
ERROR_SAVING_FILE_MSG = "Error saving profiles!"
INVALID_CHOICE_MSG = "Invalid choice. Please try again."
INVALID_INPUT_MSG = "Invalid input. Please enter a number."
INCORRECT_PASSWORD_MSG = "Incorrect password. Please try again."



# A function to load profiles from a file
def load_profiles() -> List[Dict[str, str]]:
    """Load profiles from JSON file."""
    if os.path.exists(PROFILES_FILE):
        try:
            with open(PROFILES_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(ERROR_READING_FILE_MSG)
            return []   
    return []

def save_profiles(profiles: List[Dict[str, str]]) -> None:
    """Save profiles to a JSON file."""
    try:
        with open(PROFILES_FILE, 'w') as file:
            json.dump(profiles, file, indent=4)
    except IOError:
        print(ERROR_SAVING_FILE_MSG)

def get_unique_name(profiles: List[Dict[str, str]]) -> str:
    """Prompt the user for a unique profile name."""
    while True:
        name = input("Enter your name: ")
        if any(profile['name'] == name for profile in profiles):
            print(PROFILE_EXISTS_MSG)
        else:
            return name
        
def get_confirmed_password() -> str:
    """Prompt user for a password and confirm it."""
    while True:
        password = getpass.getpass("Enter your password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        if password == confirm_password:
            break 
        else:
            print(PASSWORD_MISMATCH_MSG)

def create_profile(profiles):
    """Create a new profile and add it to the profiles list."""
    name = get_unique_name(profiles)
    password = get_confirmed_password()
    profiles.append({"name": name, "password":password})
    save_profiles(profiles)
    return name

def select_profile(profiles):
    """Display profiles and allow the user to select or create one."""
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
                    print(INCORRECT_PASSWORD_MSG)
            
            else:
                print(INVALID_CHOICE_MSG)
        except ValueError:
            print(INVALID_INPUT_MSG)

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
