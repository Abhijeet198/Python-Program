# Search item


myset= {"C","C++","Java","Python","50","L#@12","@@@@","1","A","a"}

search = input("Enter item to be searched:")
if search in myset:
  print("Yes",search,"is in the set")
else:
  print("No",search,"is not in the set.")
