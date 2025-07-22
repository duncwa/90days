name = input("What's your name?")
language = input("What is you favorite programming language?")
age = int(input("How old are you?"))

hundred = 100 - age + 2025
print(f"Hello {name}!  You're {age} years old and love {language}.")
print(f"You will be 100 years old in the year #{hundred}.")