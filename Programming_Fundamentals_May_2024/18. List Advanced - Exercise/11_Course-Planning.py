def add_course(course_name, schedule):
    if course_name not in schedule:
        schedule.append(course_name)


def insert_course(course_name, index, schedule):
    if course_name not in schedule:
        schedule.insert(index, course_name)


def remove_course(course_name, schedule):
    if course_name in schedule:
        schedule.remove(course_name)
        exercise_title = course_name + "-Exercise"
        if exercise_title in schedule:
            schedule.remove(exercise_title)


def swap_courses(course_one, course_two, schedule):
    if course_one in schedule and course_two in schedule:
        index_one, index_two = schedule.index(course_one), schedule.index(course_two)
        schedule[index_one], schedule[index_two] = schedule[index_two], schedule[index_one]

        exercise_one, exercise_two = course_one + "-Exercise", course_two + "-Exercise"
        if exercise_one in schedule:
            schedule.remove(exercise_one)
            schedule.insert(schedule.index(course_one) + 1, exercise_one)
        if exercise_two in schedule:
            schedule.remove(exercise_two)
            schedule.insert(schedule.index(course_two) + 1, exercise_two)


def add_exercise(course, schedule):
    exercise_name = course + "-Exercise"
    if course in schedule:
        if exercise_name not in schedule:
            schedule.insert(schedule.index(course) + 1, exercise_name)
    else:
        schedule.append(course)
        schedule.append(exercise_name)


def process_commands(schedule, commands):
    for cmd in commands:
        parts = cmd.split(":")
        action = parts[0]

        if action == "Add":
            course_name = parts[1]
            add_course(course_name, schedule)

        elif action == "Insert":
            course_name = parts[1]
            index = int(parts[2])
            insert_course(course_name, index, schedule)

        elif action == "Remove":
            course_name = parts[1]
            remove_course(course_name, schedule)

        elif action == "Swap":
            course_one = parts[1]
            course_two = parts[2]
            swap_courses(course_one, course_two, schedule)

        elif action == "Exercise":
            course_name = parts[1]
            add_exercise(course_name, schedule)


initial_schedule = input().split(", ")
command_list = []

while True:
    command = input()
    if command == "course start":
        break
    command_list.append(command)

process_commands(initial_schedule, command_list)
for i in range(len(initial_schedule)):
    initial_schedule[i] = f"{i + 1}.{initial_schedule[i]}"

print("\n".join(initial_schedule))


