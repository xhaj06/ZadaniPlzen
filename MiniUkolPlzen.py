import wikipedia
wikipedia.set_lang("cs")
encoding = 'utf-8'

def Zadej():

	if __name__== "__main__":
		try:
			name = sys.argv[1]
		except:
			name = input("Zadejte název článku\n")
	print ("---------")
	return name


def hledani(slovo):
	print(f'Článek s názvem "{slovo}" nebyl nalezen. Zadaný text se vyskytuje v článcích s tímto názvem:')
	print(wikipedia.search(name))

name = Zadej ()
try:
	nalez = wikipedia.page(name)
	print (nalez.title)
	if str.lower(nalez.title) == str.lower(name):
		shrnuti= str(wikipedia.summary(name))
		print (shrnuti)
	else: 
		hledani(name)
except wikipedia.exceptions.PageError: 
	hledani(name)
