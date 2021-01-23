import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

def mean(new_data):
    n = len(new_data)
    total = 0
    for x in new_data:
        total += x

    mean = total/n
    print('The mean is:', str(mean))

def median(new_data):
    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        median = (median1+median2)/2
    else:
        median = new_data[n//2]
        print(n)

    print(median, "is the median")

def mode(new_data):
    data = Counter(new_data)
    mode_data = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }

    for weight, occurence in data.items():
        if 75 < float(weight) < 85:
            mode_data["75-85"] += occurence
        elif 85 < float(weight) < 95:
            mode_data["85-95"] += occurence
        elif 95 < float(weight) < 105:
            mode_data["95-105"] += occurence
        elif 105 < float(weight) < 115:
            mode_data["105-115"] += occurence
        elif 115 < float(weight) < 125:
            mode_data["115-125"] += occurence
        elif 125 < float(weight) < 135:
            mode_data["125-135"] += occurence
        elif 135 < float(weight) < 145:
            mode_data["135-145"] += occurence
        elif 145 < float(weight) < 155:
            mode_data["145-155"] += occurence
        elif 155 < float(weight) < 165:
            mode_data["155-165"] += occurence
        elif 165 < float(weight) < 175:
            mode_data["165-175"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence
        
    mode = float((mode_range[0]+mode_range[1])/2)

    print('Mode is ->', mode)

mean(new_data)
median(new_data)
mode(new_data)