"""
Write a program that writes the first four powers of the numbers between 1 and 1,000 in comma-separated
fields to the file powers.txt
"""

# Open the file in write mode
with open('powers.txt', 'w') as file:
    # Iterate through numbers from 1 to 1000
    for num in range(1, 1001):
        powers = [str(num**i) for i in range(1, 5)]  # Calculate the first four powers of the number
        line = ','.join(powers) + '\n'  # Join powers with commas and add a newline
        file.write(line)  # Write the line to the file
