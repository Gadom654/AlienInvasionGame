pizzas= ["pepperoni","jalapeno","gyros"]
friend_pizzas = pizzas[:]
pizzas.append("Kebab")
friend_pizzas.append("Hawai")
print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)