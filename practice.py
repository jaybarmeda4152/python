""" Count line from the file - START"""
# def countLines(fileName):
#     file = open(fileName,'r+')
#     count = 0
#     for line in file:
#         # print(count , line,end="")
#         count += 1
    
#     file.write("\n\n Total line in this file is "+str(count)+".")
#     file.close()
#     return count

# print("Total lines in your files is",countLines("D:/Jay/Basic_constiction_site_template.txt"),end=".")

""" Count line from the file - END"""

""" print max mutations but not have sum of all given input , equal to n- START"""
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# ansList = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 ansList.append([i,j,k])
# atli lambi loop lakhva karta ek j line lakhvanu and aane ek list ma store kari sakay
"""
ansList = [[i,j,k] for i in range(x+1) for j in range(j+1) for k in range(k+1) if i+j+k != N]
print(ansList)
print(ansList)
"""

""" print max mutations but not have sum of all given input , equal to n- END"""

""" Find the runnerUp number - START"""
# n = int(input())
# ans = list(map(int,input().split()))
# print(sorted(ans, reverse=True)[1]) # sort the list and get the 1 index number which will be runner up.
""" Find the runnerUp number - END"""

""" Find the lowest mark of given input - START"""
# students = []
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
# mn = min(students, key=lambda x: x[1])
# nonlowest = sorted([student for student in students if student[1] > mn[1]], key= lambda x: x[1])
# seconds = sorted([student[0] for student in nonlowest if student[1] == nonlowest[0][1]])
# for student in seconds:
#         print(student)
# print(a(students))
# nonlowest = sorted([student for student in students if student[1] > mn[1]], key= lambda x: x[1])
# print(min(students, key= lambda x:x[1])) 

"""Find the lowest mark of given input - END"""