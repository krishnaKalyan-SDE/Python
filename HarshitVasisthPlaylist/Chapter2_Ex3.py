name,char=input("Enter name and char ").split(",")
print("length as input string is:",len(name.strip()))
print(f"count of char in string is {((name.strip()).lower()).count((char.strip()).lower())}")
