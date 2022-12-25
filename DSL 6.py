def entries(a):
    n=int(input("Enter number of students: "))
    for i in range(n):
        m=float(input("Enter percentage of student: "))
        a.append(m)
    print("Array Entries are Recorded\n")
def display(a):
    n=len(a)
    if n==0:
        print("No records entered\n")
    else:
        print("Array of percentage:  ",end='  ')
        for i in range(len(a)):
            print(a[i],end='  ')
    print("")
def partition(a,f,l):
    pivot=a[f]
    left=f+1
    right=l
    while True:
        while left<=right and a[left]<=pivot:
            left=left+1
        while left<=right and a[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            a[left],a[right]=a[right],a[left]
    a[f],a[right]=a[right],a[f]
    return right
def quick_sort(a,f,l):
    if f<l:
        p=partition(a,f,l)
        quick_sort(a,f,p-1)
        quick_sort(a,p+1,l)
a=[]
entries(a)
while True:
    print("1. Display array of FE percentage.")
    print("2. sort by quicksort")
    print("3. Exit.")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print("")
        display(a)
        print("")
    elif ch==2:
        print("\nPercentage before sorting")
        display(a)
        print("\nPercentage after sorting")
        n=len(a)
        quick_sort(a,0,n-1)
        display(a)
        if n>=5:
            print("\n------------Top five scores----------")
            top=a[::-1]
            print(top[:5:])
            print("")
        else:
            print("\n----------Top scores-----------")
            top=a[::-1]
            print(top[:5:])
            print("")
    elif ch==3:
        print("Program Finished!!")
        quit()
    else:
        print("Invalid choice,Try again.")
