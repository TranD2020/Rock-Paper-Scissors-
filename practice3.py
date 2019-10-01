print("Hello, this is the Custom Calendar.")

day = input("What is today(monday/tuesday/wednesday/thursday/friday/saturday/sunday): ")

if day == "monday":
	print("It's Monday, the weekend is over")
elif day == "friday":
	print("It's Friday, the weekend is close")
elif day == "saturday" or "sunday":
	print("It's the weekend, time to relax")
else:
	print("Its not the weekend yet")