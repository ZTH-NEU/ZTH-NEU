import csv

with open('checkpoints/result.csv', 'r') as f:
    reader = csv.reader(f)
    sum_ = 0
    dett_ = float(0.5)
    dog = 0
    cat = 0
    for row in reader:
        if len(row) and row[1] != 'label':
            sum_ += 1
            row[1] = float(row[1])
            if row[1] > dett_:
                dog += 1
            else:
                cat += 1
    print(sum_, dog, cat)
