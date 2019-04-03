def title():
	print("You are meeting with Tabbs.")
	print("I must leave you now. Best of luck.")

def add(op1, op2):
	return op1 + op2

title()

print("Here iss tabbs.")
age = int(input("How old iss you? "))
while age < 18:
	print ("You are ssstill young...")
	print("Chosen... return in " + str(18-age) + " years...")
	print("We shall see each other then...")
	age = int(input("Are you certain of your age? Repeat it... "))
if age >= 18:
	print("Yessss... Chosen... come to tabbs.")
	print("I've waited " + str(add(age, 78)) + " years for thisss...")
