from math import ceil
from time import sleep
import json

with open('pricing.json') as json_file:
    data = json.load(json_file)

region = ""
print("Please type your region")
while region not in ["AU", "BR", "EU", "IN", "MX", "NZ", "NZ", "NA", "UK"]:
    region = input("AU, BR, EU, IN, MX, NZ, NA or UK: ")

target = int(input("Enter the amount of Valorant Points (VP) you want to calculate the cost for: "))

print("\nOptionally, you can specify how much VP you currently have to get a more accurate result.")
curr = int(input("This will deduct it from your specified amount, leaving blank will default to 0: ") or 0)

if curr > target:
    print("You already have enough VP, the program will exit in 5 seconds.")
    sleep(5)
    exit()

target -= curr

print("\nTo get", target, "Valorant Points, you could buy...\n")

print('  ----------------------------------------------------------------')
for key, value in data[f'{region}'].items():
    diff = target / value[0] # gets the multiplier needed to get from the bundle value to the target 
    count = ceil(diff) # count of times needed to buy bundle (diff will likely be float so needs to be rounded up)

    print(
    f'''
    The [{value[0]}] bundle {count} time(s) for £{'%0.2f' % (value[1]*count)}, giving you {value[0]*count} VP,
    Buying this much would mean {target} VP would cost you £{'%0.2f' % (value[1]*diff)}, 
    This would leave you with {(value[0]*count)-target} VP left over.
    ''')
    print('  ----------------------------------------------------------------')

