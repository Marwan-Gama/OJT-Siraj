"""
Some of the countries population is shown in this file and are given in the tab-delimited text file at
https://drive.google.com/file/d/1zQv1XJ5u4SxQHz3PdvLn0OB41JaO7wsE/view?usp=sharing
• Write a Python program to read in this data and report:
• 1- The most populated country
• 2- Which country is the most crowded and which is the least one
• 3- Who’s the oldest country? Who’s the newest?
• 4- List how many countries there are for each continent
"""


# Read the data from the file
with open('country_population.txt', 'r') as file:
    lines = file.readlines()[1:]  # Skip the header line

    # Initialize variables to store required information
    max_population = 0
    most_populated_country = ''
    most_crowded_country = ''
    least_crowded_country = ''
    oldest_date = ''
    newest_date = ''
    continent_count = {}

    for line in lines:
        data = line.strip().split(',')  # Split the line by comma

        country = data[0]
        population = int(data[1])
        established_date = data[4]
        continent = data[5]

        # Finding the most populated country
        if population > max_population:
            max_population = population
            most_populated_country = country

        # Finding the most crowded and least crowded countries
        if most_crowded_country == '' or population > int(lines[0].split(',')[1]):
            most_crowded_country = country
        if least_crowded_country == '' or population < int(lines[0].split(',')[1]):
            least_crowded_country = country

        # Finding the oldest and newest countries
        if oldest_date == '' or established_date < oldest_date:
            oldest_date = established_date
            oldest_country = country
        if newest_date == '' or established_date > newest_date:
            newest_date = established_date
            newest_country = country

        # Counting countries for each continent
        if continent in continent_count:
            continent_count[continent] += 1
        else:
            continent_count[continent] = 1

    # Printing the results
    print(f"The most populated country is: {most_populated_country}")
    print(f"The most crowded country is: {most_crowded_country}")
    print(f"The least crowded country is: {least_crowded_country}")
    print(f"The oldest country is: {oldest_country}")
    print(f"The newest country is: {newest_country}")
    print("Number of countries for each continent:")
    for continent, count in continent_count.items():
        print(f"{continent}: {count}")
