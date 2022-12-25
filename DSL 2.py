a = input("Enter the string: ")
list1 = a.split()
m = 0
word = 0

for i in range(len(list1)):
    if m < len(list1[i]):
        m = len(list1[i])
        word = i
print("\nThe word with longest length is ",list1[word])

b = input("\nEnter the character of frequency you want: ")
print("\nCharacter",b,"comes in",a,a.count(b),"times")

if a == a[::-1]:
    print("\n",a,"is palindrome")
else:
    print("\n",a,"is not palindrome")

c = input("\nEnter the substring you want to find/search: ")
if c in a:
    print("\n",c,"is present in",a,"at position",a.index(c))
else:
    print("\n",c,"is not present in",a)

list2 = set(list1)
list3 = list(list2)
list4 =[]
list5 = []
n = 0
for i in range(len(list3)):
    n = 0
    for j in range (len(list1)):
        if (list3[i] == list1[j]):
            n += 1
    list4 = list3[i], n
    list5.append(list4)
print("\nOccurrence of each word in a given string")
print(list5)
