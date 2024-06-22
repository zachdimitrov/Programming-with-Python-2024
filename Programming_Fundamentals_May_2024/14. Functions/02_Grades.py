grade_num = float(input())


def print_grade(grd):
    if 2 <= grd < 3:
        return "Fail"
    elif 3 <= grd < 3.5:
        return "Poor"
    elif 3.5 <= grd < 4.5:
        return "Good"
    elif 4.5 <= grd < 5.5:
        return "Very Good"
    elif 5.5 <= grd <= 6:
        return "Excellent"


print(print_grade(grade_num))
