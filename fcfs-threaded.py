from processes import Process
import pprint, threading
processes = []

howmany = int(input("Enter how many processes: "))

totalProcesses = []

for i in range(howmany):
    # arrival = int(input("Enter arrival time: "))
    burst = int(input("Enter burst time: "))
    print()
    processes.append(Process(i, 0, burst))

def doitnow(processes) -> None:
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

    print()
    # pprint.pprint([proc for proc in processes])
    
    totalProcesses.extend(processes)

t1 = threading.Thread(target = doitnow, args=(processes[:5],))
t2 = threading.Thread(target = doitnow, args=(processes[5:],))

t1.start()
t2.start()

t1.join()
t2.join()
print()
pprint.pprint(totalProcesses)
print()
avgWaiting = sum(proc.WT for proc in totalProcesses)
print("Average Waiting Time:", avgWaiting/len(totalProcesses))