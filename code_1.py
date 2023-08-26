class FlightProcess:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def p_id(self, process):
        return int(process.p_id[1:])

    def start_time(self, process):
        return process.start_time

    def priority(self, process):
        priority_order = {'Low': 0, 'MID': 1, 'High': 2}
        return priority_order[process.priority]

    def display_table(self):
        print("P_ID\tProcess\t\tStart Time\tPriority")
        print("----------------------------------------")
        for process in self.processes:
            print(f"{process.p_id}\t{process.process}\t\t{process.start_time}\t\t{process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(FlightProcess("P1", "VSCode", 100, "MID"))
    flight_table.add_process(FlightProcess("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(FlightProcess("P93", "Chrome", 189, "High"))
    flight_table.add_process(FlightProcess("P42", "JDK", 9, "High"))
    flight_table.add_process(FlightProcess("P9", "CMD", 7, "High"))
    flight_table.add_process(FlightProcess("P87", "NotePad", 23, "Low"))

    while True:
        print("\nSorting Options:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            break
        
        sorting_key = None
        if choice == 1:
            sorting_key = flight_table.p_id
        elif choice == 2:
            sorting_key = flight_table.start_time
        elif choice == 3:
            sorting_key = flight_table.priority
        
        flight_table.processes.sort(key=sorting_key)
        flight_table.display_table()

if __name__ == "__main__":
    main()
