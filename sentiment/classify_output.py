import csv
import os

# Splite result of sentiment140 into three classification files

def rwData():
	for filename in os.listdir("./sentiment140_output"):
		if filename.endswith(".csv"): 
			inputfilename = "./sentiment140_output/" + filename
			with open(inputfilename, 'rb') as inputfile, open("./sentiment_classification/positive.csv", "a") as positive, open("./sentiment_classification/negative.csv", "a") as negative, open("./sentiment_classification/neutral.csv", "a") as neutral:
				for line in inputfile:
					split = line.split(",", 1)
					classification = split[0].replace("\"", "")
					text = split[1].replace("\"", "")
					reFormat = classification + ";" + text

					if int(classification) == 0:
						negative.write(reFormat)
					elif int(classification) == 4:
						positive.write(reFormat)
					elif int(classification) == 2:
						neutral.write(reFormat)

def main():
	rwData()
main()