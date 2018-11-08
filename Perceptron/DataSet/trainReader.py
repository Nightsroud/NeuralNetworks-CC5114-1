import csv

def trainReader():
    with open('Train-Norm-T1.csv', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
        next(reader)
        lineList = []
        for line in reader:
            lineList.append([int(line[0]), float(line[1]), float(line[2]), float(line[3]),
                                  float(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8])])
        file.close()
        return lineList