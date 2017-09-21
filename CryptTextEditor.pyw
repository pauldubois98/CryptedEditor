from tkinter import *
from code import code, decode
from primeFunc import *
import tkinter.font as tkFont
import webbrowser


class CryEdit(Frame):
    """frame class of text edition"""
    def __init__(self, root, file, password, txt='', new=True, width=80, height=20):
        """__init__ automatic function"""
        Frame.__init__(self, root, relief='groove', borderwidth=5)
        self.file=file
        self.password=password
        if new:
            self.txt=txt
            self.p, self.q, self.n, self.phi, self.e, self.d = newKeys(password)
        else:
            self.txt, self.p, self.q, self.n, self.phi, self.e, self.d = decode(file, password)

        ###graphic elements
        #title
        self.title=Button(self, text=file, font=tkFont.Font(family='Helvetica',\
                          size=24, weight='bold'), relief='flat', \
                          command=self.info, fg='purple')
        self.title.grid(row=0, column=0, columnspan=5)
        #text entry zone
        self.entr=Text(self, undo=True, width=width, height=height)
        self.entr.insert('1.0', self.txt)
        self.entr.grid(row=3, column=0, columnspan=5)
        #save button
        self.btSave=Button(self, text='Save', bg='light green', activebackground='green', command=self.save)
        self.btSave.grid(row=2, column=0)
        self.entr.bind('<Control-s>', self.save)
        self.entr.bind('<Control-S>', self.save)
        #save & quit button
        self.btSQuit=Button(self, text='Save & Quit', bg='orange', activebackground='darkorange', command=self.squit)
        self.btSQuit.grid(row=2, column=1)
        self.entr.bind('<Control-q>', self.squit)
        self.entr.bind('<Control-Q>', self.squit)
        #quit button
        self.btQuit=Button(self, text='Quit', bg='red', activebackground='darkred', command=self.Quit)
        self.btQuit.grid(row=2, column=2)
        #undo button
        self.btQuit=Button(self, text='Undo', bg='blue', activebackground='blue', activeforeground='white',\
                           command=self.undo)
        self.btQuit.grid(row=2, column=4)
        self.entr.bind('<Control-z>', self.undo)
        self.entr.bind('<Control-Z>', self.undo)
        #redo button
        self.btQuit=Button(self, text='Redo', bg='light blue', activebackground='light blue',\
                           activeforeground='white', command=self.redo)
        self.btQuit.grid(row=2, column=3)
        self.entr.bind('<Control-y>', self.redo)
        self.entr.bind('<Control-Y>', self.redo)


    def undo(self, event=None):
        """to undo in the text edition"""
        try:
            self.entr.edit_undo()
        except:
            self.bell()
    def redo(self, event=None):
        """to undo in the text edition"""
        try:
            self.entr.edit_redo()
        except:
            self.bell()
            
    def save(self, event=None):
        """to save the text"""
        self.txt=self.entr.get('1.0', 'end-1c')
        code(self.file, self.txt, self.e, self.n)

    def squit(self, event=None):
        """to save and quit"""
        self.save()
        self.Quit()

    def Quit(self, event=None):
        """fo close the text editor"""
        self.destroy()
        del self

    def info(self, event=None):
        """to display the keys of RSA encryption"""
        T=Toplevel(bg='silver')
        T.title('Keys of RSA encryption')
        mess=Message(T, bg='grey', text="""\
Public keys: (at the begining of the file)\n\
n={}\n\
e={}\n\n\
Private keys: (extracted from the password)
p={}\n\
q={}\n\
phi={}\n\
d={}\n\n\
password: {}""".format(self.n, self.e, self.p, self.q, self.phi, self.d, \
                         self.password))
        mess.pack()
        but=Button(T, text="Close", command=T.destroy, bg='black', fg='white')
        but.pack()








