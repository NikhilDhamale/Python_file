name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))

percentage = (maths + python + sql) / 3
is_passed = percentage >= 40

print("\n Result ")
print("Student:", name)
print("Maths:", maths)
print("Python:", python)
print("SQL:", sql)
print("Percentage:", percentage)
print("Passed:", is_passed)

print("\nData Types:")
print(type(name))
print(type(maths))
print(type(percentage))
print(type(is_passed))