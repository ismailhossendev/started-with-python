#  we can assign different data type in List
list1 = ["abc", 34, True, 40, "male"]
print(list1)
#  we can know length of list
print(len(list1))
print(list1[0])

# append or add a item in list it js called array push
list1.append("my name")

print(list1)


#  add item is specified index  this  not remove any item add new on this index
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print("1", thisList)

# remove form list with name
thisList.remove("apple")  # js in pull method and pop
print("2", thisList)

#  remove from specified index
thisList.pop(2)  # this with out index delete last index
del thisList[0]  # is also and call also delete all list
print(3, thisList)
