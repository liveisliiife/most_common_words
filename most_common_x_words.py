import os
my_dict = dict()
name = input("Enter filename:")
if not os.path.isfile(name):
    print("File not found")
    exit()

file = open(name)
x = int(input("How many words would you like me to find the most common words? "))
for line in file:
    words = line.split()
    for word in words:
        my_dict[word] = my_dict.get(word,0) +1

lst = []
for k,v in my_dict.items():
    temp = (v,k)
    lst.append(temp)

lst = sorted(lst,reverse=True)

# most common x words
for val,key in lst[:x]:
    print(key,val)

file.close()