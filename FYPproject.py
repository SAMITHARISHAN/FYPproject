import csv
Totalmomentum = 0
Totaltime = 0 
with open('Book1.csv', 'r') as csv_files:
    csv_reader = csv.reader(csv_files)

    next(csv_reader)
    
    
    momentum = 0
    for line in csv_reader:
        # momentum = float(line[0])*float(line[1])
        Totalmomentum += float(line[0])*float(line[1])
    
    
    print(Totalmomentum)
digits = 0
newTotalmomentum = Totalmomentum
while(Totalmomentum != 0):
        Totalmomentum = Totalmomentum//10
        digits = digits + 1
print(newTotalmomentum/pow(10,digits))

with open('Book2.csv', 'r') as csv_files:
    csv_reader = csv.reader(csv_files)

    next(csv_reader)
    
    
    for line in csv_reader:
        # momentum = float(line[0])*float(line[1])
        Totaltime += float(line[0])
    print(Totaltime)

digitTime = 0
newTotaltime = Totaltime
while(Totaltime != 0):
        Totaltime = Totaltime//10
        digitTime = digitTime + 1
print(newTotaltime/pow(10,digitTime))


statevalue = (newTotalmomentum/pow(10,digits)*newTotaltime/pow(10,digitTime))
print(statevalue)


  

