import json
import os
import getpass
from typing import List, Dict

class ProfileManager:
    PROFILES_FILE = 'profiles.json'
    PROFILE_EXISTS_MSG = "Profile name already exists. Please choose a different name."
    PASSWORD_MISMATCH_MSG = "Passwords do not match. Please try again."
    ERROR_READING_FILE_MSG = "Error reading profiles file. Starting with an empty profile list!"
    ERROR_SAVING_FILE_MSG = "Error saving profiles!"
    INVALID_CHOICE_MSG = "Invalid choice. Please try again."
    INVALID_INPUT_MSG = "Invalid input. Please enter a number."
    INCORRECT_PASSWORD_MSG = "Incorrect password. Please try again."

    def __init__(self):
        self.profiles = self.load_profiles()

    def load_profiles(self) -> List[Dict[str, str]]:
        """Load profiles from a JSON file."""
        if os.path.exists(self.PROFILES_FILE):
            try:
                with open(self.PROFILES_FILE, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(self.ERROR_READING_FILE_MSG)
                return []
        return []

    def save_profiles(self) -> None:
        """Save profiles to a JSON file."""
        try:
            with open(self.PROFILES_FILE, 'w') as file:
                json.dump(self.profiles, file, indent=4)
        except IOError:
            print(self.ERROR_SAVING_FILE_MSG)

    def get_unique_name(self) -> str:
        """Prompt the user for a unique profile name."""
        while True:
            name = input("Enter your name: ")
            if any(profile['name'] == name for profile in self.profiles):
                print(self.PROFILE_EXISTS_MSG)
            else:
                return name

    def get_confirmed_password(self) -> str:
        """Prompt the user for a password and confirm it."""
        while True:
            password = getpass.getpass("Enter your password: ")
            confirm_password = getpass.getpass("Confirm your password: ")
            if password == confirm_password:
                return password
            else:
                print(self.PASSWORD_MISMATCH_MSG)

    def create_profile(self) -> str:
        """Create a new profile and add it to the profiles list."""
        name = self.get_unique_name()
        password = self.get_confirmed_password()
        self.profiles.append({"name": name, "password": password})
        self.save_profiles()
        return name

    def select_profile(self) -> str:
        """Display profiles and allow the user to select or create one."""
        print("Profiles:")
        for idx, profile in enumerate(self.profiles, start=1):
            print(f"{idx}. {profile['name']}")
        print(f"{len(self.profiles) + 1}. Create a new profile")

        while True:
            try:
                choice = int(input("Select a profile: "))
                if choice == len(self.profiles) + 1:
                    return self.create_profile()
                elif 1 <= choice <= len(self.profiles):
                    selected_profile = self.profiles[choice - 1]
                    password = getpass.getpass("Enter your password: ")
                    if password == selected_profile['password']:
                        return selected_profile['name']
                    else:
                        print(self.INCORRECT_PASSWORD_MSG)
                else:
                    print(self.INVALID_CHOICE_MSG)
            except ValueError:
                print(self.INVALID_INPUT_MSG)

def application_start_up() -> None:
    """Start the application and handle user profile selection."""
    profile_manager = ProfileManager()
    if not profile_manager.profiles:
        print("No profiles found. Let us create one.")
        user = profile_manager.create_profile()
    else:
        print("Who is using the program?")
        user = profile_manager.select_profile()

    print(f"Welcome, {user}!")

if __name__ == "__main__":
    application_start_up()