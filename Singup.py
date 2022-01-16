import Userclass
users=[]
def create_user():
    print("hello user, what is your name")
    name = input()
    print("hello user, select a username")
    username = input()
    print("hello user, choose a password")
    password = input()
    print("hello user, input your age")
    age = input()
    print("hello user, input your height")
    height= input()
    print('hello user, input your weight')
    weight=input()
    
    newuser = Userclass.User(name,username,password,age,height,weight)
    users.append(newuser)
    append_to_databse(newuser)
    append_all_info(newuser)
    return newuser

def append_to_databse(object):
    write=open('username_password_database.txt','a')
    write.write(object.username)
    write.write('\n')
    write.write(object.password)
    write.write('\n')
    write.close()

def append_all_info(object):
    write=open('user_database.txt','a')
    write.write('Newuser \n')
    write.write(object.name)
    write.write('\n')
    write.write(object.username)
    write.write('\n')
    write.write(object.password)
    write.write('\n')
    write.write(object.age)
    write.write('\n')
    write.write(object.height)
    write.write('\n')
    write.write(object.weight)
    write.write('\n')
    write.close()


