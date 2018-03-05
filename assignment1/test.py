THIS FILE IS NOT FOR GRADING
JUST FOR MY LEARNING PROGRESS RECORDING
THANK YOU!!

# import sys
# print("argv are:")

# for i in sys.argv:
#     print(i)
#     print(type(i))

# newDrone = input("Enter New Cooridnate[x, y, z]:")
# newLocString = newDrone.split(',')
# qwe = int(newLocString)
# print(qwe)


# def stringToIntList(newDrone):
#     new_loc_string_list = newDrone.split(',')

#     x = int(new_loc_string_list[0])
#     y = int(new_loc_string_list[1])
#     z = int(new_loc_string_list[2])
#     print([x, y, z])
#     return [x, y, z]

# stringToIntList("1,2,5")

# dic = {0:"213", 1: "3453",2:"1233"}

# i = 1
# while i < len(dic):
#     print(dic[i])
#     i+=1

import re

print(re.match("[0-9]+,[0-9]+,[0-9]+","0,0,0") == None)
print(re.match("[0-9]+,[0-9]+,[0-9]+","123") == None)
print(re.match("[0-9]+,[0-9]+,[0-9]+","e,w,q") == None)