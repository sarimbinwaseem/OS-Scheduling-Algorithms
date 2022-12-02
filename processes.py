from dataclasses import dataclass

@dataclass(slots = True)
class Process:
    # priority: int
    pid: str
    arrivalTime: int
    burstTime: int
    CT: int = None
    TAT: int = None
    WT: int = None
    

    def __add__(self, other):
        return self.burstTime + other.burstTime

    def __lt__(self, other):
        return self.burstTime < other.burstTime

    def __gt__(self, other):
        return self.burstTime > other.burstTime

    def __repr__(self) -> str:
        return f""" 
        PID: {self.pid}
        Burst Time: {self.burstTime}
        Arrival Time: {self.arrivalTime}
        Completion Time: {self.CT}
        Wating Time: {self.WT}
        Turn Around Time: {self.TAT}       
        """