from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from idlelib.ToolTip import *
import subprocess as S
from os import listdir, path
import pandas as pd
import numpy as np


Caris = ('C:/Program Files/CARIS/HIPS and SIPS/11.3/bin')
Caris_Env = ('C:/Program Files/CARIS/HIPS and SIPS/11.3/system')

def JD_Conv(M, D, Y):

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
                return str(Y) + '-' + str(JDs) 

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.Widgets()

    def Search_TrackLines (self):
        """Search for Trackline Folder"""
        Dir = filedialog.askdirectory(initialdir = "/", title='Select Track Line Directory')
        self.TL_Dir.set(Dir)

        TL_Dir_list = listdir(Dir)

        self.listbox.delete(0,'end')
        for item in TL_Dir_list:
            if not item.startswith('JD') and not item.endswith(".rawdataindex"): 
                self.listbox.insert(END, item)


    def Search_VesselFile(self):
        """Allows the user to choose the
        Vessel Config file, then updates the
        Vessel file entry box with the selected Vessel file path"""

        vessel = self.VESSEL_N.get()
        V = path.split(vessel)

        VESSEL_File = filedialog.askopenfilename(initialdir = V[0],
                                       title = 'Select Vessel File',
                                       filetypes = (("Vessel Config","*.hvf"),("all files","*.*")))
        self.VESSEL_N.set(VESSEL_File)
        tip_Vessel = ToolTip(self.VESSEL_n, (self.VESSEL_N.get()))

    
    def Widgets(self):

        self.Refract = LabelFrame(self, text="Caris Refraction Options", foreground="blue")
        self.Refract.grid(row=0, column=0, sticky=W)
        
        self.TL_Dir = StringVar()
        self.tl_dir = Entry(self.Refract, width=38, textvariable=self.TL_Dir)
        self.tl_dir_text = Label(self.Refract, text="TrackLine Directory")
        self.tl_dir_text.grid(row=1, column=0, sticky=W)
        self.tl_dir.grid(row=1, column=1, sticky=W)
        self.Button = Button(self.Refract, text="...", height=0,
                              command=self.Search_TrackLines)
        self.Button.grid(row=1, column=2, sticky=W, padx=2)
        

        self.listbox = Listbox(self.Refract, height=25, width=38, selectmode=EXTENDED)
        self.listbox.grid(row=2, column=1, sticky=W)

        self.PROFILE = StringVar()
        self.Profile = Entry(self.Refract, width=5, textvariable=self.PROFILE)
        self.Profile_text = Label(self.Refract, text="Number of Profiles")
        self.Profile_text.grid(row=0, column=0, sticky=W)
        self.Profile.grid(row=0, column=1, sticky=W)


        self.Button1 = Button(self, text="Compute Refraction \n Coefficients", height=0,
                              command=self.Refraction)
        self.Button1.grid(row=23, column=0, sticky=W, padx=2)

        self.ER = IntVar()
        self.E_R = Checkbutton(self, onvalue=1, offvalue=0, variable=self.ER, text= "Edit Refraction Coefficients File",
                               command=self.Edit)
        self.E_R.grid(row=1, column=0, sticky=W)

        self.GeoRef = IntVar()
        self.Geo_Ref = Checkbutton(self, onvalue=1, offvalue=0, variable=self.GeoRef, text= "Georeference Lines",
                               command=self.Georeference)
        self.Geo_Ref.grid(row=2, column=0, sticky=W)


    def Refraction(self):

        TL_Dir = self.TL_Dir.get()
        TL_Dir_list = listdir(TL_Dir)
        Tracklines = [self.listbox.get(idx) for idx in self.listbox.curselection()]
        no_Profiles = self.PROFILE.get()

        with open('Refract_Track_Lines.bat', "w") as R:
            R.write('@ECHO OFF' + '\n')
            R.write('ECHO Computing Refraction Coefficients' + '\n')
            R.write('cd '+ Caris_Env + '\n')
            R.write('call caris_env.bat' + '\n')

            for TL in Tracklines:
                R.write('refract' + ' ' + TL_Dir + '/' + TL + ' ' + no_Profiles + '\n')
            R.write('pause')
                
        p = S.check_call("Refract_Track_Lines.bat", stdin=None, stdout=None, stderr=None, shell=False)


    def Georeference(self):

        if self.GeoRef.get() ==1:

            self.GEOREF = LabelFrame(self, text="GEOREFERENCE", foreground="blue")
            self.GEOREF.grid(row=0, column=2, sticky=W)

            self.VERT_REF = StringVar()
            vert_ref = ['NONE',
                        'GPS',
                        'TIDE']

            self.VREF_op = ttk.Combobox(self.GEOREF, values=vert_ref, width=7, textvariable=self.VERT_REF)
            self.VREF_text = Label(self.GEOREF, text="Choose Vertical Reference")
            self.VREF_text.grid(row=1, column=0, sticky=W)
            self.VREF_op.grid(row=1, column=1, sticky=W+E, padx=0)

            ## Vessel File Name (inlcuing .hvf)
            self.VESSEL_N = StringVar()
            self.VESSEL_n = Entry(self.GEOREF, width=30, textvariable=self.VESSEL_N)
            self.VESSEL_text = Label(self.GEOREF, text="Select Vessel File")
            self.VESSEL_text.grid(row=2, column=0, sticky=W)
            self.VESSEL_n.grid(row=2, column=1, sticky=W)
            self.Button4 = Button(self.GEOREF, text="...", height=0,
                                  command=self.Search_VesselFile)
            self.Button4.grid(row=2, column=2, sticky=W, padx=2)

            self.Button1 = Button(self.GEOREF, text="Apply Refraction \n Coefficients", height=0,
                                  command=self.Apply_RefCoefficients)
            self.Button1.grid(row=4, column=0, sticky=W, padx=2)


    def Edit(self):

        if self.ER.get() ==1:

            self.Edit_coe = LabelFrame(self, text="Edit Refraction Coefficients File", foreground="blue")
            self.Edit_coe.grid(row=0, column=1, sticky=W)

            
            self.E_L=IntVar()
            self.sol = Radiobutton(self.Edit_coe, text= "Start Of Line", variable=self.E_L,
                        value=1, command=self.Line_Location).grid(row=0, column=0, sticky= W)
            self.eol = Radiobutton(self.Edit_coe, text= "End of Line", variable=self.E_L,
                        value=2, command=self.Line_Location).grid(row=1, column=0, sticky=W)
            self.mol = Radiobutton(self.Edit_coe, text= "Middle of Line", variable=self.E_L,
                        value=3, command=self.Line_Location).grid(row=2, column=0, sticky=W)

            self.Button = Button(self.Edit_coe, text="Edit RefCoe File", height=0,
                              command=self.Edit_RefCoe)
            self.Button.grid(row=3, column=0, sticky=W, padx=2)
        

        else:
            try:
                self.Edit_coe.grid_forget()
            except AttributeError:
                pass

        
            
            

    def Line_Location(self):


        if self.E_L.get() == 1: 

            self.PROFILE_S = StringVar()
            self.Profile_s = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_S)
            self.Profile_s_text = Label(self.Edit_coe, text="Profile Cutoff Start")
            self.Profile_s_text.grid(row=1, column=1, sticky=W)
            self.Profile_s.grid(row=1, column=2, sticky=W, padx=2)

            self.PROFILE_E = StringVar()
            self.Profile_e = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_E, state='disabled')
            self.Profile_e_text = Label(self.Edit_coe, text="Profile Cutoff End")
            self.Profile_e_text.grid(row=2, column=1, sticky=W)
            self.Profile_e.grid(row=2, column=2, sticky=W, padx=2)


        elif self.E_L.get() == 2:
            
            self.PROFILE_S = StringVar()
            self.Profile_s = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_S, state='disabled')
            self.Profile_s_text = Label(self.Edit_coe, text="Profile Cutoff Start")
            self.Profile_s_text.grid(row=1, column=1, sticky=W)
            self.Profile_s.grid(row=1, column=2, sticky=W, padx=2)
            
            self.PROFILE_E = StringVar()
            self.Profile_e = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_E)
            self.Profile_e_text = Label(self.Edit_coe, text="Profile Cutoff End")
            self.Profile_e_text.grid(row=2, column=1, sticky=W)
            self.Profile_e.grid(row=2, column=2, sticky=W, padx=2)

        elif self.E_L.get() == 3:
            
            self.PROFILE_S = StringVar()
            self.Profile_s = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_S)
            self.Profile_s_text = Label(self.Edit_coe, text="Profile Cutoff Start")
            self.Profile_s_text.grid(row=1, column=1, sticky=W)
            self.Profile_s.grid(row=1, column=2, sticky=W, padx=2)
            
            self.PROFILE_E = StringVar()
            self.Profile_e = Entry(self.Edit_coe, width=5, textvariable=self.PROFILE_E)
            self.Profile_e_text = Label(self.Edit_coe, text="Profile Cutoff End")
            self.Profile_e_text.grid(row=2, column=1, sticky=W)
            self.Profile_e.grid(row=2, column=2, sticky=W, padx=2)


    def Edit_RefCoe(self):

        TL_Dir = self.TL_Dir.get()
        TL_Dir_list = listdir(TL_Dir)
        Tracklines = [self.listbox.get(idx) for idx in self.listbox.curselection()]

        if len(Tracklines)== 1:
            for TL in Tracklines:
                Refract_coe = pd.read_csv(TL_Dir + '/' + TL + '/refCoefficients', delimiter='\s+', header=None)

                if self.E_L.get()==1:
                    st = int(self.PROFILE_S.get())
                    Refract_coe[2] = np.where(Refract_coe[0] < st, 0, Refract_coe[2])
                    
                elif self.E_L.get()==2:
                    end = int(self.PROFILE_E.get())
                    Refract_coe[2] = np.where(Refract_coe[0] > end, 0, Refract_coe[2])

                elif self.E_L.get()==3:
                    st = int(self.PROFILE_S.get())
                    end = int(self.PROFILE_E.get())
                    Refract_coe[2] = np.where((Refract_coe[0] > st) & (Refract_coe[0] < end), 0, Refract_coe[2])
                    
                Refract_coe.to_csv(TL_Dir + '/' + TL + '/refCoefficients', sep=' ', mode='w', index=False, header=False)
            
        else:
             print('Please only select One Line from List')
                



    def Apply_RefCoefficients(self):

        Vert_Ref = self.VERT_REF.get()
        Vessel_F = self.VESSEL_N.get()
        Vessel = path.basename(Vessel_F)
        Vessel = re.sub(".hvf","", Vessel)
        TL_Dir = self.TL_Dir.get()
        StripTL_Dir = TL_Dir.split("/")
        TL_Dir_list = listdir(TL_Dir)
        Tracklines = [self.listbox.get(idx) for idx in self.listbox.curselection()]


        TLQuery = []
        
        for trackline in Tracklines:
            
            result = re.split(r'(20\d{2})(\d{2})(\d{2})', trackline)
            Y = int(result[1])
            M = (result[2])
            D = int(result[3])
            tlq = ('Vessel=' + Vessel + ';Day=' + JD_Conv(M,D,Y) + ';Line=' + trackline)
            TLQuery.append(tlq)

        TLTotal = len(TLQuery)
        Dirlength = len(StripTL_Dir)


        with open("ApplyRefCoe.bat", "w") as Import:
            Import.write('@ECHO OFF' + '\n')
            Import.write('@ECHO Merging and Appling Reference Coefficients' + '\n')
            Import.write('cd '+ Caris + '\n')
            Import.write('carisbatch --run GeoreferenceHIPSBathymetry --vertical-datum-reference ' + str(Vert_Ref) +
                         ' --heave-source DELAYED_HEAVE')
            Import.write(r' "file:///')
            ## Building Query to apply refreaction coefficients from the selected tracklines and trackline directory.
            j = 1
            while j < Dirlength:
                if j == Dirlength-1:
                    Import.write(StripTL_Dir[j-1] + '/' + StripTL_Dir[j-1]+'.hips?')
                else:
                    Import.write(StripTL_Dir[j-1] + '/')
                j = j + 1
            i = 1
            for line in TLQuery:
                if i != TLTotal:
                    Import.write(line + '&')
                else:
                    Import.write(line + '"' + '\n')
                i = i + 1
            Import.write('@ECHO Georeferencing Finished and Refraction Coefficients Applied to Lines:' + str(Tracklines) + '\n')
            Import.write('pause')

        p = S.check_call("ApplyRefCoe.bat", stdin=None, stdout=None, stderr=None, shell=False)



root = Tk()
root.title("Refraction GUI")
root.geometry("1000x600")
app = Application(root)
root.mainloop()
