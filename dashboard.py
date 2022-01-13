import login
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
        print('are you sure your details are correct, pls create an account and do not stress us')
else:
    done = False
    count=0
    accountbase=[]
    databasefile=open('database.txt','a')
    print('would you like to create an account with us')
    respon=input()
    if(respon=='yes'):
        healthclass.create_health_data()
        print('congratulations i see that you have made an account with us ')
    else:
        print('lose weight you dont want to lose you want to still be fat,better get your life')
        done=True
    count=count+1
    
