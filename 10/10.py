file = "gatsby.txt"
with open(file) as f:
	content = f.read()
print(content.lower().count("in"))