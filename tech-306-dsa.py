class Patient:
    def __init__(self, id):
        self.id = id
        self.next = None

front = None
rear = None

def add_patient(id):
    global front, rear
    new_patient = Patient(id)
    if front is None:
        front = rear = new_patient
        rear.next = front
    else:
        rear.next = new_patient
        rear = new_patient
        rear.next = front

def delete_patient(id):
    global front, rear
    if front is None:
        print("Queue is empty.")
        return
    
    temp = front
    prev = rear
    while True:
        if temp.id == id:
            if temp == front:
                if front == rear:
                    front = rear = None
                else:
                    prev.next = front.next
                    front = front.next
                    rear.next = front
            else:
                prev.next = temp.next
                if temp == rear:
                    rear = prev
            print(f"Deleted patient with ID: {id}")
            return
        
        prev = temp
        temp = temp.next
        if temp == front:
            break
    print(f"Patient with ID {id} not found.")

def print_list(start_id):
    global front
    if front is None:
        print("Queue is empty.")
        return
    
    temp = front
    found = False
    while True:
        if temp.id == start_id:
            found = True
            break
        temp = temp.next
        if temp == front:
            break
            
    if not found:
        print(f"Patient with ID {start_id} not found.")
        return
    
    start_node = temp
    print(f"Current patient list starting from ID {start_id}:", end=" ")
    while True:
        print(temp.id, end=" ")
        temp = temp.next
        if temp == start_node:
            break
    print()

def main():
    n = int(input("Enter the number of patients: "))
    for _ in range(n):
        id = int(input("Enter patient ID: "))
        add_patient(id)
        
    while True:
        operation = input("Enter operation (Add, Delete, Print, Exit): ")
        if operation == "Add":
            id = int(input("Enter patient ID to add: "))
            add_patient(id)
        elif operation == "Delete":
            id = int(input("Enter patient ID to delete: "))
            delete_patient(id)
        elif operation == "Print":
            id = int(input("Start from patient ID: "))
            print_list(id)
        elif operation == "Exit":
            break
        else:
            print("Invalid operation!")

if __name__ == "__main__":
    main()
