#print 1 to 10 and break at 5
for i in range(1,11):
    if i==5:
       break
    print(i,end=" ") #1 2 3 4
print(end="\n")


for j in range(1,11):
    if j==5:
        continue
    print(j,end=" ") #1 2 3 4 6 7 8 9 10