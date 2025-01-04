#함수 이름은 변경 가능합니다.
students = []
data = {}
##############  menu 1
def Menu1(data) :
    students.append(data) #사전에 학생 정보 저장하는 코딩 

##############  menu 2
def Menu2(ungraded_students) :
    for student in ungraded_students : 
        avg=(student['mid_score']+student['final_score'])/2
        if avg >= 90:
            grade = 'A'
        elif avg>=80:
            grade='B'
        elif avg >= 70:
            grade ='C'
        else :
            grade ='D'
        student['grade'] =grade   #학점 부여 하는 코딩            

##############  menu 3
def Menu3(students) :
    print("-"*40)
    print(f"{'name':<10}{'mid':<10}{'final':<10}{'grade':<10}")
    for student in students:
        print(f"{student['name']:<10}{student['mid_score']:<10}{student['final_score']:<10}{student['grade']:<10}")

    print("-"*40)  #출력 코딩

##############  menu 4
def Menu4(delete_name):
    for student in students:
        if student['name'] == delete_name:
            students.remove(student)
            return
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")


while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        while True:
            try :
                user_input = input('Enter name mid-score final-score : ').split()  #학생 정보 입력받기
                if len(user_input) != 3 :
                        raise ValueError('Num of data is not 3!')   #예외사항 처리-데이터 입력 갯수
                try:
                    mid_score = int(user_input[1])
                    final_score = int(user_input[2])
                except ValueError:
                    raise ValueError('Score is not positive integer!') 
                    continue
                
                data = {
                        'name' : user_input[0],
                        'mid_score' : int(user_input[1]),
                        'final_score' : int(user_input[2])
                    }
                if any( data['name']==student['name'] for student in students) :  #예외사항 처리-이미 존재하는 이름
                    raise ValueError('Alreay given student!')
                if data['mid_score']<0 or data['final_score'] <0:  #예외사항 처리-입력 점수 값이 양의 정수인지
                    raise ValueError('Score is not positive integer!') 
                
            except ValueError as e:
                print(e)
                break
            else :
                Menu1(data) #예외사항이 아닌 입력인 경우 1번 함수 호출 
                break

    elif choice == "2" :
        ungraded_students = [student for student in students if 'grade' not in student]  #예외사항 처리(저장된 학생 정보의 유무)
        if ungraded_students:
            Menu2(ungraded_students) #예외사항이 아닌 경우 2번 함수 호출
            print('Grading to all students')  #"Grading to all students." 출력
        else:   
            print('No student data!')


    elif choice == "3" :
        ungraded_students = [student for student in students if 'grade' not in student]
        try:
            if len(students)==0 :  #예외사항 처리-저장된 학생 정보의 유무
                raise ValueError('No student data!')
            if ungraded_students :   #예외사항 처리-저장되어 있는 학생들의 학점이 모두 부여되어 있는지
                raise ValueError("There is a student who didn't get grade.")
        except ValueError as e:
            print(e) 
        else :
            Menu3(students) #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        try:
            if len(students)==0 :  #예외사항 처리(저장된 학생 정보의 유무)
                raise ValueError('No student data!')
        except ValueError as e:
            print(e)
        else :
            delete_name = input('Enter the name to delete:') #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
            if any(delete_name.strip().lower() == student['name'] for student in students) :
                Menu4(delete_name)  #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
                print(f"{delete_name} student information is deleted.")
            else :
                print('Not exist name!')   #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        
    elif choice == "5" :
        print('Exit Program!') #프로그램 종료 메세지 출력
        break #반복문 종료

    else :
        print('Wrong number. Choose again.')