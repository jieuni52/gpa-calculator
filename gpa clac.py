def convert_score(gpa):
    match gpa:
        case "A+":
            return 4.5
        case "A":
            return 4.0
        case "B+":
            return 3.5
        case "B":
             return 3.0
        case "C+":
             return 2.5
        case "C":
             return 2.0
        case "D+":
             return 1.5
        case "D":
             return 1.0
        case "F":
             return 0.0

archive_credit, submit_credit = 0.0, 0.0
archive_gpa, submit_gpa = 0.0, 0.0

while True:
    print("작업을 선택하세요.")
    print("     1. 입력")
    print("     2. 계산")

    user_value = input()
    value= int(user_value)

    match value:
        case 1:
            user_value = input("학점을 입력하세요: ")
            credit = int(user_value)

            user_value = input("평점을 입력하세요: ")
            gpa = convert_score(user_value)

            if gpa > 0:
                submit_credit += credit
                submit_gpa += credit * gpa
            archive_credit += credit
            archive_gpa += credit * gpa

        case 2:
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit

            print("제출용: " + str(submit_credit) + "학점 (GPA: " + str(submit_gpa) + ")")
            print("열람용: " + str(archive_credit) + "학점 (GPA: " + str(archive_gpa) + ")\n")

            print("프로그램을 종료합니다.")
            break