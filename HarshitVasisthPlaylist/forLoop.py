# user_input=input("Enter your name: ") #Hare Krishna
# count=0
# # if user_input>='a' and user_input<='z':
# for i in range(0,len(user_input)):
#       for j in range(0,len(user_input)):
#         if user_input[i]==user_input[j] and i!=j:
#             count=count+1
#       print(user_input[i],count
# 

# print(user_input.count('a'))


# temp=""
# for i in range(len(user_input)):
#     if user_input[i] not in temp:
#         print(f"{user_input[i]}:{user_input.count(user_input[i])}")
#         temp=temp+user_input[i]


user=input("Enter no:")
count=0
for i in range(len(user)):
    count=count+int(user[i])
print(count)    





