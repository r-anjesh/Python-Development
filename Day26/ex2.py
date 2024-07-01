import random

# numbers = [1,2,3,4,57,87,5,3,2,4,56]
# result = [number for number in numbers if number%2 == 0]


# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# student_score = {
#     name:random.randint(80,90)
#     for name in names 
# }

# passed_student = {student:score for (student,score) in student_score.items() if score > 85
# }
# print(passed_student)


# ex 1
# sentence = "You can add or remove names as needed."
# sentence_list = sentence.split(" ")
# sentence_dict = {word:len(word) for word in sentence_list}
# print(sentence_dict)


# ex 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:c * 9/5 + 32 for (day,c) in weather_c.items()}
print(weather_f)