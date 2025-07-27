age = 65
if age < 18: 
    print("You're a minor.")
elif age < 65:
    print("You're an adult.")
else: 
    print("You're a senior.")


for i in range(5):
     print(i)

n = 0
while n < 5:
     print(n)
     n += 1
    
for i in range(10):
     if i == 3:
          continue
     if i == 7: 
          break
     print(i)


old = int(input("Type your age:"))
if old < 13: 
    print("You're a child.")
elif old >= 13 and old < 20:
    print("You're a teenager.")
elif old >= 20 and old < 65:
    print("You're and adult.")
else: 
    print("You're a senior.")

guess = 0
while guess != 7:
    guess = int(input("Guess my secret number:"))
print("You guessed my number!  7 was it.")
