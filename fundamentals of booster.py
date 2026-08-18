print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favorite number: "))

print("Thank you! Here is the information we have collected:")

print("Name: ", name, "(Type: ", type(name), ", Memory Address: ", id(name), ")")
print("Age: ", age, "(Type: ", type(age), ", Memory Address: ", id(age), ")")
print("Height: ", height, "(Type: ", type(height), ", Memory Address: ", id(height), ")")
print("Favorite Number: ", fav_num, "(Type: ", type(fav_num), ", Memory Address: ", id(fav_num), ")")


birth_year = 2026 - age 
print("Your birth year is approximately : " , birth_year, "(based on your age of)", age)

rounded_height = int(height)
print("Your rounded height is :", rounded_height)

print("Thank you for using the personal data collector. Goodbye!")


