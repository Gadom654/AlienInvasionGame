current_users = ["lukasz","nukasz","Bukasz","hukasz","tukasz"]
new_users = ["lukasz","artur","bukasz","huku","duku"]
for new_user in new_users:
	if new_user.lower() in [current_user.lower() for current_user in current_users]:
		print("You'r username is already taken!")
	else:
		print("You can make new account with this username.")