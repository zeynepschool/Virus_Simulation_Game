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
# Main game logic
print("Welcome to Virus Simulation Game")
print("Each day you can choose to help only one country. Helping a country decreases its infected count by 40%, while the other countries' infected counts increase by 20%.")

#Initial Statues of Countries
print("Initial status of countries:")
for entry in countries_infected:
    print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']} \n ")

# Loop for 5 days
for day in range(1, 6):
    print(f"\nDay {day}")

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
            print(f"\nHelped {entry['Country']}: Infected reduced to {entry['Infected People']:.0f}")
        else:
            entry['Infected People'] *= 1.2  # Increase by 20%
            print(f"\n{entry['Country']}: Infected increased to {entry['Infected People']:.0f}")

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

