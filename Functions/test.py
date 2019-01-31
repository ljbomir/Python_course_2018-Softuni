st_grades = {
    'bob': [2, 2],
    'petar': [5, 2, 5],
    'maria': [6, 6, 5, 6],
    'alex': [2, 2]
}

from collections import OrderedDict
#sort = sorted(student_grades.items(), key = lambda x: (len(x[1]), x[0]))
#sort = sorted(student_grades.values(), key=len)
#print(student_grades)
sort_by_key = sorted(st_grades.items(), key = lambda x: (-len(x[1]),x[0]))
print(sort_by_key)
