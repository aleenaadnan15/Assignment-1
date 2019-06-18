def phone(a):
    number = '('
    counter = 0
    for i in a:
        counter += 1
        number += str(i)
        if counter == 3:
            number += ')'
        elif counter == 6:
            number += '-'
    return number


list = [9,2,3,1,2,3,4,5,6,7]
print(phone(list))   