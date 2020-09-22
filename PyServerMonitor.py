#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from tkinter import *
import tkinter as tk

import psutil, subprocess, os, time


def OutputAnything():
    print('Working')

class MainGui:

    def server_settings_window(self):
        print('Starte Window')
        self.window_rawDat_functions = tk.Toplevel(self.root)
        self.window_rawDat_functions.focus_set()
        self.window_rawDat_functions.grab_set()
        self.window_rawDat_functions.maxsize(400,400)
        self.window_rawDat_functions.minsize(400,400)

        self.textArea_frame = tk.Frame(master=self.window_rawDat_functions)

        self.textArea_frame.grid(row=0, column=0)

    def __init__(self):
        # Neues Window erstellen
        self.root = Tk()

        # Erstelle Application mit Einstellungen
        self.menu = Menu(self.root)
        self.root.title('Test')
        #Adde Icon later
        #root.iconbitmap('Path')
        self.root.geometry("375x125")
        self.root.resizable(False, False)

        # Setze Hintergrund und Menue
        self.root.config(bg='white', menu=self.menu)

        # Erstelle neues filemenu zum Menu tearoff = false damit Separator wegfaellt
        self.server_menu = Menu(self.menu, tearoff=False)
        self.world_menu = Menu(self.menu, tearoff=False)
        self.auth_menu = Menu(self.menu, tearoff=False)
        self.pybackup_menu = Menu(self.menu, tearoff=False)
        self.help_menu = Menu(self.menu, tearoff=False)

        # Fuege Menupunkte hinzu
        self.menu.add_cascade(label='Server', menu=self.server_menu)
        self.menu.add_cascade(label='World', menu=self.world_menu)
        self.menu.add_cascade(label='Auth', menu=self.auth_menu)
        self.menu.add_cascade(label='Backup', menu=self.pybackup_menu)
        self.menu.add_cascade(label='Hilfe', menu=self.help_menu)

        # Erstelle neuen Unterpunkt zu Obermenues
        self.server_menu.add_command(label='Verbindungsinfos', command=OutputAnything)
        self.server_menu.add_command(label='Platzhalter', command=OutputAnything)

        self.world_menu.add_command(label='Konfiguration')

        self.auth_menu.add_command(label='Konfiguration')
        self.auth_menu.add_command(label='Realm anlegen')

        self.pybackup_menu.add_command(label='Konfiguration')

        self.help_menu.add_command(label='How to...? FAQ', command=OutputAnything)
        self.help_menu.add_command(label='Version', command=OutputAnything)
        self.help_menu.add_command(label='�ber', command=OutputAnything)

        # Hier beginnt das Gui
        ####################################################################
        # Service_Status Gruppenframe erstellen
        self.status_frame = LabelFrame(self.root, text='Service Status: ', bg='white', padx=15, pady=5)

        # Widgets in Frame hinzuf�gen
        self.label_db = Label(self.status_frame, text='Service running...', bg='white', fg='red')
        self.label_py = Label(self.status_frame, text='Service running...', bg='white', fg='green')
        self.label_wo = Label(self.status_frame, text='Service running...', bg='white')
        self.label_au = Label(self.status_frame, text='Service running...', bg='white')

        self.label_db.grid(row=0, column=0)
        self.label_py.grid(row=1, column=0)
        self.label_wo.grid(row=2, column=0)
        self.label_au.grid(row=3, column=0)

        # Widgets in status_frame verpacken und zum GUI hinzuf�gen
        self.status_frame.grid(row=0, column=0, padx=5, pady=5)

        ####################################################################
        # Service_Starter Gruppenframe erstellen
        self.starter_frame = LabelFrame(self.root, text='Service Starter: ', bg='white', padx=20, pady=5)

        # Widgets in Frame hinzuf�gen
        self.button_db = Button(self.starter_frame, text='Start Server', bg='white', width=10, command=self.server_settings_window)
        self.button_py = Button(self.starter_frame, text='Start Backup', bg='white', width=10)
        self.button_wo = Button(self.starter_frame, text='Start MySQL', bg='white', width=10)

        self.button_db_stop = Button(self.starter_frame, text='Stop Server', bg='white', width=10)
        self.button_py_stop = Button(self.starter_frame, text='Stop Backup', bg='white', width=10)
        self.button_wo_stop = Button(self.starter_frame, text='Stop MySQL', bg='white', width=10)

        self.button_db.grid(row=0, column=0, padx=2, pady=1)
        self.button_py.grid(row=1, column=0, padx=2, pady=1)
        self.button_wo.grid(row=2, column=0, padx=2, pady=1)

        self.button_db_stop.grid(row=0, column=1, padx=2, pady=1)
        self.button_py_stop.grid(row=1, column=1, padx=2, pady=1)
        self.button_wo_stop.grid(row=2, column=1, padx=2, pady=1)

        # Widgets in Frame verpacken und zum GUI hinzuf�gen
        self.starter_frame.grid(row=0, column=1, padx=5, pady=5)

        self.status_frame.grid_propagate(1)
        self.starter_frame.grid_propagate(1)

        # Mainloop um das Fensterchen am Laufen zu halten
        self.root.mainloop()

"""
    class StarterTest:     
        def restart_process(name):
            print(name)
            if name == 'worldserver.exe':
                #Path of Files
                os.chdir('C:/Users/Admin/Desktop/WoW_Server/Server/')
                os.startfile('worldserver.exe')
            elif name == 'authserver.exe':
                #Path of Files
                os.chdir('C:/Users/Admin/Desktop/WoW_Server/Server/')
                os.startfile('authserver.exe')
            elif name == 'pybackup.exe':
                None
                #Path of Files
                #os.chdir('C:/Users/Admin/Desktop/WoW_Server/Server/')
                #os.startfile('pybackup.exe')
            elif name == 'mysqld.exe':
                None
                #Path of Files
                #os.chdir('C:/Users/Admin/Desktop/WoW_Server/Server/')
                #os.startfile('mysqld.exe')
                

                #subprocess.Popen(r'"C:/Users/Admin/Desktop/WoW_Server/Server/worldserver.exe"', shell=False)

        def check_process():
            check_proc_list = ('worldserver.exe', 'authserver.exe', 'pybackup.exe', 'mysqld.exe')
            process_list = []

            # Speichere Prozesse in Array aus anderer Funk und echeke in andere dann die prozesse die gecheckt werden m�ssen

            for running_procs in psutil.process_iter():
                try:
                    process_list.append(running_procs.name().lower())
                except:
                    continue

            for restart_procs in check_proc_list :
                print('Searching for Process "%s" by name.' % (restart_procs))
                if restart_procs in process_list:
                    print('%s running!' % (restart_procs))
                else:
                    print('%s not found...\nRestarting %s!' % (restart_procs, restart_procs))
                    restart_process(restart_procs)


        # Starte Programm in Loop
        while True == True:
            try:
                check_process()
            except:
                print('Could not open all process..')
            time.sleep(1)

        test = StarterTest()
        test.check_process()
"""


root = MainGui()

