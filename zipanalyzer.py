import zipfile, csv
import os

inputzip = input("Enter the Zip File:")

file = zipfile.ZipFile(inputzip, "r")

inputcsv = input("Enter the name of the CSV file: ")
csvfile = open(inputcsv, 'a')
b = open(inputcsv, 'w')
print ("The list of files in the zipped : ")

for name in file.namelist():
		print (name)
		
print ("The path of the CSV file : ")

print (os.path.abspath(inputcsv))
		
def filecount(name):

	d = {"lines":0, "words":0, "lengths":[]}
	with open(name, 'r') as f:
		for line in f:
			spl = line.split()
			d["lines"] += 1
			d["words"] += len(spl)
			d["lengths"].append(sum(len(word) for word in spl))
	return d
	
def main():
	for name in file.namelist():
		data = filecount(name)
	
	
		for ind, s in enumerate(data["lengths"], 1):
			
			a = csv.writer(b)
			data = [name, ind, s]
			a.writerow(data)
				
main()



