def build_profile(first,last,**user_info):
	profile = {}
	profile["First name:"] = first.title()
	profile["Last name:"] = last.title()
	for k,v in user_info.items():
		profile[k]=v
	return profile
user_profile = build_profile("dominik","gadomski",location = "Wroclaw",
	field = "Math")
print(user_profile)