class OpenMenu(Frame):
    """frame class for choosing file to edit"""
    def __init__(self, root, file='', psw='', width=40):
        """__init__ automatic function"""
        #frame init & pack
        Frame.__init__(self, root, relief='groove', borderwidth=10)
        self.pack()
        
        ###title LABEL
        self.title=Label(self, text='Open a new file...', font=tkFont.Font(\
            family='Helvetica', size=20, weight='bold'), fg='red', width=width)
        self.title.grid(row=0, column=1, columnspan=2)
        ##open BUTTON
        self.openBut=Button(self, text='Open the file', fg='green', \
                            command=self.tryToOpen, \
                            activebackground='darkgreen')
        self.openBut.grid(row=4, column=1, columnspan=2)
        ###ENTRIES
        ##file
        #lab
        self.fileLab=Label(self, text='File name:')
        self.fileLab.grid(row=2, column=1, sticky='e')
        #entr
        self.file=StringVar()
        self.file.set(file)
        self.fileEnt=Entry(self, textvariable=self.file)
        self.fileEnt.grid(row=2, column=2, sticky='w')
        self.fileEnt.bind('<Return>', self.hitReturn)
        ##psw
        #lab
        self.pswLab=Label(self, text='File password:')
        self.pswLab.grid(row=3, column=1, sticky='e')
        #entr
        self.psw=StringVar()
        self.psw.set(psw)
        self.pswEnt=Entry(self, textvariable=self.psw)
        self.pswEnt.grid(row=3, column=2, sticky='w')
        self.pswEnt.bind('<Return>', self.hitReturn)
        ##new-file CHECK-BUTTON
        self.new=IntVar()
        self.chbt=Checkbutton(self, text='Open as new file', variable=self.new)
        self.chbt.grid(row=1, column=1, columnspan=2)

        
        
        #files var
        self.framFiles=Frame(root, relief='groove', borderwidth=3)
        self.framFiles.pack()
        self.openFiles=[]
        

    def hitReturn(self, event=None):
        """method to be called when return is hited"""
        #need an other method the self.openBut.invoke as an event is given as an argument
        self.openBut.invoke()

    def tryToOpen(self, event=None):
        """function that looks if the openning is possible"""
        ##coloration of the entries:
        #blue: already existing file
        #green: new file
        #red: error
        if self.psw.get()=='':
            self.fileEnt.config(bg='red')
            self.pswEnt.config(bg='darkred')
        else:
            psw=self.psw.get()
            if self.new.get():
                self.fileEnt.config(bg='light green')
                self.pswEnt.config(bg='dark green')
                self.openNew(new=True)
            else:
                try:
                    file=open(self.file.get(), 'r')
                    self.openNew(txt='')
                except:
                    self.fileEnt.config(bg='red')
                    self.pswEnt.config(bg='dark red')
                else:
                    self.fileEnt.config(bg='light blue')
                    self.pswEnt.config(bg='blue')
    
    def openNew(self, txt='Type here your text to safely store...\n', new=False):
        """function that open a file"""
        new=CryEdit(self.framFiles, self.file.get(), self.psw.get(), txt=txt, \
                    new=new)
        new.grid(row=2, column=len(self.openFiles)+1)
        self.openFiles.append(new)




def openAbout():
    """open the "about US" web page"""
    try:
        webbrowser.open('aboutUS.html')
    except:
        print('error')
def openRSA():
    """open the wikipedia page about RSA crypting system"""
    try:
        webbrowser.open('https://en.wikipedia.org/wiki/RSA_(cryptosystem)')
    except:
        print('error')
def openGuide():
    """open the "user guide" web page"""
    try:
        webbrowser.open('user_guide.html')
    except:
        print('error')
        

        




if __name__=='__main__':
    #####Thing to be done if executed a principal program
    ###Window
    fen=Tk()
    fen.title('RSA-Crypted text editor')
    
    ##Infos Frame
    info=Frame(fen, bg='silver')
    info.pack()
    #About US button
    about=Button(info, text='Learn more about us', command=openAbout, \
                 bg='black', fg='white', activebackground='white', \
                 activeforeground='black')
    about.grid(row=1, column=1)
    #RSA button
    about=Button(info, text='Learn more about RSA encryption', command=openRSA,\
                 fg='black', activeforeground='white', \
                 bg='grey', activebackground='grey')
    about.grid(row=1, column=2)
    #UserGuide button
    about=Button(info, text='User Guide of this editor', command=openGuide, \
                 bg='white', fg='black', activebackground='black', \
                 activeforeground='white')
    about.grid(row=1, column=3)
    
    ###Menu
    menu=OpenMenu(fen, 'text.txt', 'psw')
    menu.openBut.invoke()




    #mainloop
    fen.mainloop()


