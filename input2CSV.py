import csv


def average(focus, n):
    avg = focus / n
    return avg

def readCSV():
    d = dict()
    with open('data.csv', 'r') as data:
        csvReader = csv.reader(data)
        for line in csvReader:
            if line[0] not in d:
                d[line[0]] = [[float(line[1]),1],[float(line[2]),1],[float(line[3]),1],[float(line[4]),1], float(line[5])]
            else:
                for i in range(len(d[line[0]]) - 1):
                    d[line[0]][i][0] += float(line[i+1])
                    d[line[0]][i][1] += 1
    return d

def writeCSV(data):
    with open('data.csv', 'w') as f:
        
        csvWriter = csv.writer(f)
        for className in data:
            hwFocus = average(data[className][0][0], data[className][0][1])
            rFocus = average(data[className][1][0], data[className][1][1])
            nFocus = average(data[className][2][0], data[className][2][1])
            cFocus = average(data[className][3][0], data[className][3][1])
            grade = float(data[className][4])
            csvWriter.writerow([className, hwFocus, rFocus, nFocus, cFocus, grade])

# def getInput(data):
#     print('Enter Class: ')
#     className = input()
#     if className not in data:
#         data[className] = [[0,0],[0,0],[0,0],[0,0],0]
#     print('Enter HW: ')
#     data[className][0][0] += int(input())
#     print('Enter Reading: ')
#     data[className][1][0] += int(input())
#     print('Enter Note-Taking: ')
#     data[className][2][0] += int(input())
#     print('Enter In-Class: ')
#     data[className][3][0] += int(input())
#     print('Enter Grade: ')
#     data[className][4] = int(input())

#     for i in range(len(data[className])-1):
#         data[className][i][1] += 1
    
#     print(data)

def clean():
    lines = list()
    with open('data.csv', 'r') as data:
        reader = csv.reader(data)
        for line in reader:
            if line != []:
                lines.append(line)
    with open('data.csv', 'w') as data:
        writer = csv.writer(data)
        writer.writerows(lines)
