from colorama import Fore, Style

class Wizard:
    def __init__(self):
        self.details = {
            'Name': '',
            'Email': '',
            'Birth Date': '',
            'City': '',
            'Street': '',
            'Number': '',
            'Social Media': '',
            'Hobbies': ''
        }
        self.current_phase = 1

    def start_new(self):
        self.current_phase = 1
        self.phase_1()

    def phase_1(self):
        print(Fore.YELLOW + "Phase 1: User Information")
        self.get_name()
        self.get_email()
        self.get_birth_date()
        print(Fore.YELLOW + "\nDetails after Phase 1:")
        self.display_details()
        self.next_or_prev()

    def phase_2(self):
        print(Fore.YELLOW + "\nPhase 2: Address Information")
        self.get_city()
        self.get_street()
        self.get_number()
        print(Fore.YELLOW + "\nDetails after Phase 2:")
        self.display_details()
        self.next_or_prev()

    def phase_3(self):
        print(Fore.YELLOW + "\nPhase 3: Social Media and Hobbies")
        self.get_social_media()
        self.get_hobbies()
        self.display_summary()
        print(Fore.YELLOW + "\nDetails after Phase 3:")
        self.display_details()

    def display_details(self):
        for key, value in self.details.items():
            print(Fore.WHITE + f"{key}: {value}")


    def get_name(self):
        name = input(Fore.WHITE + "Enter your full name (First Name Last Name): ")
        if len(name.split()) == 2 and len(name.split()[0]) >= 2 and len(name.split()[1]) >= 2:
            self.details['Name'] = name
        else:
            print(Fore.RED + "Invalid name format. Please enter at least 2 characters for both first and last names.")
            self.get_name()

    def get_email(self):
        email = input("Enter your email address: ")
        # Basic email format validation
        if "@" in email and "." in email:
            self.details['Email'] = email
        else:
            print(Fore.RED + "Invalid email format. Please enter a valid email address.")
            self.get_email()

    def get_birth_date(self):
        birth_date = input("Enter your birth date (dd/MM/yy): ")
        # Basic date format validation
        if len(birth_date) == 8 and birth_date.count('/') == 2:
            self.details['Birth Date'] = birth_date
        else:
            print(Fore.RED + "Invalid date format. Please enter the date in dd/MM/yy format.")
            self.get_birth_date()

    def get_city(self):
        city = input(Fore.WHITE + "Enter your city: ")
        if len(city) >= 2:
            self.details['City'] = city
        else:
            print(Fore.RED + "City name must be at least 2 characters long.")
            self.get_city()

    def get_street(self):
        street = input("Enter your street: ")
        if len(street) >= 2:
            self.details['Street'] = street
        else:
            print(Fore.RED + "Street name must be at least 2 characters long.")
            self.get_street()

    def get_number(self):
        number = input("Enter your house number (leave blank if none): ")
        if number == '' or (number.isdigit() and int(number) > 0):
            self.details['Number'] = number
        else:
            print(Fore.RED + "Invalid house number. Please enter a valid number.")
            self.get_number()

    def get_social_media(self):
        social_media = input(Fore.WHITE + "Enter your social media URL: ")
        # Basic URL validation
        if social_media.startswith(('http://', 'https://')) and any(platform in social_media for platform in ['facebook', 'twitter', 'instagram', 'linkedin']):
            self.details['Social Media'] = social_media
        else:
            print(Fore.RED + "Invalid social media URL. Please enter a valid URL from Facebook, Twitter, Instagram, or LinkedIn.")
            self.get_social_media()

    def get_hobbies(self):
        hobbies = input("Enter your hobbies (comma-separated): ")
        # No validation required for hobbies input
        self.details['Hobbies'] = hobbies

    def next_or_prev(self):
        action = input(Fore.CYAN + "\nEnter 'next' to proceed or 'prev' to go back: ")
        if action.lower() == 'next':
            self.current_phase += 1
            if self.current_phase == 2:
                self.phase_2()
            elif self.current_phase == 3:
                self.phase_3()
        elif action.lower() == 'prev':
            self.current_phase -= 1
            if self.current_phase == 1:
                self.phase_1()
            elif self.current_phase == 2:
                self.phase_2()
        else:
            print(Fore.RED + "Invalid input. Please enter 'next' or 'prev'.")
            self.next_or_prev()

    def display_summary(self):
        print(Fore.YELLOW + "\nSummary:")
        for key, value in self.details.items():
            print(Fore.WHITE + f"{key}: {value}")
        print(Style.RESET_ALL + "\nThank you for providing your details!")

def main():
    wizard = Wizard()

    while True:
        choice = input(Fore.GREEN + "\nMenu: 1) Start New 2) Continue\nEnter your choice: ")

        if choice == '1':
            wizard.start_new()
        elif choice == '2':
            phase = int(input("Enter the phase number you want to continue from (1-3): "))
            wizard.current_phase = min(max(phase, 1), 3)
            if wizard.current_phase == 1:
                wizard.phase_1()
            elif wizard.current_phase == 2:
                wizard.phase_2()
            elif wizard.current_phase == 3:
                wizard.phase_3()
        else:
            print(Fore.RED + "Invalid choice. Please enter '1' to start new or '2' to continue.")

if __name__ == "__main__":
    main()
