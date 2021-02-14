sandwitch_orders = ["chicken","bacon","egg","lamb"]
finished_sandwitches = []
while sandwitch_orders:
	ready_order = sandwitch_orders.pop()
	finished_sandwitches.append(ready_order)
	print("Sandwitch with", ready_order, "is ready.")
for finished_sandwitch in finished_sandwitches:
	print(finished_sandwitch)