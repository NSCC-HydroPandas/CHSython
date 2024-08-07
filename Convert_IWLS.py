from tkinter import *
from idlelib.ToolTip import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import numpy as np
from os import listdir, path, remove, mkdir, chdir, getcwd
import datetime

owd = getcwd() ## Get Script Dir

class Application(Frame):
    """Intialize Query Application"""

    def __init__(self, master):
        """Initialize the Frames for Querys"""
        Frame.__init__(self, master)
        self.grid()
        self.app_widgets()

    def Search_filet(self):
        
        self.Tide_Fi = filedialog.askopenfilename(initialdir = "/", title = "Select Tide CSV file",
                                   filetypes = (("CSV","*.csv"),("all files","*.*")))
        self.TFILE.set(self.Tide_Fi)

    def app_widgets(self):
        """Creates Widgets for user GUI"""

        OUD = LabelFrame(self, text="Tide File Convert Options", foreground="blue")
        OUD.grid(row=1, column=0, padx=1, sticky=W+N)

        self.TFILE = StringVar()
        self.TFile = Entry(OUD, width=35, textvariable=self.TFILE)
        self.TFile_text = Label(OUD, text="Station File")
        self.TFile_text.grid(row=0, column=0, sticky=W)
        self.TFile.grid(row=0, column=1, sticky=W)
        self.ButtonTide = Button(OUD, text="...", height=0,
                              command=self.Search_filet)
        self.ButtonTide.grid(row=0, column=3, sticky=W, padx=2)


        self.Button_Q = Button(self, text="Run", height=0,
                               command=self.Run_Queries)
        self.Button_Q.grid(row=5, column=0, sticky=W, padx=2)    

    def Run_Queries(self):
        self.Convert_File()


    def Convert_File(self):
        
        TF = self.TFILE.get()
        head_tail = path.split(TF)
        Filename = path.basename(TF)
        Fname = path.splitext(Filename)


        FTF = pd.read_csv(TF, header=0)

        FTF['Date'] = pd.to_datetime(FTF['Date'], infer_datetime_format=True)
        FTF['Day'] = [d.date() for d in FTF['Date']]
        FTF['Time'] = [d.time() for d in FTF['Date']]
        FTF['Day'] = FTF['Day'].astype(str).str.replace('-','/')
        FTF = FTF.drop(['Date'], axis=1)
        FTF.rename(columns = {'predictions (m)':'Tide', 'observations (m)':'Tide'}, inplace = True)
        FTF = FTF.reindex(columns= ['Day', 'Time', 'Tide'])
        FTF.to_csv(head_tail[0] + '/Formated_' + head_tail[1], index=False)


        with open(head_tail[0] + '/CarisTide_' + Fname[0] +'.txt', 'w') as f:
            dfAsString = FTF.to_string(header=False, index=False)
            f.write(dfAsString)
            f.close()

        with open(head_tail[0] + '/CarisTide_' + Fname[0] +'.tid', 'w') as f2:
            f2.write('--------\n')

            file = open(head_tail[0] + '/CarisTide_' + Fname[0] +'.txt', 'r')
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line=='' or line=="/n":
                    pass
                else:
                    f2.write(line + '\n')
            file.close()
            remove(head_tail[0] + '/CarisTide_' + Fname[0] +'.txt')

            
        
    
root = Tk()
root.title("Convert Tide Station CSV to Caris Tide")
root.geometry("400x100")
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
submenu2 = Menu(menu)
app = Application(root)
root.mainloop()
