from tkinter import *
from PIL import Image,ImageTk
import speech_to_text
import action





a=Tk()
a.title("AI Assistant")
a.config(bg="SKY BLUE")
a.geometry("1000x800")
a.resizable(False,False)



def ask():


    user_val = speech_to_text.speech_to_text()

    if user_val is None:
        text.insert(END, "Voice not recognized\n")
        return
    text.insert(END, "DEBUG: I heard ---> " + user_val + "\n")

    bot_val = action.Action(user_val)

    text.insert(END, "User ---> " + user_val + "\n")
    text.insert(END, "Bot ---> " + bot_val + "\n")

  
 



    

def send():
   
    user_val = entry.get()
    
    if user_val.strip() == "":
        text.insert(END, "Please type something\n")
        return
    
    bot_val = action.Action(user_val)
    
    text.insert(END, "User ---> " + user_val + "\n")
    text.insert(END, "Bot  ---> " + bot_val + "\n")
    
    entry.delete(0, END)  # clear the entry box after sending


def delete():
    text.delete(1.0, END)  # clears entire chat text box
    entry.delete(0, END)   # clears entry box too









frame =LabelFrame(a,padx=100,pady=7,borderwidth=15)
frame.config(bg="SKY BLUE")
frame.grid (row=0,column=1 ,padx=40,pady=10)

text_label=Label(frame,text="AI ASSISTANT", font=("Comic Sans MS", 18, "bold"))
text_label.grid(row=0,column=0,padx=20,pady=10)


image=ImageTk.PhotoImage(Image.open(r"C:\Users\Srinithi S\Downloads\images (2).jpg"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=10) 

text=Text(a,font=('courier 10 bold'),bg="sky blue",borderwidth=5)
text.grid(row=2,column=0)
text.place(x=200,y=600,width=375,height=45)


entry=Entry(a,justify=CENTER)
entry.place(x=200,y=650,width=375,height=20)


Button1=Button(a,text="ASK",bg="#356696", pady=16,padx=40,borderwidth=3,command=ask)
Button1.place(x=800,y=100)


Button2=Button(a,text="SEND",bg="#356696", pady=16,padx=40,borderwidth=3,command=send)
Button2.place(x=800,y=300)


Button3=Button(a,text="DELETE",bg="#356696", pady=16,padx=40,borderwidth=3,command=delete)
Button3.place(x=800,y=500)









a.mainloop()
