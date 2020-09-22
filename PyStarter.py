import os, time, psutil

def restart_process(name):
    print(name)
    if name == 'worldserver.exe':
        #Path of Files
        os.chdir('C:/Server/')
        os.startfile('worldserver.exe')
    elif name == 'authserver.exe':
        #Path of Files
        os.chdir('C:/Server/')
        os.startfile('authserver.exe')
    elif name == 'pybackup.exe':
        #Path of Files
        os.chdir('C:/Users/Administrator/Desktop/Software/PyBackup/')
        os.startfile('pybackup.exe')
    elif name == 'mysqld.exe':
        None
        os.chdir('C:/Program Files/MySQL/MySQL Server 8.0/bin/')
        os.startfile('mysqld.exe')
        

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