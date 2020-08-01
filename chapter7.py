# message = input("Enter your you car preference: ")
# print(f"Let me help you from your {message}")

# nos = input("how many people in your dinner party")
# nos = int(nos)
# if nos > 8:
#     print("please call in to reserve your table")
# else:
#     print("no need for reservation. your table is available")

# # Loops
# phrase = "\nPlease enter a pizza topping"
# phrase += "\nEnter exit to quit: "
# flag = "true"
# while flag:
#     request = input(phrase)
#     if request != "exit":
#         print(f"{request} has been added to the topping")
#     else:
#         break
# question = "Please enter your age of your children. Enter exit to stop: "
# number = input(question)
# while (number != "exit"):

#     number = int(number)
#     if (number < 3):
#         print("Free entry")
#     elif (number > 3 and number <= 12):
#         print("cost is 12 dollars")
#     elif(number > 12):
#         print("Cost is 15 dollars")
#     number = input(question)
# Loops with dictionaries and lists
sandwich_orders = ["tuna", "pastrami", "veggie", "salami", "pastrami"]
finished_orders = []
while sandwich_orders:
    finished = sandwich_orders.pop()
    finished_orders.append(finished)
    print(f"I have completed your {finished} sandwich")
for i in finished_orders:
    print(i)
sandwich_orders = ["tuna", "pastrami", "veggie", "salami", "pastrami"]
print("we have run out of Pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for j in sandwich_orders:
    print(j)

flag = "true"
person = {}
while flag == 'true':
    name = input("Please enter your name: ")
    location = input("Please enter your location: ")
    person[name] = location
    goon = input("Do you want to continue (y/n: ")
    if goon != 'y':
        flag = "false"
for p, i in person.items():
    print(f"{p} lives in {i}")
