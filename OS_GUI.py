import tkinter
from tkinter import StringVar
from tkinter import Label
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button
# from tkinter import Canvas
# from PIL import ImageTk, Image
# import os
from FCFS import *
from SJF import *

# def resource_path(pic):
#     cwd = os.path.join(os.path.dirname(__file__))
#     path = os.path.join(cwd,pic)
#     return path

class Sys(tkinter.Frame):

    def process (self):
        p_time = []
        p_duration = []
        if (self.typeOfSchedulerComboBox.get() == 'FCFS'):
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
            FCFS (p_time, p_duration)

        elif (self.typeOfSchedulerComboBox.get() == 'Preemptive SJF'):
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
                # function name

        elif (self.typeOfSchedulerComboBox.get() == 'Non-Preemptive SJF'):
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
            non_pre_epmtive_SJF(p_time, p_duration)

        elif (self.typeOfSchedulerComboBox.get() == 'Preemptive Priority'):
            p_priority = []
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == '' or self.processPriority[x].get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
                    p_priority.append(int(self.processPriority[x].get()))
                # function name

        elif (self.typeOfSchedulerComboBox.get() == 'Non-Preemptive Priority'):
            p_priority = []
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == '' or self.processPriority[x].get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
                    p_priority.append(int(self.processPriority[x].get()))
                # function name

        elif (self.typeOfSchedulerComboBox.get() == 'Round Robin'):
            for x in self.processTime:
                if (self.processTime[x].get() == '' or self.processDuration[x].get() == '' or self.quantumTime.get() == ''):
                    messagebox.showerror('Error', 'Please fill the empty entry')
                    return False
                else:
                    p_time.append(float(self.processTime[x].get()))
                    p_duration.append(float(self.processDuration[x].get()))
                # function name
        

    def generate (self):
        if (self.numberOfProcessEntry.get() != ''):
            if (self.clear != 0):
                for x in range(1, self.clear + 1):
                    self.parent.children['lFirst' + str(x)].place_forget()
                    self.parent.children['eFirst' + str(x)].place_forget()
                    self.parent.children['lSecond' + str(x)].place_forget()
                    self.parent.children['eSecond' + str(x)].place_forget()
                    if (self.clearType == 'Preemptive Priority' or self.clearType == 'Non-Preemptive Priority'):
                        self.parent.children['lThird' + str(x)].place_forget()
                        self.parent.children['eThird' + str(x)].place_forget()
                    elif (self.clearType == 'Round Robin'):
                        self.labelQuantum.place_forget()
                        self.entryQuantum.place_forget()
                self.bt.place_forget()
            if (self.typeOfSchedulerComboBox.get() == 'FCFS'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.processTime = {}
                self.processDuration = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.71, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
            elif (self.typeOfSchedulerComboBox.get() == 'Preemptive SJF'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.processTime = {}
                self.processDuration = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.71, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
            elif (self.typeOfSchedulerComboBox.get() == 'Non-Preemptive SJF'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.processTime = {}
                self.processDuration = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.71, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
            elif (self.typeOfSchedulerComboBox.get() == 'Preemptive Priority'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.processTime = {}
                self.processDuration = {}
                self.processPriority = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.processPriority[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.378, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.57, rely = r_entry)
                    self.l3 = Label(self.parent, text = "Process " + str(i) + " priority:", font = ("Cambria", 12), name = 'lThird{}'.format(i))
                    self.l3.place(relx = 0.748, rely = r_label)
                    self.entry3 = Entry(self.parent, textvariable = self.processPriority[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eThird{}'.format(i))
                    self.entry3['validatecommand'] = (self.entry3.register(self.testVal), '%P', '%d')
                    self.entry3.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
            elif (self.typeOfSchedulerComboBox.get() == 'Non-Preemptive Priority'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.processTime = {}
                self.processDuration = {}
                self.processPriority = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.processPriority[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.378, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.57, rely = r_entry)
                    self.l3 = Label(self.parent, text = "Process " + str(i) + " priority:", font = ("Cambria", 12), name = 'lThird{}'.format(i))
                    self.l3.place(relx = 0.748, rely = r_label)
                    self.entry3 = Entry(self.parent, textvariable = self.processPriority[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eThird{}'.format(i))
                    self.entry3['validatecommand'] = (self.entry3.register(self.testVal), '%P', '%d')
                    self.entry3.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
            elif (self.typeOfSchedulerComboBox.get() == 'Round Robin'):
                i = 1
                r_label = 0.23
                r_entry = 0.233
                self.clear = int(self.numberOfProcessEntry.get())
                self.clearType = self.typeOfSchedulerComboBox.get()
                #self.entries = {}
                self.quantumTime = StringVar()
                self.processTime = {}
                self.processDuration = {}
                while(i <= int(self.numberOfProcessEntry.get())):
                    self.processTime[i] = StringVar()
                    self.processDuration[i] = StringVar()
                    self.l1 = Label(self.parent, text = "Process " + str(i) + " arrival time:", font = ("Cambria", 12), name = 'lFirst{}'.format(i))
                    self.l1.place(relx = 0.04, rely = r_label)
                    self.entry1 = Entry(self.parent, textvariable = self.processTime[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eFirst{}'.format(i))
                    self.entry1['validatecommand'] = (self.entry1.register(self.testFloat), '%P', '%d')
                    self.entry1.place(relx = 0.223, rely = r_entry)
                    self.l2 = Label(self.parent, text = "Process " + str(i) + " execute time:", font = ("Cambria", 12), name = 'lSecond{}'.format(i))
                    self.l2.place(relx = 0.71, rely = r_label)
                    self.entry2 = Entry(self.parent, textvariable = self.processDuration[i], validate = "key", width = 5, font = ("Cambria", 12), name = 'eSecond{}'.format(i))
                    self.entry2['validatecommand'] = (self.entry2.register(self.testFloat1), '%P', '%d')
                    self.entry2.place(relx = 0.9, rely = r_entry)
                    i += 1
                    r_label += 0.05
                    r_entry += 0.05
                self.labelQuantum = Label(self.parent, text = "Quantum Time:", font = ("Cambria", 12))
                self.labelQuantum.place(relx = 0.417, rely = r_label)
                self.entryQuantum = Entry(self.parent, textvariable = self.quantumTime, validate = "key", width = 5, font = ("Cambria", 12))
                self.entryQuantum['validatecommand'] = (self.entry2.register(self.testFloat), '%P', '%d')
                self.entryQuantum.place(relx = 0.543, rely = r_entry)
                r_label += 0.05
                r_entry += 0.05
                self.bt = Button(self.parent, text = "Visualize processes", font = ("Times New Roman", 16), width = 25, bg = "#7bd45d", command = self.process)
                self.bt.place(relx = 0.33, rely = r_label)
        else:
            messagebox.showerror('Error', 'Please enter the number of processes')
            return False

    def testVal (self,inStr,acttyp):
        if (acttyp == '1'):
            try:
                if (isinstance(int(inStr), int)):
                    1
            except:
                return False
        return True

    def testVal1 (self,inStr,acttyp):
        if(acttyp == '1'):
            try:
                if (inStr.count('0') == len(inStr)):
                    return False
                if (isinstance(int(inStr), int)):
                    1
            except:
                return False
        return True
        
    def testFloat (self,inStr,acttyp):
        if(acttyp == '1'):
            try:
                if (isinstance(float(inStr), float)):
                    1
            except:
                return False
        return True

    def testFloat1 (self,inStr,acttyp):
        if(acttyp == '1'):
            try:
                if (inStr.count('0') == len(inStr)):
                    return False
                if (isinstance(float(inStr), float)):
                    1
            except:
                return False
        return True

    def __init__ (self, parent):

        tkinter.Frame.__init__ (self, parent)

        self.parent = parent

        self.numberOfInputs = StringVar()
        self.clear = 0
        self.clearType = ""

        # path = resource_path('pic.png')
        # self.load = Image.open(path)
        # self.img = ImageTk.PhotoImage(self.load)
        # self.background = Canvas(self.parent, height = 700, width = 885)
        # self.background.place(x = 0, y = 0)
        # self.background.create_image(0, 0, image = self.img, anchor = "nw")
        # self.background.create_text( 200, 250, text = "Welcome")

        self.title = Label(self.parent, text = "The OS Scheduler", font = ("Times New Roman Bold", 30))
        self.title.place(relx = 0.35, rely = 0.01)

        self.typeOfScheduler = Label(self.parent, text = "Type of Scheduler:", font = ("Times New Roman", 18))
        self.typeOfScheduler.place(relx = 0.005, rely = 0.1)
        typeOfSchedulerComboBoxFont = ("Times New Roman", 13)
        self.typeOfSchedulerComboBox = Combobox(self.parent, values = ["FCFS", "Preemptive SJF", "Non-Preemptive SJF", "Preemptive Priority", "Non-Preemptive Priority", "Round Robin"], width = 20, state = 'readonly', font = typeOfSchedulerComboBoxFont)
        self.option_add('*TCombobox*Listbox.font', typeOfSchedulerComboBoxFont)
        self.typeOfSchedulerComboBox.place(relx = 0.22, rely = 0.109)
        self.typeOfSchedulerComboBox.current(0)

        self.numberOfProcess = Label(self.parent, text = "Number of processes:", font = ("Times New Roman", 18))
        self.numberOfProcess.place(relx = 0.677, rely = 0.1)
        self.numberOfProcessEntry = Entry(self.parent, textvariable=self.numberOfInputs, width = 5, validate = "key", font = ("Times New Roman", 16))
        self.numberOfProcessEntry['validatecommand'] = (self.numberOfProcessEntry.register(self.testVal1), '%P', '%d')
        self.numberOfProcessEntry.place(height = 32, relx = 0.922, rely = 0.1)

        self.generateButton = Button(self.parent, text = "Generate", font = ("Times New Roman", 16), bg = "lightgreen", command = self.generate)
        self.generateButton.place(relx = 0.464, rely = 0.17)


def main():
    window = tkinter.Tk()
    window.withdraw()
    window.title("The Scheduler")
    window.geometry('885x700+225+0')
    window.resizable(0, 0)
    Sys(window).place(relx=1, rely=1)
    window.deiconify()
    window.mainloop()

if __name__ == "__main__":
    main()