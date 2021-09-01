import sys
import glob
import os

#cestaKSouboru ='c:\Prace\Soubory'
nalezeno = 0
#souboru=0
#-------Nazev Input-------
if __name__== "__main__":
    try:
        name = sys.argv[1]
    except:
        name = input("Zadejte název článku\n")

    #print(name)

print ("---------")

#-------Hledani Clanku--------
#os.chdir(cestaKSouboru)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for file in glob.glob("*.txt"):
	#souboru +=1
    #print(file[:-4])
	if file[:-4]==name:
		f = open(file ,'r',encoding="utf8")
		file_contents = f.read()
		print(file_contents)
		
		nalezeno=1

#-------Hledani Slova-------
#print(souboru)
#jeTam=[0 for x in range (souboru)]
#poradi=0
if nalezeno == 0:
	for file in glob.glob("*.txt"):
		f = open(file ,'r',encoding="utf8")
		file_contents = f.read()
		if name in file_contents:
			if nalezeno==0:
				print(f'Článek s názvem "{name}" nebyl nalezen. Zadaný text se vyskytuje v článcích s tímto názvem:')
				nalezeno=1
			print(file[:-4])
			#jeTam[poradi]=1
		#poradi += 1

if nalezeno == 0:
	print("Bohuzel jsme nenašli žádny soubor ani text odpovidající zadaným parametrům")
	




		#print('Článek s názvem "', name, '" nebyl nalezen. Zadaný t ext se v yskytujev článcích s tímto názvem:')
		#print 'Článek s názvem "' +  name + 'nebyl nalezen. Zadaný t ext se v yskytujev článcích s tímto názvem:'
		
	

