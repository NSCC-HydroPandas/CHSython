from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
import re


class Application(Frame):

        def __init__(self, master):

                Frame.__init__(self, master)
                self.grid()
                self.create_widgets()

        def create_widgets(self):

                self.Button_Con = Button(self, text="Convert", height=0,
                               command=self.JD_Conv)
                self.Button_Con.grid(row=1, column=1, sticky=W, padx=2)

                JD_op = LabelFrame(FJD, foreground="blue")
                JD_op.grid(row=0, column=0, padx=1, sticky=W)

                self.Y = StringVar()
                self.y = Entry(JD_op, width=5, textvariable=self.Y)
                self.y_text = Label(JD_op, text="Year")
                self.y_text.grid(row=0, column=0, sticky=W)
                self.y.grid(row=0, column=1, sticky=W)


                self.D = StringVar()
                self.d = Entry(JD_op, width=5, textvariable=self.D)
                self.d_text = Label(JD_op, text="Day")
                self.d_text.grid(row=0, column=2, sticky=W)
                self.d.grid(row=0, column=3, sticky=W)

                self.M = StringVar()
                self.m = Entry(JD_op, width=5, textvariable=self.M)
                self.m_text = Label(JD_op, text="Month")
                self.m_text.grid(row=0, column=4, sticky=W)
                self.m.grid(row=0, column=5, sticky=W)

                self.textL = Label(JD_op, text="Julian Day is:")
                self.textL.grid(row=1, column=0, sticky=W)
                self.text = Text(JD_op, width=5, height=1)
                self.text.grid(row=1, column=1, sticky=W)
                

        def JD_Conv(self):

                M = self.M.get()
                D = int(self.D.get())
                Y = int(self.Y.get())
                Search = re.findall('\w\w', M)

                if Search == []:
                        M = ('%0.2d' % int(M))
                else:
                        M = M
                
                if Y%4 == 0:
                        Jan = list(range(1,32))
                        FebL = list(range(32,61))
                        MarL = list(range(61,92))
                        AprL = list(range(92,122))
                        MayL = list(range(122,153))
                        JunL = list(range(153,183))
                        JulL = list(range(183,214))
                        AugL = list(range(214,245))
                        SeptL = list(range(245,275))
                        OctL = list(range(275,306))
                        NovL = list(range(306,336))
                        DecL = list(range(336,367))

                        FebL.append('Nan')
                        FebL.append('Nan')
                        AprL.append('Nan')
                        JunL.append('Nan')
                        SeptL.append('Nan')
                        NovL.append('Nan')

                        JD = pd.DataFrame(
                                {'01': Jan,
                                 '02': FebL,
                                 '03': MarL,
                                 '04': AprL,
                                 '05': MayL,
                                 '06': JunL,
                                 '07': JulL,
                                 '08': AugL,
                                 '09': SeptL,
                                 '10': OctL,
                                 '11': NovL,
                                 '12': DecL})

                else:
                        Jan = list(range(1,32))
                        Feb = list(range(32,60))
                        Mar = list(range(60,91))
                        Apr = list(range(91,121))
                        May = list(range(121,152))
                        Jun = list(range(152,182))
                        Jul = list(range(182,213))
                        Aug = list(range(213,244))
                        Sept = list(range(244,274))
                        Oct = list(range(274,305))
                        Nov = list(range(305,335))
                        Dec = list(range(335,366))

                        Feb.append('Nan')
                        Feb.append('Nan')
                        Feb.append('Nan')
                        Apr.append('Nan')
                        Jun.append('Nan')
                        Sept.append('Nan')
                        Nov.append('Nan')

                        JD = pd.DataFrame(
                                {'01': Jan,
                                 '02': Feb,
                                 '03': Mar,
                                 '04': Apr,
                                 '05': May,
                                 '06': Jun,
                                 '07': Jul,
                                 '08': Aug,
                                 '09': Sept,
                                 '10': Oct,
                                 '11': Nov,
                                 '12': Dec})

                JDs = JD.loc[(D-1), M] ## Fix index issue where Python starts at 0
                
                message = str(JDs)
                self.text.delete(0.0, END)
                self.text.insert(0.0, message)


root = Tk()
root.title("DOY to JD")
root.geometry("270x80")
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
notebook = ttk.Notebook(root)
FJD = ttk.Frame(notebook)
notebook.add(FJD, text="Convert DOY to JD")
notebook.grid(row=0, column=0)
app = Application(root)
root.mainloop()
