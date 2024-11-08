dict1={1:"Businessman",2:"Pilot",3:"Corporate job",4:"Government job",5:"Teacher",6:"Farmer",7:"Principal"}
print(dict1)

#accessing item
print(dict1[1])
print(dict1[2])

#change items
dict1[1]="Politician"
print(dict1)

#Add item
dict1[7]="doctor"
print(dict1)

#update
dict2={8:"Good",9:"Bad",10:"worse"}
dict1.update(dict2)
print(dict1)

#copyb of dict1
dict3=dict1.copy()
print(dict3)

#remove
del dict3[1]
print(dict3)

dict3.pop(2)
print(dict3)

dict3.popitem()
print(dict3)

dict3.clear()
print(dict3)


#nested of dict
student={
   "stud1":{'name':"krishna",'RegNo':'2023BCS101',"subject":["M3","DE","DM"]}
}
print(student)



