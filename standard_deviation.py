import csv
import math

with open("data_deviation.csv" , newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#data = file_data[0]

def mean():
    n = len(file_data[0])
    total = 0

    for x in file_data[0]:
        total = total+ int(x)

    mean = total/n
    print(mean)
    return mean

squared_list = []

for x in file_data[0]:
    a = int(x) - mean()
    a = a**2
    squared_list.append(a)

total_sum = 0

for total in squared_list:
    total_sum = total_sum + total

result = total_sum/len(file_data[0])-1

strd_de = math.sqrt(result)

print(strd_de)
