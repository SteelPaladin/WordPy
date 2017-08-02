'''Created on 10 Mar 2017    -    10/03/17
Word processing application with Python 3x.     -    WordPy by Harrison Baillie.
TO_DO:  FONT SIZE (PRACTICALLY FUCKING IMPOSSIBLE), DOCUMENT TITLE LABEL, 'NEW' FUNCTION, HEADERS/FOOTERS, PAGES, PRINT, FONT PREVIEWS, .wpy, .docx.
@author: Harrison Baillie    -    SteelPaladin'''

from tkinter import *   #IMPORTING tkinter MODULE FOR GUI.
from tkinter.filedialog import asksaveasfile, askopenfile    #IMPORTING MODULE FOR SAVE & OPEN FUNCTIONS.
import sys, os, datetime
root=Tk()   #CREATES A WINDOW
root.title("WordPy")    #SETS THE WINDOW TITLE
root.iconbitmap('WordPy.ico')
root.geometry('600x650')    #STES THE WINDOW SIZE
root.resizable(False, False)    #MAKES THE WINDOW NOT RESIZEABLE TO THE USER
currentfont=()

statusVar=StringVar()
statusbar=Label(root,textvariable=statusVar,relief=SUNKEN)
statusbar.pack(fill=X,side=BOTTOM)
statusbar.config(anchor=S)

textEntry=Text(root, width=600,height=650)  #CREATES A TEXT ENTRY
scrlBar=Scrollbar(root) #CREATES A SCROLL BAR ASSIGNED TO textEntry
scrlBar.pack(side=RIGHT,fill=Y) #DISPLAYS SCROLL BAR.
textEntry.pack(side=LEFT, fill=Y)    #DISPLAYS THE TEXT ENTRY
scrlBar.config(command=textEntry.yview) #CONFIGURES THE SCROLL BAR.
textEntry.config(yscrollcommand=scrlBar.set)    #CONFIGURES textEntry TO USE THE SCROLL BAR.

wordpyMenu=Menu(root)   #CREATES A MENU

#DEFINING FUCNTIONS TO ALTER FONTS
def Courier():
    textEntry.configure(font="Courier")
    currentfont=("Courier")
def Helvetica():
    textEntry.configure(font="Helvetica")
    currentfont=("Helvetica")
def Fixedsys():
    textEntry.configure(font="Fixedsys")
    currentfont=("Fixedsys")
#FORMATTING FUNCTIONS
def Center():
    textEntry.tag_configure("center", justify=CENTER)
    textEntry.tag_add("center", 1.0, "end")
def Right():
    textEntry.tag_configure("right", justify=RIGHT)
    textEntry.tag_add("right", 1.0, "end")
def Left():
    textEntry.tag_configure("left", justify=LEFT)
    textEntry.tag_add("left", 1.0, "end")
#FILE FUNCTIONS, SAVE/OPEN etc.
def SaveAs(Event):   #FUNCTION TO SAVE AS .wpy FILE
    file=asksaveasfile(defaultextension='.wpy') #TRIGGERS FUNCTION TO 'SAVE AS'
    text=textEntry.get(0.0, END)    #RETRIEVES CONTENT OF THE textEntry WIDGET AND HOLDS IT AS text VARIABLE
    file.write(text.rstrip())   #WRITES THE FILE
    textEntry.insert(END, currentfont)
def Open(Event): #FUNCTION TO OPEN .wpy FILE
    global filename #SETS FILE NAME AS GLOBAL VARIABLE.
    file=askopenfile(parent=root,title='Choose file to Open')   #OPENS EXPLORER WINDOW TO SELECT FILE TO OPEN
    filename=str(file.name) #SETS THE NAME OF THE FILE AS STRING.
    text=file.read()   #READS THE FILE
    textEntry.delete(0.0, END)  #CLEARS THE CURRENT textEntry WINDOW
    textEntry.insert(0.0, text)    #INSERTS THE READ FILE TO THE textEntry WIDGET.
    file.close()    #CLOSES THE FILE (IMPROVED PERFORMANCE, UNNECESSARY PROCESSES).
def AddToday():
    textEntry.insert(END,datetime.date.today())
def fontUp():
    print(textEntry.config()['font'])
menuLabels=["File","Edit"]  #LABELS FOR THE MAIN MENU BAR.

subMenus=[]
for i in range(len(menuLabels)):    #LOOP TO CREATE THE MENU LABELS
    menux=Menu(wordpyMenu)
    subMenus.append(menux)
    wordpyMenu.add_cascade(label=menuLabels[i],menu=menux)

fontMenu=Menu(wordpyMenu)   #CREATES ANOTHER MENU THAT CASCADES FROM EDIT FOR FONT CHANGES.
formatMenu=Menu(wordpyMenu)
formatOptions=["Center","Right","Left"]
fonts=["Courier","Helvetica","Fixedsys"]    #LIST OF POSSIBLE FONTS AS STRINGS.
for i in range(len(fonts)):
    fontMenu.add_command(label=str(fonts[i]),command=eval(fonts[i]))    #ADDING COMMANDS TO THE CASCADING FONT MENU
    if i >= (len(fonts)-1): #CHECKING IF THE LOOP SHOULD MOVE TO THE NESTED 'WHILE' IF FINISHED WITH THE FONT OPTIONS.
        loop=int(0)
        while loop != len(formatOptions):   #NESTED WHILE LOOP FOR FORMAT MENU
            formatMenu.add_command(label=str(formatOptions[loop]),command=eval(formatOptions[loop]))    #ADDING COMMANDS TO THE FORMATTING MENU
            loop=loop+1 #CONTINUING THE NESTED WHILE LOOP

subMenus[1].add_cascade(label="Font",menu=fontMenu) #ADDING THE CASCADING MENU TO THE FONT OPTION
subMenus[1].add_cascade(label="Format",menu=formatMenu) #ADDING THE CASCADING MENU TO THE FORMAT OPTION
subMenus[1].add_command(label="Font Up",command=fontUp)
subMenus[1].add_command(label="Add Today's Date",command=AddToday)
#THE accelerator FUNCTION SHOWS THE SHORTCUT KEYS ON THE WIDGET.
subMenus[0].add_command(label="Save As",command=SaveAs,accelerator='Ctrl+Shift') #ADDING THE COMMAND TO CALL THE SAVE AS FUNCTION
root.bind('<Control-Key-s>', SaveAs)
subMenus[0].add_command(label="Open",command=Open,accelerator='Ctrl+O')  #ADDING THE COMMAND TO CALL THE OPEN FILE FUNCTION.
root.bind('<Control-Key-o>', Open)  #BINDING Ctrl+O TO THE Open() FUNCTION.
root.config(menu=wordpyMenu)    #CONFIGURES WINDOW TO HAVE MENU
root.mainloop() #LOOPS THE WINDOW TO RUN, GOES AT THE END OF THE PROGRAM.
