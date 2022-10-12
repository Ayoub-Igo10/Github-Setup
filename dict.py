# What is a Dictionary - Data collection type
# How to manage Dictionaries - How to manage the data using Dict
# It works as Key value pair key = value
# Syntax { "name": "Sparta"         }
#           # 0       1
# store student's data - name, course_name, progress, completed_lessons_names
student_1 = {
    "name": "Ayoub",
    "Stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings"]
}                            #     0        1           2
# print(type(student_1))
# print(student_1)
# print(student_1["stream"]) # This will display the value saved inside stream
# # print/display completed_lesson_names
# # print/display completed_lesson_names index 0 means lists

print(student_1)
print(type(student_1))
print(student_1["name"])
print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])




