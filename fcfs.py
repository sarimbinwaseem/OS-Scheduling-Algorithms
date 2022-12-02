from processes import Process
import pprint 
processes = []

howmany = int(input("Enter how many processes: "))

for i in range(howmany):
    arrival = int(input("Enter arrival time: "))
    burst = int(input("Enter burst time: "))
    print()
    processes.append(Process(i, arrival, burst))


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

pprint.pprint(processes)