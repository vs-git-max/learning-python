# if statements

is_hot = True
is_cold = False
if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")


# house pricing program
has_good_credit = True
price = 1000000
if has_good_credit:
    amount = 0.1 * price
else:
    amount = 0.2 * price


#  print(amount)

# continuing with the conditionals
cars = ["bmw", "ford", "toyota", "subaru", "noah"]

for car in cars:
    if car.strip().lower() != "bmw":
        print(car.upper())
    else:
        print(car.title())


# more operations


age = 100

if age < 18:
    print("Make sure you're above 18")
elif age >= 18 and age < 65:
    print("You can take the drink")
else:
    print("Die nigger")


# checking whether a value is in the list
print("bmw" in cars)


main_car = "bmw"

if main_car not in cars:
    print(f"{main_car.title()} is not in the list.")
else:
    print(f"{main_car.title()} in the list.")


alien_color = "yellow"
if alien_color == "green":
    points = 5
elif alien_color == "red":
    points = 15
elif alien_color == "yellow":
    points = 10


print(f"You have earned yourself {points} points")


# stages of life thing

vowels = ["a", "e", "i", "o", "u"]


age = 19
if age < 2:
    stage = "baby"
elif age >= 2 and age < 4:
    stage = "toddler"
elif age >= 4 and age < 13:
    stage = "kid"
elif age >= 13 and age < 20:
    stage = "teenager"
elif age >= 20 and age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"


first_letter = stage[0]
if first_letter in vowels:
    prefix = "an"
else:
    prefix = "a"

print(prefix)
print(f"Based on your age you're {prefix} {stage}")
