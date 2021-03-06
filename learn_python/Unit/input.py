#How the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

##########################################################################################

#Writing Clear Prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

##########################################################################################

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

##########################################################################################

#Using int() to Accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

##########################################################################################
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")