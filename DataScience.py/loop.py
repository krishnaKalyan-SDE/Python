# for i in range(1,101):
#     print(i)

#print no from 20 to 50
# for i in range(20,51):
#     print(i)

#print no from 100 to 1
# for i in range(100,0,-1):
#     print(i)

#Generate odd/even no
# for i in range(1,101):
#     if i%2==0:
#         print(i,)
#     else:
#         print(i,end=" ")

#multiplication table of two
# for i in range(1,11):
#     print(f"2*{i}={2*i}")

#loop with list example
# list=["M3","IE","Python","HoMI","DE","DM","EN"]
# for i in range(0,len(list)):
#     print(f"{i+1}:{list[i]}")


#sum of no from 1 to 100
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("Sum of no from 1 to 100 is ",sum)

# l=['KRISHNA','HARIOM','Ashutosh','Shrikant','Sunil']
# for num in l:
#     print(num)

#print word
# word="Python"
# for i in range(3):
#     print(word*3)

# #count no of characters in python
# word="Pyhton"
# count=0  
# for i in range(0,len(word)):
#     count=count+1
# print(count)

#prime no
n=int(input("Enter n:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"is the prime number")
else:
    print("not a prime number")

   