from database import DatabaseManager

# Define sample data
students_data = [
    {"student_id": 1, "name": "Alice", "surname": "Smith", "age": 20},
    {"student_id": 2, "name": "Bob", "surname": "Johnson", "age": 22},
    {"student_id": 3, "name": "Charlie", "surname": "Brown", "age": 21}
]

advisors_data = [
    {"advisor_id": 101, "name": "David", "surname": "Miller", "age": 35},
    {"advisor_id": 102, "name": "Eve", "surname": "Garcia", "age": 40},
    {"advisor_id": 103, "name": "Frank", "surname": "Lee", "age": 38}
]

student_advisor_data = [
    {"student_id": 1, "advisor_id": 101},
    {"student_id": 2, "advisor_id": 102},
    {"student_id": 3, "advisor_id": 101}
]

# Initialize DatabaseManager
db_manager = DatabaseManager()

# Insert sample data into MongoDB collections
for student in students_data:
    db_manager.add_data("students", **student)

for advisor in advisors_data:
    db_manager.add_data("advisors", **advisor)

for relation in student_advisor_data:
    db_manager.add_data("student_advisor", **relation)

print("Sample data inserted successfully.")


order_by = 1  # 1 for ascending order, -1 for descending order
result_advisors = db_manager.list_advisors_with_students_count(order_by)
print("Advisors with students count:")
for advisor in result_advisors:
    print(advisor)

# Test list_students_with_advisors_count method
order_by = 1  # 1 for ascending order, -1 for descending order
result_students = db_manager.list_students_with_advisors_count(order_by)
print("Students with advisors count:")
for student in result_students:
    print(student)