# Virus Simulation Game
# The Countries

# List of dictionaries containing countries and infected people numbers
countries_infected = [
    {"Country": "New Zealand", "Infected People": 150000},
    {"Country": "Australia", "Infected People": 150000},
    {"Country": "Mexico", "Infected People": 200000},
    {"Country": "Italy", "Infected People": 200000},
    {"Country": "France", "Infected People": 150000},
    {"Country": "China", "Infected People": 250000},
    {"Country": "Canada", "Infected People": 150000},
]

# Define the game  
print("Welcome to Virus Simulation Game\nEach day user can choose to help only one country between 6 countries, within 5 days.")
print("The number of infected for the helped country decreases by 40%, whereas the other countries increase by 20%.")

# Loop for 5 days
for day in range(1, 6):
    print(f"\nDay {day}")
    print("Countries status:")
    for entry in countries_infected:
        print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']} \n ")

    # Check for valid country
    valid_country = False
    while not valid_country:
        help_country = input("Enter the country to help: ")
        for entry in countries_infected:
            if entry['Country'].lower() == help_country.lower():
                valid_country = True
                break
        if not valid_country:
            print("Invalid country name. Please enter a valid country name from the list.")

    # Apply the changes and Display the final status of each country
    for entry in countries_infected:
        if entry['Country'].lower() == help_country.lower():
            entry['Infected People'] *= 0.6  # Reduce by 40%
        else:
            entry['Infected People'] *= 1.2  # Increase by 20%

# Display the final status of each country and determine lockdown status
print("\nFinal status of countries after 5 days:")
lockdown_occurred = False
for entry in countries_infected:
    lockdown_status = "Yes" if entry['Infected People'] > 375000 else "No"
    print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']:.0f}, On Lockdown: {lockdown_status}")
    if lockdown_status == "Yes":
        lockdown_occurred = True

# Determine if the player wins or loses
if lockdown_occurred:
    print("\nYou lose! One or more countries went into lockdown.")
else:
    print("\nYou win! No countries went into lockdown.")
