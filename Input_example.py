name = input("What is your name?")
age = int(input("How old will you be this year?"))
try:
    age = int(age)
    birth_year = 2023 - age
except ValueError:age
    print( "sorry, that was not a valid number" )
except NameError:
    print("sorry, that was not a valid number")
else:
    print(name, "you were born in", birth_year)
finally:
    print("Thanks for playing, come again")





