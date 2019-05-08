import csv

with open('movie_metadata.csv', 'r') as csvFile:
	reader = csv.DictReader(csvFile)
	for row in reader:
		print(row['director_name'])
		


csvFile.close()