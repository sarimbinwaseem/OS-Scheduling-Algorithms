from processes import Process
import pprint 
import operator
from tabulate import tabulate


processes = []

howmany = int(input("Enter how many processes: "))

for i in range(howmany):
    arrival = int(input("Enter arrival time: "))
    burst = int(input("Enter burst time: "))
    print()
    processes.append(Process(i, arrival, burst))

# pprint.pprint(processes)
print()

###### SORTING ######## make sorting as we do in copy.
processes = sorted(processes)

pprint.pprint(processes)
print()
first = True
previousCT = 0

for proc in processes:
    if first:
        proc.CT = proc.burstTime
        first = False
        previousCT = proc.CT
    else:
        proc.CT = previousCT = previousCT + proc.burstTime

    proc.TAT = proc.CT - proc.arrivalTime
    proc.WT = proc.TAT - proc.burstTime

# pprint.pprint(processes)

columns = ["PID", "Arrival Time", "Burst Time", "TAT", "Completion Time", "Wating Time"]

data = [proc for proc in processes]

print(tabulate(data, headers=columns, tablefmt="pretty"))