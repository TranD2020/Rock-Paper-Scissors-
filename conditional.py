# Conditional 
print("Welcome to Ticket Bot")
print("You must be at least 18 to see R rated movies")
age = int(input("How old are you? "))

if age > 17: 
	print("You can go see an R rated movie")
else:
	print("You cannot go see an R rated movie")

print("Thank you")

mysteryNum = 6 
guess = int(input("Guess a number between 1 and 10: "))

if guess == mysteryNum:
	print("Good Guess, that is correct")
elif guess > 10:
	print("Please read directions")
elif guess > mysteryNum:
	print("Too High")
else:
	print("Too Low")

# conditional operators: >, <, >=, <=, == (is equal to), != (is not equal)

birthday = input("Is today your birthday(yes/no): ")
if birthday == "yes": 
	print("Happy Birthday")
elif birthday == "no": 
	print("Have a good day anyway")
else:
	print("Please read directions")