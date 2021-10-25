from tkinter import *
from tkinter import ttk
import subprocess as sp
programname = 'Notepad.exe'
filename = 'D:\learningPython\practise\count.txt'

def Open():
	sp.Popen([programname, filename])
def men_plus():
	value_men.set(int(value_men.get()) + 1)
	men = value_men.get() 
	women = value_women.get() 
	result = int(men) + int(women)
	total.set(result)

def men_minus():
	value_men.set(int(value_men.get()) - 1)
	men = value_men.get() 
	women = value_women.get() 
	result = int(men) + int(women)
	total.set(result)

def women_plus():
	value_women.set(int(value_women.get()) + 1)
	men = value_men.get() 
	women = value_women.get() 
	result = int(men) + int(women)
	total.set(result)

def women_minus():
	value_women.set(int(value_women.get()) - 1)
	men = value_men.get() 
	women = value_women.get() 
	result = int(men) + int(women)
	total.set(result)

def Save():
	men = value_men.get() 
	women = value_women.get() 
	result = int(men) + int(women)
	total.set(result)
	msg = 'M = ' + value_men.get() + '\nW = ' + value_women.get() + '\nTotal = ' + total.get()
	try:
		file = open(r'D:\learningPython\practise\count.txt','w')
		file.write(msg)
		file.close()
	except FileNotFoundError:
		print('ไม่พบไฟล์')
	
mainframe = Tk()
mainframe.title('Count')

ttk.Label(mainframe, text='#Men').grid(column=0, row=0, padx=2, pady=2, sticky='e')
ttk.Label(mainframe, text='#Women').grid(column=0, row=1, padx=2, pady=2, sticky='e')
ttk.Label(mainframe, text='Total').grid(column=0, row=2, padx=2, pady=2, sticky='e')

value_men = StringVar()
value_women = StringVar()
total = StringVar()
entry_men = ttk.Entry(mainframe, textvariable=value_men).grid(column=1, row=0)
entry_women = ttk.Entry(mainframe, textvariable=value_women).grid(column=1, row=1)
entry_total = ttk.Entry(mainframe, textvariable= total).grid(column=1, row=2)

ttk.Button(mainframe,text='+M',command= men_plus).grid(column=2, row=0)
ttk.Button(mainframe,text='-M',command=men_minus).grid(column=3, row=0)

ttk.Button(mainframe,text='+W',command=women_plus).grid(column=2, row=1)
ttk.Button(mainframe,text='-W',command=women_minus).grid(column=3, row=1)

ttk.Button(mainframe,text='Open',command=Open).grid(column=2, row=2)
ttk.Button(mainframe,text='Save',command=Save).grid(column=3, row=2)


mainframe.mainloop()









