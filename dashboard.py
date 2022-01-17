import usersignup
import login
import minisignup
print('hello user welcome to optimized excercise app')
print('Do you have an account with us? pls login, or sign up to create an account')
respon= input()
if(respon =='yes'):
    print('That is very nice user, pls what is your username')
    username=input()
    print('what is the password given to this specific username')
    password=input()
    verification= login.logins(username,password)
    if(verification==True):
        print('you may now proceed to dashboard')
    else:
        
        print('are you sure your details are correct,type yes to create one')
else:
    done = False
    count=0
    accountbase=[]
    databasefile=open('database.txt','a')
    print('would you like to create an account with us')
    respon=input()
    if(respon=='yes'):
        usersignup.classer()
        print('congratulations i see that you have made an account with us ')
        minisignup.create_user()
    else:
        print('okay then')
        done=True
