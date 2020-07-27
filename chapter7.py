message = input("Enter your you car preference: ")
print(f"Let me help you from your {message}")

nos= input("how many people in your dinner party")
nos = int(nos)
if nos >8:
	print("please call in to reserve your table")
else:
	print("no need for reservation. your table is available")
