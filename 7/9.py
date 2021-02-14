sandwitch_orders = ["chicken","bacon","egg","lamb","pastram","pastram","pastram"]
finished_sandwitches = []
print("I'm sorry but we'r actualy out of pastrami.")
while sandwitch_orders:
	ready_order = sandwitch_orders.pop()
	if ready_order == "pastram":
		continue
	else:
		finished_sandwitches.append(ready_order)
		print("Sandwitch with", ready_order, "is ready.")
for finished_sandwitch in finished_sandwitches:
	print(finished_sandwitch)