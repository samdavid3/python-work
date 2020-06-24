pizzas = ["pepparoni", "veggie", "cheese"]

for pizza in pizzas:
	print(f"I like {pizza}")
print("\nI really like Pizza")

for value in range(1,21):
	print(value)

#list of a million
millionmiles = [value for value in range(1,1000001)]
for mile in millionmiles:
	print(mile)

print(f"the lowest number on the list is {min(millionmiles)}")
print(f"the maximum number on the list is {max(millionmiles)}")
print(f"the sum of a millionmiles is {sum(millionmiles)}")