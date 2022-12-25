print("Matrix Size :")
r=int(input("Enter Number of Rows : "))
c=int(input("Enter Number of Columns  : "))
print("\nMatrix 1 Elements")
m1=[]
for i in range (r):
  a=[]
  for j in range (c):
    a.append(int(input("Enter Elements : ")))
  m1.append(a)
for i in range(r):
  for j in range (c):
    print(m1[i][j],end=" ")
  print()
print("\nMatrix 2 Elements")
m2=[]
for i in range (r):
  a=[]
  for j in range (c):
    a.append(int(input("Enter Elements : ")))
  m2.append(a)
for i in range(r):
  for j in range (c):
    print(m2[i][j],end=" ")
  print()

print("\nNew Matrix showing Addition of M1 and M2")
add=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m1[0])):
       add[i][j] = m1[i][j] + m2[i][j]
for k in add:
   print(k)

print("\nNew Matrix showing Subtracting of M1 and M2")
sub=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m1[0])):
       sub[i][j] = m1[i][j] - m2[i][j]
for k in sub:
   print(k) 

print("\nNew Matrix showing Multiplication of M1 and M2")
mul=[[0 for i in range(c) ] for j in range(r) ]
for i in range(len(m1)):
   for j in range(len(m2[0])):
     for k in range(len(m2)):
       mul[i][j] += m1[i][k] * m2[k][j]
for k in mul:
   print(k)

print("\nNew Matrix showing Transpose of M1")
trans1=[[0 for i in range (c)]for j in range (r)]
for i in range (len(m1)):
  for j in range (len(m1[0])):
    trans1[j][i]=m1[i][j]
for k in trans1:
  print(k)

print("\nNew Matrix showing Transpose of M2")
trans2=[[0 for i in range (c)]for j in range (r)]
for i in range (len(m2)):
  for j in range (len(m2[0])):
    trans2[i][j]=m2[j][i]
for k in trans2:
  print(k)
