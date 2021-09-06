# ‘NoneType’ object is not iterable

# Problem

def filter_students(class_names):
  new_class_names = []
  for c in class_names:
    if c.startswith("E"):
      new_class_names.append(c)

def show_students(class_names):
  for c in class_names:
    print(c)

students = ["Elena", "Peter", "Chad", "Sam"]
students_e_name = filter_students(students)

show_students(students_e_name)

# Solution

def filter_students(class_names):
  new_class_names = []
  for c in class_names:
    if c.startswith("E"):
      new_class_names.append(c)
    return new_class_names

def show_students(class_names):
	for c in class_names:
		print(c)

students = ["Elena", "Peter", "Chad", "Sam"]
students_e_name = filter_students(students)

show_students(students_e_name)