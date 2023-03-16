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


''' The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''
from functools import reduce
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
def findAvrage(query_name):
    # print(student_marks[query_name])
    return reduce(lambda x,y:x+y,student_marks[query_name])/len(student_marks[query_name])
result = findAvrage(query_name)
print(f"{result:.2f}")

