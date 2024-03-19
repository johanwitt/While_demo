Temperature conversion program

Celsius -> Fahrenheit / Fahrenheit -> Celsius

Including loop validation on users conversion choice

'''

# Display messages

print("This program will convert temperatures")

print("Enter C to convert Celsius to Fahrenheit")

print("Enter F to convert Fahrenheit to Celsius")

# Get user choice

which = input("Enter selection (F or C): ")

# loop if users choice not correct until correct entry entered

while which != 'C' and which != 'F':

    which = input("'Invalid choice'. Enter selection (F or C): ")

# Determine temperature conversion based on user choice, then display result

if which == 'C' :

# Read temperature data

    temp = float(input("Enter Celsius temperature: "))

    convertedTemp = (9/5) * temp + 32

    print(temp, 'in Celsius is', convertedTemp, 'in Fahrenheit')

else :

# Read temperature data

    temp = float(input("Enter Fahrenheit temperature: "))

    convertedTemp = (temp - 32) * (5/9)

    print(temp, 'in Fahrenheit is', convertedTemp, 'in Celsius')
