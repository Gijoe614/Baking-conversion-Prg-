def convert(liter):
    cups = round((float(liter) * 4.2), 1)
    return cups

print("This program will convert liters to cups")
liters = raw_input("How many liters? ")

cups = convert(liters)
print (liters + "liters is equal to " + str(cups) + " cups")
