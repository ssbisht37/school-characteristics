file = open("Public_School_Characteristics_2018-19.csv","r").read()

file = file.replace(',,', ',?,')
file = file.replace(',,', ',?,')
file = file.replace(',"', ',')
file = file.replace('",', ',')
file = file.replace('""', '"')

fout = open("Public_School_Characteristics_2018-19_?Miss.csv","w")
fout.write(file)
fout.close()
