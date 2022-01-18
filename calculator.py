
import tkinter

root = tkinter.Tk()
root.title("calculator")
 
#weight - goal weight = X
#x*7700 = total amount of calories to be lost


def calculate_exercise():
    goal = float(entry_goal.get())
    current = float(entry_current.get())
    exercise = round( current - goal )
    ans = exercise * 7700
    label_result['text'] = f"total weight to be lost: {exercise}kg"  
    label_result2['text'] = f"total amount of calories to be lost : {ans}" 

label_current = tkinter.Label(root, text = "current: ")
label_current.grid(column=0, row = 0)
 
entry_current = tkinter.Entry(root)
entry_current.grid(column=1, row = 0)


label_goal = tkinter.Label(root, text = "goal weight : ")
label_goal.grid(column=0, row = 1)

entry_goal = tkinter.Entry(root)
entry_goal.grid(column=1, row = 1)




button_calculate = tkinter.Button(root, text="Calculate", command=calculate_exercise)
button_calculate.grid(column=0, row = 2)
   
label_result = tkinter.Label(root, text = "exercise: ")
label_result.grid(column=1, row = 2 )

label_result2 = tkinter.Label(root, text = "ans: ")
label_result2.grid(column=1, row = 3 )




root.mainloop()



