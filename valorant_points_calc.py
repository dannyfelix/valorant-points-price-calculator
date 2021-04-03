import time

# Uses the bundle's VP value as a key to point to its respective price.
microtx = {
    525:4.99,
    1100:9.99,
    2250:19.99,
    4000:34.99,
    5800:49.99,
    12000:99.99,
}

target = int(input("Enter the amount of Valorant Points (VP) you want to calculate the cost for: "))
print("\nOptionally, you can specify how much VP you currently have to get a more accurate result.")
curr = int(input("This will deduct it from your specified amount, leaving blank will default to 0: ") or 0)

if curr > target:
    print("You already have enough VP, the program will exit in 5 seconds.")
    time.sleep(5)
    exit()

target -= curr

print("\nTo get", target, "Valorant Points, you could buy...\n")

print('  ----------------------------------------------------------------')

for x in microtx:
    calc = 0
    counter = 0 
    while calc < target:
        calc += x
        counter += 1
    diff = 0
    diff = target / x # how much the target is as a percentage compared to the current VP bundle price
    print(
    f'''
    The [{x}] bundle {counter} time(s) for £{'%0.2f' % (microtx[x]*counter)}, giving you {x*counter} VP,
    Buying this much would mean {target} VP would cost you £{'%0.2f' % (microtx[x]*diff)}, 
    This would leave you with {(x*counter)-target} VP left over.
    ''')
    print('  ----------------------------------------------------------------')
    time.sleep(0.5)

