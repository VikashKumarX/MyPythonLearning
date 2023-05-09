import csv
samplefilename = "Demosample_hotels.csv"
#open the csv file
with open(samplefilename, newline="") as csvfile:
    #create a reader object
    reader = csv.reader(csvfile, delimiter=",")

    #loop through the rows in the csv file
    for row in reader:
        #print out the contents of each row
        print(row)