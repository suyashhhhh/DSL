list1 = []
a = int(input("Enter the total no. of students in 1st year: "))
for i in range(1,a+1):
        b = float(input("Enter %ith student 1st year percentage: " %(i)))
        list1.append(b)

def selectionsort(list1):  
        for i in range(0,a-1):
                for j in range(i+1,a):
                        if list1[i]<list1[j]:  
                                (list1[i],list1[j]) = (list1[j],list1[i]) 
        print("\nSorted Data by Selection Sort is:")
        print(list1[::-1]) 

def bubblesort(): 
        for i in range(a-1):
                for j in range(0,a-i-1):
                        if list1[j]>list1[j+1]: 
                                list1[j],list1[j+1] = list1[j+1],list1[j]
        print("\nSorted Data by Bubble Sort is:")
        print(list1)
        print("Top five scores are: ",list1[-5:a],end = ",")

print("\nChoose the method by which you want to sort the data.")
print("1.Selection Sort\n2.Bubble Sort\n3.Quit")
while(1):
        choice = int(input("\nEnter your Choice:"))
        if choice == 1:
                selectionsort(list1)  
        elif choice == 2:
                bubblesort()   
        elif choice == 3:
                quit()
        else:
                print("Invalid Choice")
