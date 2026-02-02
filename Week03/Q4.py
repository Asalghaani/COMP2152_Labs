monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")

print(f"Both classes: {monday_class & wednesday_class}")
print(f"Attended either class: {monday_class | wednesday_class}")
print(f"Only Monday: {monday_class - wednesday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}")

all_students = monday_class | wednesday_class
print(f"Is Monday subset of all students: {monday_class <= all_students}")
