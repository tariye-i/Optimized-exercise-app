Login=False

def attempt_login(username,password):
    trying=open('username_password_database.txt','r')
    username=username+'\n'
    password=password+'\n'
    done=False
    while(not done):
        line=trying.readline()
        if line==username:
            database_password= trying.readline()
            if(database_password==password):
                print('Welcome user login succesfull')
                Login=True
                done=True
                return True
            else:
                print('Username or password, is incorrect')
                done=True
                return False
        if(line==''):
            print('Sorry, username is not present in our database')
            done=True
            return False

