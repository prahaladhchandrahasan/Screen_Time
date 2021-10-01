# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import tkinter as Tkinter 
import sys 
import calendar
from datetime import datetime 
from datetime import date
from csv import writer 
List = []
date = date.today()
List.append(date)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
List.append(current_time)
counter = 66600
running = False
def counter_label(label): 
	def count(): 
		if running: 
			global counter 
	
			# To manage the intial delay. 
			if counter==66600:			 
				display="Starting..."
			else: 
				tt = datetime.fromtimestamp(counter) 
				string = tt.strftime("%H:%M:%S") 
				display=string 
	
			label['text']=display # Or label.config(text=display) 
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
			label.after(1000, count) 
			counter += 1
	
	# Triggering the start of the counter. 
	count()	 

def Stop():
    end = datetime.now()
    end_time = end.strftime("%H:%M:%S")
    List.append(end_time)
    q = end-now
    q1 = str(q)
    List.append(q1)



    with open('record.csv', 'a') as f_object: 
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()
        sys.exit("Bye Bye")
        



root = Tkinter.Tk() 
root.title("Screen Time") 
	
# Fixing the window size. 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="red", font="Verdana 30 bold") 
label.pack() 
f = Tkinter.Frame(root) 
running = True
counter_label(label)
Exit = Tkinter.Button(f, text='EXIT',width=6, command=Stop) 
f.pack(anchor = 'center',pady=5) 
Exit.pack(side="left")  
root.mainloop() 
