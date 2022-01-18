import Singup
import login
import healthdashboard

donee = False
while (donee == False):
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
            donee = True
        else:
            print('your log in details are incorrect, please try again')
    elif(respon == 'no'):
        print('would you like to create an account with us?')
        respon=input()
        if(respon=='yes'):
            Singup.create_user()
            print('congratulations youre almost done. Just one more step')
            healthdashboard.healthdata_signup()
            print('congratulations I see that you have made an account with us')
            print('Please proceed to the bmi tab to calculate your bmi')
            donee = True
        else:
            print('okay, goodbye')
            donee=True
    else:
        print('your response is invalid, please input a valid response')
