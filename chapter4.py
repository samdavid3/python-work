pizzas = ["pepparoni", "veggie", "cheese", "supreme"]

for pizza in pizzas:
	print(f"I like {pizza}")
print("\nI really like Pizza")

# for value in range(1,21):
# 	print(value)

#list of a million
#millionmiles = [value for value in range(1,1000001)]
#for mile in millionmiles:
#	print(mile)

# print(f"the lowest number on the list is {min(millionmiles)}")
# print(f"the maximum number on the list is {max(millionmiles)}")
# print(f"the sum of a millionmiles is {sum(millionmiles)}")
# odd = [value for value in range(1,20,2)]
# print(odd)
# multiplesof3 = [value*3 for value in range (1,30)]
# for multiple in multiplesof3:
# 	print(multiple)

#cubed list
# cubed= [value**3 for value in range(1,11)]
# for cube in cubed:
# 	print

#splicing
print(f"the first 3 items are {pizzas[:3]}")
print(f"the last item is {pizzas[-1:]}")
print(pizzas[1])

#copying
pizzas.append("hamburger")
myfriendspizzas=pizzas[:]
myfriendspizzas.append("hawaiian")
print("My Pizzas Are")
for pizza in pizzas:
	print(pizza)
print("\nMy Friends Pizzas Are")
for pizza in myfriendspizzas:
	print(pizza)