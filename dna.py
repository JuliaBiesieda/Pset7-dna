import sys
import csv
import re

# check if user entered 2 command line arguments. If not, exit
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(0)

# open the csv file

with open(sys.argv[1], "r") as read_obj:
    reader = csv.reader(read_obj)
    sequence_list = (next(reader))[1:]
    # print(sequence_list)

with open(sys.argv[1], "r") as csv_file:

    # read the data
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    result = {}
    for row in csv_reader:
        key = row[0]
        if key in result:
            pass
        result[key] = row[1:]
        result[key] = [int(i) for i in result[key]]
    # print(result)

with open(sys.argv[2]) as sequence_txt:
    check = []
    sequence_txt = sequence_txt.read()
    for item in sequence_list:
        pattern = item
        counter = 0
        while pattern in sequence_txt:
            counter += 1
            pattern += item
        check.append(counter)
    # check = [chr(i) for i in check]
    # print(check)

    # matching

for key, value in result.items():
    for x in value:
        x = int(x)

    if check == value:
        # print('Match found')
        print(key)
        exit(0)
print('No match')