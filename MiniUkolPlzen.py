import sys
import glob
import os

nalezeno = 0

#-------Nazev Input-------
if __name__== "__main__":
    try:
        name = sys.argv[1]
    except:
        name = input("Zadejte název článku\n")


print ("---------")

#-------Hledani Clanku--------

os.chdir(os.path.dirname(os.path.abspath(__file__)))
for file in glob.glob("*.txt"):
	if file[:-4]==name:
		f = open(file ,'r',encoding="utf8")
		file_contents = f.read()
		print(file_contents)
		
		nalezeno=1

#-------Hledani Slova-------

if nalezeno == 0:
	for file in glob.glob("*.txt"):
		f = open(file ,'r',encoding="utf8")
		file_contents = f.read()
		if name in file_contents:
			if nalezeno==0:
				print(f'Článek s názvem "{name}" nebyl nalezen. Zadaný text se vyskytuje v článcích s tímto názvem:')
				nalezeno=1
			print(file[:-4])
			

if nalezeno == 0:
	print("Bohuzel jsme nenašli žádny soubor ani text odpovidající zadaným parametrům")
	
