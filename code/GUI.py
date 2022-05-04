import tkinter as tk
from tkinter import ttk
from tkinter import IntVar, StringVar
import csv
from PIL import ImageTk, Image
from yearHandler import yearHandler
from database import Datenbank

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1100x1000")
        self.title("Mosiak Inventur Datenbank Leonard")
        self.left_frame=self.make_left_frame()
        self.right_frame=self.make_right_frame()
        self.month_checkboxes=[]
        self.series_checkbox=[]
        self.garbage=[]
        self.yearHandler=yearHandler()
        self.database=Datenbank()
        self.make_year_component()
        self.make_month_component()
        self.make_serien_component()
        self.make_searchbar()

    def make_right_frame(self):
        right_frame=ttk.Frame(self,borderwidth="4", relief="sunken")
        right_frame.grid(column=1,row=0,sticky=tk.NSEW)
        return right_frame

    def make_left_frame(self):
        left_frame=ttk.Frame(self,borderwidth="4", relief="sunken")
        left_frame.grid(column=0, row=0, sticky=tk.NSEW)
        return left_frame

    def change(self, option):
        if option=="add":
            self.yearHandler.handle_add(self.input_value.get())
        else:
            self.yearHandler.handle_delete(self.input_value.get())
        self.years_variable.set(self.yearHandler.get_years_formated())

    def get_formated_years(self):
        temp=self.yearHandler.get_years_formated()
        text=""
        for i in temp:
            text=text+i
        print("text: ",text)
        return text

    def make_year_component(self):
        self.year_frame=ttk.Frame(self.right_frame)
        self.year_frame.grid(column=0,row=1,sticky=tk.W)
        ttk.Label(self.year_frame, text="Liste der Jahre").grid(column=0 , row=0, sticky=tk.W)
        self.years_variable = StringVar()
        self.years_variable.set(self.get_formated_years())
        display_years=ttk.Label(self.year_frame, textvariable = self.years_variable)
        display_years.grid(column=0, row=1, columnspan=2, sticky= tk.NSEW)
        self.input_value= StringVar()
        input=ttk.Entry(self.year_frame,textvariable=self.input_value)
        input.grid(column=0,row=2,columnspan=2,sticky=tk.NSEW)
        add=ttk.Button(self.year_frame,text="Hinzufügen",command=lambda:self.change("add"))
        add.grid(column=0,row=3,sticky=tk.NSEW)
        delete=ttk.Button(self.year_frame,text="Löschen", command=lambda:self.change("delete"))
        delete.grid(column=1,row=3,sticky=tk.NSEW)
        ttk.Label(self.year_frame).grid(column=0, row=4)
        ttk.Label(self.year_frame).grid(column=0, row=5)

    def check_format(self, value):
        value=str(value).strip()
        if  len(value)==9:
            value.split(0,5)
            return 0
        elif len(value)==4:
            return 1
        else:
            print("Falsches Format")
            return 2

    def make_month_component(self):
        months=["Januar","Feburar", "März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
        month_frame=ttk.Frame(self.right_frame)
        month_frame.grid(column=0,row=0,sticky=tk.W)
        ttk.Label(month_frame, text="Monate", anchor="center").grid(column=0, row=0, columnspan=2, sticky=tk.W)
        for x,month in enumerate (months): 
            var = IntVar()
            var.set(1)
            if x % 2==0:
                ttk.Checkbutton(month_frame,text=month, variable=var).grid(column=0,row=x+1,sticky=tk.W)
            else:
                ttk.Checkbutton(month_frame,text=month, variable=var).grid(column=1,row=x,sticky=tk.W)
            self.month_checkboxes.append(var)
        ttk.Label(month_frame).grid(column=0,row=13)
        ttk.Label(month_frame).grid(column=0,row=14)

    def get_variable_values(self, array):
        for var in array:
            print(var.get())

    def make_serien_component(self):
        serien_frame=ttk.Frame(self.right_frame)
        serien_frame.grid(column=0,row=2, sticky=tk.W)
        ttk.Label(serien_frame, text="Serien", anchor="center").grid(column=0, row=0, columnspan=2, sticky=tk.W)
        with open('Daten/serien_namen.csv', newline='', encoding="utf8") as csvfile:
            serien = csv.reader(csvfile)
            for x,serie in enumerate (serien):
                var = IntVar()
                var.set(1)
                if x % 2==0:
                    ttk.Checkbutton(serien_frame,text=serie[0],variable=var).grid(column=0,row=x+1,sticky=tk.W)
                else:
                    ttk.Checkbutton(serien_frame,text=serie[0],variable=var).grid(column=1,row=x,sticky=tk.W)
                self.series_checkbox.append(var)

    def load_image(self):
        try:
            img = ImageTk.PhotoImage(Image.open("Source/mosaik.jpg").resize((160, 100)))
            return img
        except:
            print("Bild nicht geladen")
            return None

    def make_searchbar(self):
        frame=ttk.Frame(self.left_frame, borderwidth="4", relief="sunken")
        frame.grid(column=0,row=0)
        self.searchbar_entry=StringVar()
        self.searchbar=ttk.Entry(frame, width=100,textvariable=self.searchbar_entry)
        suchen_button=ttk.Button(frame, text="Suchen", command=lambda:self.display_hefte())
        suchen_button.grid(column=1, row=1, sticky=tk.NSEW)
        logo_title_frame=ttk.Frame(frame)
        logo_title_frame.grid(column=0, row=0, sticky=tk.W)
        img=self.load_image()
        if img!=None:
            logo=ttk.Label(logo_title_frame,image=img)
            logo.image=img
            logo.grid(column=0, row=0, sticky=tk.W)
            self.garbage.append(logo)
            self.searchbar.grid(column=0, row=1, sticky=tk.NSEW)
            ttk.Label(logo_title_frame,text="MOSAIK DATENBANK VON LEOANRD").grid(column=1, row=0, columnspan=5, sticky=tk.E)
        else:
            self.searchbar.grid(column=0, row=0, sticky=tk.NSEW)
    
    def get_checkbox_values(self,array):
        boolean_values=[]
        for checkbox in array:
            boolean_values.append(checkbox.get())
        return boolean_values

    def display_hefte(self):
        alle_hefte=ttk.Frame(self.left_frame, borderwidth="4", relief="sunken")
        alle_hefte.grid(column=0,row=1,sticky=tk.W)
        #Todo: Was wenn Input keine ID ist? 
        #Was wenn Input ein Titel ist?
        #Was tuen wenn Input eine Serie ist?
        if self.searchbar_entry.get()!="" and self.searchbar_entry.get()!="Suchen...":
            found=self.database.get_heft_by_id(self.searchbar_entry.get())
            if found!=None:
                self.render_heft(alle_hefte,self.database.get_heft_by_id(self.searchbar_entry.get()),0)
            else: 
                ttk.Label(alle_hefte,text="Kein Ergebnis gefunden").grid(column=0,row=0,sticky=tk.W)
        else:
            temp1=self.get_checkbox_values(self.month_checkboxes)
            temp2=self.get_checkbox_values(self.series_checkbox)
            temp3=self.yearHandler.get_years_formated()
            daten=self.database.handle_request(temp1,temp2,temp3)
            if daten!=None and daten!=[]:
                for i,mosaik in enumerate(daten):
                    self.render_heft(alle_hefte,mosaik,i)
            else:
                ttk.Label(alle_hefte,text="Kein Ergebnis gefunden").grid(column=0, row=0, sticky=tk.W)
    
    def render_heft(self,alle_hefte,info,index):
        heft=ttk.Frame(alle_hefte, borderwidth="4", relief="sunken")
        heft.grid(column=0,row=index,sticky=tk.W)
        img=self.load_image()
        cover=ttk.Label(heft,image=img)
        cover.image=img
        cover.grid(column=0, row=0,sticky=tk.W)
        text_frame=ttk.Frame(heft)
        text_frame.grid(column=1,row=0,sticky=tk.W)
        ttk.Label(text_frame,text="Mosaik Nummer:"+str(info[0])+",").grid(column=0,row=0,sticky=tk.W)
        ttk.Label(text_frame,text=str(info[1])).grid(column=1,row=0,sticky=tk.W)
        ttk.Label(text_frame,text=" - "+str(info[3])+" "+str(info[2])).grid(column=2,row=0,sticky=tk.W)

app=App()
app.mainloop()
