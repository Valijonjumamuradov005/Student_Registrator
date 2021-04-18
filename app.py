import random

studentlist = {
    'name':[],
    'age':[],
    'id':[]

}


def reg():
    fullname = input('Enter your full name: ')
    age = int(input('Enter your age: '))
    Id = random.randrange(100, 1000)


    studentlist['name'].append(fullname)
    studentlist['age'].append(age)
    studentlist['id'].append(Id)
    print('Student Royxatdan toliq otdi')


def listid():
    for y in studentlist['name']:
        print(y)
def listidd():
    for x in studentlist['id']:
        print(x)
        

     


def delete():
    lis=input('Student ismini kriting >>   ')
    studentlist['name'].remove(lis)
    print('Student Muofaqiyatl ochirldi')

while 1:
    print("O'zingizga kerakli bo'lgan menuni tanlang:")
    print('1. Registratsiya')
    print("2. O'chirish")
    print("3. Studentlar Royxati")
    print('4. Studentlar id ni korish')
    print('0. Exit')
    func_num = int(input('>>>'))
    if func_num == 1:
        reg()
    elif func_num == 2:
        delete()
    elif func_num == 3:
        listid()
    elif func_num==4:
        listidd()
    elif func_num == 0:
        break




