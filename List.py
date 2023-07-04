ToDoLst = []  # Create an empty list.
ToDoLst2 = ["Buy Maurice a Tea", "Study Essentials", "Buy da wife some flowers", "Write Python Program"]
OtherLst = [1, 3, 5, 46, 143, 6, 8]
'''
print(ToDoLst2)
print()
JobNum = 1
for Job in ToDoLst2:
    print(f"  {JobNum}. {Job}")
    JobNum += 1
print()
NewItem = input("Enter the new job for the ToDo list: ")
ToDoLst2.append(NewItem)
JobNum = 1
for Job in ToDoLst2:
    print(f"  {JobNum}. {Job}")
    JobNum += 1
print()
ToDoLst2.pop()  # Remove the last item from the list.
JobNum = 1
for Job in ToDoLst2:
    print(f"  {JobNum}. {Job}")
    JobNum += 1
print()
DelItem = int(input("Enter the list item to delete: "))
ToDoLst2.__delitem__(DelItem-1)
JobNum = 1
for Job in ToDoLst2:
    print(f"  {JobNum}. {Job}")
    JobNum += 1
print()

NumberLst = []
while True:
    Number = int(input("Enter a number (-1 to end): "))
    if Number == -1:
        break
    NumberLst.append(Number)
print(NumberLst)
'''
ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
while True:
    Prov = input("Enter the province (LL): ").upper()
    if Prov == "":
        print("Error - Province cannot be blank.")
    elif len(Prov) != 2:
        print("Error - Province must be 2 letters only.")
    elif Prov not in ProvLst:
        print("Error - not a valid province.")
    else:
        break
MarStatLst = ["S", "M", "W", "D", "O"]
while True:
    MarStat = input("Enter the marital status (S, M, W, D or O): ").upper()
    if MarStat == "":
        print("Error - Marital Status cannot be blank.")
    elif len(MarStat) != 1:
        print("Error - Marital Status must be 1 letter only.")
    elif MarStat not in MarStatLst:
        print("Error - not a valid marital status.")
    else:
        break
