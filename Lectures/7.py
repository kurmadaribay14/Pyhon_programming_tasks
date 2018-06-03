list1 = []
dict1 = {}
dict1["key1"] = 'value1'

list1.append(dict1)

dict2 = {}
dict2["key2"] = 'value2'

list1.append(dict2)

# Retrieve the Dictionary’s #
listdict1 = list1[0]
listdict2 = list1[1]

print 'This is the first dict' , listdict1
print 'Here is the second dict' , listdict2
