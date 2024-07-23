# Virus Simulation Game

# List of countries with initial infected people
countries = [
    {"Country": "New Zealand", "Infected People": 150000},
    {"Country": "Australia", "Infected People": 150000},
    {"Country": "Mexico", "Infected People": 200000},
    {"Country": "Italy", "Infected People": 200000},
    {"Country": "France", "Infected People": 150000},
    {"Country": "China", "Infected People": 250000},
    {"Country": "Canada", "Infected People": 150000},
]

def display_status(day, countries):
    # Function to display the status of each country at the end of each day
    print(f"\nDay {day}")
    print("Countries status:")
    for entry in countries:
        print(f"Country: {entry['Country']: <15} | Infected People: {entry['Infected People']:.0f} \n ")
    print("\n")

def update_infections(countries, help_country):
    # Function to update the infection counts
    for entry in countries:
        if entry['Country'].lower() == help_country.lower():
            entry['Infected People'] *= 0.6  # Reduce by 40%
        else:
            entry['Infected People'] *= 1.2  # Increase by 20%

def check_valid_country(countries, help_country):
    # Function checks that user input is a valid country from the list
    for entry in countries:
        if entry['Country'].lower() == help_country.lower():
            return True
    return False

def final_status(countries):
    # Function to display the final status and determine lockdown status
    lockdown_occurred = False
    print("\nFinal status of countries after 5 days:")
    for entry in countries:
        lockdown_status = "Yes" if entry['Infected People'] > 375000 else "No"
        print(f"Country: {entry['Country']: <15} | Infected People: {entry['Infected People']:.0f} | On Lockdown: {lockdown_status}")
        if lockdown_status == "Yes":
            lockdown_occurred = True
    return lockdown_occurred

def game_result(lockdown_occurred):
    # Function to determine and display the game result
    if lockdown_occurred:
        print("\nYou lose! One or more countries went into lockdown.")
    else:
        print("\nYou win! No countries went into lockdown.")

# Main game logic
border = '=' * 60
print(f"\n{border}")
print("Kia Ora, Welcome to Virus Simulation Game".center(60))
print(f"{border}")
print("\nEach day you can choose to help only one country. Helping a country decreases its infected count by 40%, while the other countries' infected counts increase by 20%.")
print("A country goes into lockdown after 375,000 infected people. Therefore, to win the game, you must make sure that the countries are under 375,000 infected people.\n")

# Loop for 5 days
for day in range(1, 6):
    display_status(day, countries)
   
    # Check for valid country
    valid_country = False
    while not valid_country:
        help_country = input("Enter the country to help: ")
        if check_valid_country(countries, help_country):
            valid_country = True
        else:
            print("Invalid country name. Please enter a valid country name from the list.")

  
    # Apply the changes
    update_infections(countries, help_country)

# Display the final status of each country and determine lockdown status
lockdown_occurred = final_status(countries)
game_result(lockdown_occurred)