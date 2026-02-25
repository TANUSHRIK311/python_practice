# TECH-303-DSA-TIME & SPACE COMPLEXITY
# -----------------------------
# Garden Plant Management
# -----------------------------

class Node:
def init(self, data):
self.data = data
self.next = None


head = None


# Insert at beginning (used to reverse list)
def insert_first(n):
global head
new_node = Node(n)
new_node.next = head
head = new_node


# Display list
def display():
global head
temp = head
while temp:
print(temp.data, end=' ')
temp = temp.next
print()


# Swap two nodes (without swapping data)
def swap_nodes(a, b):
global head

if a == b:
return

prevA = prevB = None
currA = currB = head

# Find node A
while currA and currA.data != a:
prevA = currA
currA = currA.next

# Find node B
while currB and currB.data != b:
prevB = currB
currB = currB.next

# If either not found
if not currA or not currB:
print("One of the elements not found!")
return

# Update previous pointers
if prevA:
prevA.next = currB
else:
head = currB

if prevB:
prevB.next = currA
else:
head = currA

# Swap next pointers
currA.next, currB.next = currB.next, currA.next


# -----------------------------
# Main Program
# -----------------------------

n = int(input())
plant_ids = list(map(int, input().split()))

# Reverse list using insert_first
for pid in plant_ids:
insert_first(pid)

print("List of plant IDs after reversal:")
display()

a, b = map(int, input().split())

swap_nodes(a, b)

print(f"List of plant IDs after swapping {a} and {b}:")
display()