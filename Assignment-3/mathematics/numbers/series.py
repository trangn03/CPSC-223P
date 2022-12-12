# Name: Trang Ngo
# Date: 09/28/2022
# File Purpose: Create sum and averange function

def sum(*,list):
    total = 0
    for y in list:
        total = total + y
    return total

def average(*,list):
    total = 0
    for y in list:
        total = total + y
    return total/len(list)
