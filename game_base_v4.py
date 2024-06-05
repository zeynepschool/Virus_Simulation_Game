##Virus Simulation Game
#The Countries

# List of dictionaries containing countries and infected people numbers
countries_infected = [
    {"Country": "New Zealand", "Infected People": 150000},
    {"Country": "Australia", "Infected People": 150000},
    {"Country": "Mexico", "Infected People": 200000},
    {"Country": "Italy", "Infected People": 200000},
    {"Country": "France", "Infected People": 150000},
    {"Country": "China", "Infected People": 250000},
]

#Define the game  
print("Welcome to Virus Simulation Game\nEach day user can choose to help only one country between 6 countries, within 5 days.")
print("The number of infected for the helped country decreases by 40%, whereas the other countries increase by 20%.") 

#Print the list to verify
##for entry in countries_infected:
##    print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']}")

##print("Initial status of countries:")
##for entry in countries_infected:
##    print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']}")


# Loop for 5 days
for day in range(1, 6):
    print(f"\nDay {day}")
    print("Countries status:")
    for entry in countries_infected:
        print(f"Country: {entry['Country']}, Infected People: {entry['Infected People']}")


    #Select Country
    help_country = input("Enter the country to help: ")



# Apply the changes
    for entry in countries_infected:
        if entry['Country'].lower() == help_country.lower():
            entry['Infected People'] *= 0.6  # Reduce by 40%
        else:
            entry['Infected People'] *= 1.2  # Increase by 20%

