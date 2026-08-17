print("Welcome to the Interactive Personal Data Collector!")


name = input("Please enter your name: ")
age = int(intput("Please enter your age: "))
height = float(intput("Please enter your height in meters: "))
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


Output:
Welcome to the Interactive Personal Data Collector!

Please enter your name: Armin
Please enter your age: 23
Please enter your height in meters: 1.75
Please enter your favorite number: 10

Thank you! Here is the information we have collected:

Name: Armin (Type: <class 'str'> , Memory Address: 140123456789456 )
Age: 20 (Type: <class 'int'> , Memory Address: 140123456780112 )
Height: 1.75 (Type: <class 'float'> , Memory Address: 140123456781904 )
Favorite Number: 7 (Type: <class 'int'> , Memory Address: 140123456779888 )

Your birth year is approximately: 2003 (based on your age of 23)
Your rounded height is: 1

Thank you for using the Personal Data Collector. Goodbye!