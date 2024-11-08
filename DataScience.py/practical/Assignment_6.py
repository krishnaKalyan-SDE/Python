# 1.Python function to check whether a number falls within a given range
def fun(n):
    start=int(input("Enter starting no: "))
    end=int(input("Enter ending no: "))
    for i in range(start,end+1):
        if i!=n:
            continue 
        else:
            return 'yes'
    return 'No'

print(fun(int(input("Enter n: "))))



# 2.Write a Python function that takes a list and returns a new
# list with distinct elements from the first list

def fun(list1):
    set1=set(list1)
    list2=list(set1)
    return list2
list1=[1,2,3,3,3,3,4,5]
print(fun(list1))

# 3.Write a Python program to print the even numbers from a given list.
def evenfun(Even):
    for i in Even:
        if i%2!=0:
           Even.remove(i)
    return Even
Even=[3,6,10,11, 2, 13, 4, 15, 6, 17, 18, 29,44]
print(evenfun(Even))

# 4.Write a  Python function that checks whether a passed string is a palindrome or not
def palindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(palindrome(input("Enter string to check palindrome: "))) 


# #output
# PS D:\Python> python -u "d:\Python\DataScience.py\practical\Assignment_6.py"
# Enter n: -4
# Enter starting no: 1
# Enter ending no: 100
# No
# [1, 2, 3, 4, 5]
# [6, 10, 2, 4, 6, 18, 44]
# Enter string to check palindrome: NOON
# True


