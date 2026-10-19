student = {}

while True:
    print('\n----Student Manager App----')
    print('1.Add Student')
    print('2.View Students')
    print('3.Check Result')
    print('4.Exit')
    choice = input('Enter ur choice')
    
    if choice == '1':
        name = input('Enter student name : ')
        marks = int(input('Enter marks : '))
        student[name] = marks
        print(f'{name} Successfully Added')
    elif choice == '2':
        if not student:
            print('no student found!')
        else:
            for name, marks in student.items():
                print(name,':', marks)
    elif choice =='3':
        name = input('Enter student name:')
        if name in student:
            marks = student[name]
            
            if marks>=40:
                print('Pass')
            else:
                print('Fail')
        else:
            print('student not found')
    elif choice == '4':
        print('Existing..')
        break
        
    else:
        print('invalid result')