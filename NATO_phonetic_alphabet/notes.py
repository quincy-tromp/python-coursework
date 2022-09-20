# List comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)
range_list = [num * 2 for num in range(1, 5)]
print(range_list)
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in students if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in students if len(name) > 5]
print(long_names)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
result = [num for num in numbers if num % 2 == 0]
print(result)
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
result = [int(x) for x in file_1_data if x in file_2_data]
print(result)

# Dictionary comprehension
#   new_dict = {new_key:new_value for item in list}
#   new_dict = {new_key:new_value for (key,value) in dict.items()}
import random
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student:random.randint(1, 100) for student in students}
print(student_score)
passed_students = {student:score for (student,score) in student_score.items() if score >= 60}
print(passed_students)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for (word) in sentence.split()}
print(result)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c * 9/5 + 32) for (day, temp_c) in weather_c.items()}

# Iterate over a Pandas DataFrame
import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
student_df = pd.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    print(row.score)