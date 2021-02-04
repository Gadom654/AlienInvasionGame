favorite_languages={
	'Janek':'Pyhton',
	'sara':'C',
	'edward':'Ruby',
	'pawel':'Python'
}
i = 0
ppl=['Janek','sara','edward','pawel','lukasz','marcin']
# for n in sorted(favorite_languages.keys()):
# 	if n in ppl:
# 		print(n + " thanks for your help.")
for p in ppl:
		if p not in  favorite_languages.keys():
			print(p + " please take a part in my form")
		else:
			print(p + " thanks for your help.")