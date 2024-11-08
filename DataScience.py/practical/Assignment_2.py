# # practical-2
# Basic data type to create a program that takes input and performs string 


user_input = input("Enter a string: ")
print("String Operations:")
print(f"Original String: {user_input}")
print(f"Uppercase: {user_input.upper()}")
print(f"Lowercase: {user_input.lower()}")
print(f"Title Case: {user_input.title()}")
print(f"String Length: {len(user_input)}")
print(f"Reversed String: {user_input[::-1]}")
print(f"Does the string start with 'a'? : {user_input.startswith('a')}")
print(f"Does the string end with 'z'? : {user_input.endswith('z')}")
print(f"Count of 'e' in the string: {user_input.count('e')}")
print(f"String with spaces removed: {user_input.strip()}")



# # output
# Enter a string: Krishna
# String Operations:
# Original String: Krishna
# Uppercase: KRISHNA
# Lowercase: krishna
# Title Case: Krishna
# String Length: 7
# Reversed String: anhsirK
# Does the string start with 'a'? : False
# Does the string end with 'z'? : False
# Count of 'e' in the string: 0
# String with spaces removed: Krishna