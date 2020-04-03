# Search item's 1st occurrence - index()


mytuple=(1,3,5,7,2,3,1,4,6,7,8,1,2,3,1,)
num = int(input("Enter item to be searched"))
x = mytuple.index(num)

print("First occurrence of the",num,"is at index:",x)


# Count Occurrence of items-count()
#count()>> number of times the item appears in the Tuple

print("Tuple:",mytuple)
n = mytuple.count(3)
print("Total count of 3 in the tuple is:",n)






# Delete tuple (del keyword)

print("Tuple Content:",mytuple)
del mytuple
print("Tuple is deleted")
