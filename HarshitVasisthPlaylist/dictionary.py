# dictionary={'name':'krishna','age':20,'hobby':'reading'}
# print(dictionary)

# print(dictionary['name'])

# print(dictionary.get('age'))

# dictionary1=dict.fromkeys(['name','age'],'unknown')
# print(dictionary1)

# d2=dict.fromkeys("abc",'unknown')
# print(d2)

# d1={'behaviour':'nice','healthy':'goood'}
# print(d1.get('behaviour'))

# # d1.clear()
# # print(d1)

# d3=d1
# print(d3.popitem())

# d4={'name':'harshit','age':24,'age':34}
# print(d4)
# print(d4['age'])


# n=int(input("Enter n: "))
# def cube_finder(n):
#     dict={}
#     for i in range(1,n+1):
#         dict[i]=i*i*i
#     return dict

# x=cube_finder(n)
# print(x)


# phy=[]
# chem=[]
# math=[]
# for i in range(1,3):
#     phy_marks=int(input("Enter phy marks: "))
#     chem_marks=int(input("Enter chem marks: "))
#     math_marks=int(input("Enter math marks: "))

#     total=phy_marks+chem_marks+math_marks
#     print(f"Total:{total}")

#     avg=total/3
#     print(f"Average:{avg}")

#     phy.append([phy_marks])
#     chem.append([chem_marks])
#     math.append([math_marks])

#     if avg>=90:
#         print("Grade:A")
#     elif avg<=90 and avg>=80:
#         print("Grade:B")
#     else:
#         print("fail")
    

# dict={}

# for i in range(1,3):
#     name=input("Enter name ")
#     age=input("enter age: ")
#     college=input("Enter college: ")
#     dict[i]=name,age,college
    
# print(dict)


# def letter_count(s):
#     count={}

#     for char  in s:
#         count[char]=s.count(char)
#     return count


# x=letter_count("Harekrishna")
# print(x)


name=input("Enter name: ")
age=int(input("Enter age: "))
# fav_movies=[]
# for movie in range(3):
#    fav_movie=input("Enter movies: ")
#    fav_movies.append(fav_movies)
fav_movies=input("Enter fav_movies ").split(",")
dic={}
dic['name']=name
dic['age']=age
dic['fav_movies']=fav_movies
# print(dic)

for key,value in dic.items():
    print(f"{key}:{value}")
