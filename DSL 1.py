C=[]
B=[]
F=[]

a=int(input("Enter the number of students who play Cricket : "))
for i in range(a):
    b=input("Name(s) of students who play Cricket : ")
    C.append(b)
print("Students who play Cricket are : ",C)

b=int(input("Enter the number of students who play Badminton : "))
for i in range(b):
    c=input("Name(s) of students who play Badminton : ")
    B.append(c)
print("Students who play Badminton are : ",B)

c=int(input("Enter the number of students who play Football : "))
for i in range(c):
    d=input("Name(s) of students who play Football : ")
    F.append(d)
print("Students who play Football are : ",F)

def CxB():
    CnB=[]
    for x in C:
        for y in B:
            if x==y:
                CnB.append(x)
    print("Students who play both Cricket and Badminton are : ",CnB)

def CorB():
    CoB=[]
    for x in C:
        if x not in B:
            CoB.append(x)

    for y in B:
        if y not in C:
            CoB.append(y)

    print("Students who play either Cricket or Badminton are : ",CoB)

def FnCB():
    OF=[]
    for x in F:
        if x not in C:
            if x not in B:
                OF.append(x)
    print("Students who play Only Football but niether Cricket nor Badminton are : ",OF)
    print("Number of Students who play Only Football but niether Cricket nor Badminton",len(OF))

def CxFnB():
    CxF=[]
    for i in C:
        for j in F:
            if i==j:
                if i not in B:
                    CxF.append(i)
    print("Students who play Cricket and Football both but not Badminton are : ",CxF)
    print("Number of Students who play Cricket and Football both but not Badminton is : ",len(CxF))

print(" 1.Name(s) of Students who play both Cricket and Badminton \n 2.Name(s) of Students who play either Cricket or Badminton \n 3.Number of Students who play Only Football but niether Cricket nor Badminton \n 4.Number of Students who play Cricket and Football both but not Badminton")

while(1):
    z=int(input("Enter your choice : "))
    if z==1:
        CxB()
    elif z==2:
        CorB()
    elif z==3:
        FnCB()
    elif z==4:
        CxFnB()
    else :
        print("Wrong Option !!")
