class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.prev = None
        self.next = None

head = None
tail = None

def insertBook(id, title):
    global head, tail
    newBook = Book(id, title)
    newBook.prev = tail
    if tail:
        tail.next = newBook
    else:
        head = newBook
    tail = newBook

def deleteBook(id):
    global head, tail
    temp = head
    while temp and temp.id != id:
        temp = temp.next
    if not temp:  # Book not found
        return
    if temp.prev:
        temp.prev.next = temp.next
    if temp.next:
        temp.next.prev = temp.prev
    if temp == head:
        head = temp.next
    if temp == tail:
        tail = temp.prev

def displayForward():
    temp = head
    while temp:
        print(f'{temp.id} "{temp.title}"', end=' ')
        if temp.next:
            print("->", end=' ')
        temp = temp.next
    print()

# Demo
print("Book list forward:")
insertBook(101, "Python Programming")
insertBook(102, "Data Structures")
insertBook(103, "Algorithms")
insertBook(104, "Operating Systems")
displayForward()

print("After insertion:")
insertBook(105, "Machine Learning")
displayForward()

print("After deletion:")
deleteBook(102)
displayForward()
