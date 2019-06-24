StudentsData=[]

def GetStudentValue(value):
    index = 0
    for name in StudentsData:
        if name['Name'].lower() == value.lower():
            return index
        index += 1

while True:
    print('\n..............Press 1 to add new Student\'s data..............')
    print('..............Press 2 to delete Student\'s data..............')
    print('..............Press 3 to Search Student\'s data..............')
    print('..............Press 4 to Edit Student\'s data..............')
    print('..............Press 5 to Show All Students data..............')
    print('..............Press 6 to Exit..............')

    value = input("\n What do you want to do? ")

    if value == '1':
        Student={}
        Student['Name']=input("Enter Student's Name ")
        Student['F_Name'] = input("Enter Father Name ")
        Student['Age'] = input("Enter Student's Age ")
        Student['ContactNo'] = input("Enter Student's Contact Number ")
        StudentsData.append(Student)

    elif value == '2':
        SName = input('Enter Student\'s Name ')
        DeleteValue =GetStudentValue(SName)
        del StudentsData[DeleteValue]
        input('Press any Key to Continue...')

    elif value == '3':
        SName = input('Enter Student\'s Name ')
        SearchValue =GetStudentValue(SName)
        print('\n'+"\n".join("{}: {}".format(k, v) for k, v in StudentsData[SearchValue].items())+'\n')
        input('Press any Key to Continue...')

    elif value == '4':
        SName = input('Enter Student\'s Name ')
        ValueForUpdate = GetStudentValue(SName)
        print('\n' + "\n".join("{}: {}".format(k, v) for k, v in StudentsData[ValueForUpdate].items()) + '\n')
        while True:
            Key = input('Enter Key ')
            value = input('Enter Value ')
            for keySearch in StudentsData[ValueForUpdate].keys():
                if keySearch == Key:
                    StudentsData[ValueForUpdate][keySearch] = value
            print('\n' + "\n".join("{}: {}".format(k, v) for k, v in StudentsData[ValueForUpdate].items()) + '\n')
            check=input('Do you want to Update more? Y/N ')
            if check=='N' or 'n':
                break
    elif value == '5':
        print(StudentsData)
        input('Press any Key to Continue...')
    elif value == '6':
        break