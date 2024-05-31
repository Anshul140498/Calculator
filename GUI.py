from tkinter import *
from tkinter.messagebox import *
#Some useful variables
font =('Cambria',24 , 'bold')
font2=('Helvetica ' , 28)
font3 =('Helvetica',14 , 'bold')

# all clear

def all_clear():
     textField.delete(0,END)

# single clear function
def clear():
     ex=textField.get()
     ex=ex[0:len(ex)-1]
     textField.delete(0,END)
     textField.insert(0,ex)


# Bind functions
def Click_Btn_function(event):
    print('btn clicked')
    b=event.widget
    text=b['text']
    print(text)
    if text=='=':
        try:
            ex=textField.get()
            ans=eval(ex)
            textField.delete(0,END)
            textField.insert(0,ans)
        except Exception as e:
                print("Error...")
                showerror("Error",e)
        return

    textField.insert(END,text)


#creating a window
window=Tk()
x=window.title("Calculator")
window.geometry('520x600') #Width x height
# heading label
heading = Label(window, text="CALCULATOR",font = font )
heading.pack(side=TOP)

# Text field
textField=Entry(window , font=font3 , justify=CENTER)
textField.pack(side=TOP ,pady=10,fill=X,padx=10)

#Buttons
buttonFrame = Frame(window)
buttonFrame.pack()

# adding buttons
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn1=Button(buttonFrame,text=str(temp),font=font2,width=5,relief='ridge',bg='light grey',activebackground='dark salmon',activeforeground='white')
        btn1.grid(row=i,column=j,padx=5,pady=5)
        temp=temp+1
        btn1.bind('<Button-1>',Click_Btn_function)

zerobtn=Button(buttonFrame,text='0',font=font2,width=5,relief='ridge',bg='light gray',activebackground='dark salmon',activeforeground='white',)
zerobtn.grid(row=3,column=0,padx=5,pady=5)
Brkbtn2=Button(buttonFrame,text='(',font=font2,width=5,relief='ridge',bg='light gray',activebackground='dark salmon',activeforeground='white',)
Brkbtn2.grid(row=3,column=1,padx=5,pady=5)
Brktbtn=Button(buttonFrame,text=')',font=font2,width=5,relief='ridge',bg='light gray',activebackground='dark salmon',activeforeground='white',)
Brktbtn.grid(row=3,column=2,padx=1,pady=1)
dotbtn=Button(buttonFrame,text='.',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white',)
dotbtn.grid(row=4,column=0,padx=5,pady=5)
equalbtn=Button(buttonFrame,text='=',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white')
equalbtn.grid(row=4,column=1,padx=5,pady=5)
clear=Button(buttonFrame,text='C',font=font2,width=5,relief='solid',bg='gray65',command=clear,activebackground='dark salmon',activeforeground='white',)
clear.grid(row=4,column=2,padx=5,pady=5)
add=Button(buttonFrame,text='+',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white',)
add.grid(row=0,column=3,padx=5,pady=5)
sub=Button(buttonFrame,text='-',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white',)
sub.grid(row=1,column=3,padx=5,pady=5)
divide=Button(buttonFrame,text='/',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white',)
divide.grid(row=2,column=3,padx=5,pady=5)
mul=Button(buttonFrame,text='*',font=font2,width=5,relief='solid',bg='gray65',activebackground='dark salmon',activeforeground='white',)
mul.grid(row=3,column=3,padx=5,pady=5)
AC=Button(buttonFrame,text='AC',font=font2,width=5,relief='solid',bg='gray65',command=all_clear,activebackground='dark salmon',activeforeground='white',)
AC.grid(row=4,column=3,padx=5,pady=5)

# bind all other hard cded buttons

add.bind('<Button-1>',Click_Btn_function)
sub.bind('<Button-1>',Click_Btn_function)
mul.bind('<Button-1>',Click_Btn_function)
divide.bind('<Button-1>',Click_Btn_function)
dotbtn.bind('<Button-1>',Click_Btn_function)
zerobtn.bind('<Button-1>',Click_Btn_function)
Brktbtn.bind('<Button-1>',Click_Btn_function)
Brkbtn2.bind('<Button-1>',Click_Btn_function)
equalbtn.bind('<Button-1>',Click_Btn_function)

window.mainloop()