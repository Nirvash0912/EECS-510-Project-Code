import csv

# Get text from tweet metadata files

def readFiles(files):
	texts = []
	for file in files:
		with open(file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			csvfile.readline()
			for row in reader:
				texts.append(row[4])
	return texts

def main():
	files = ['../output_got_part_1.csv', '../output_got_part_2.csv', '../output_got_part_3.csv']
	texts = readFiles(files)

	length = len(texts)

	i = 1
	start = 0
	now = start
	while length > 0:
		with open("./sentiment140_input/text" + str(i) + ".csv", "w") as outputfile:
			while now - start < 10000:
				if length == 0:
					break
				outputfile.write(texts[now] + "\n");
				length -= 1
				now += 1
			start = now
		i += 1
		
main()

