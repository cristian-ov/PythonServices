#-------------------------------------
# Importing the system module
import sys

# Importing the subprocess module
import subprocess

# Importing the os module
import os

# Importing importlib.util module
import importlib.util
#-------------------------------------

def check_package(name):
    #opening the module list 
    lib_list = os.popen('pip list')
    print(lib_list)

    #storing the list of pip modules 
    pack_list = lib_list.read()
    print(pack_list)

    #formatting of the list
    Detpack=list(pack_list.split(" "))
    print(Detpack)

    #code to check if the library exists
    if(any(name in i for i in Detpack)):
        # Displaying that the module is found with Os Module
        print("Yay! The '",name,"' Module is Installed")

    elif (spec := importlib.util.find_spec(name)) is not None:
        # Displaying that the module is found Importlib.Util And Sys Modules
        print("\n'",name,"' already in sys.modules \n")

    else:
        print("\n Can't find the '", name, "' module \n\n Installing packages libraries for '",name,"' ...")
        # Implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def check():
    print("\n\n Checking packages!, Please wait...\n\n")
    check_package("webdriver-manager")
    check_package("selenium")
    check_package("beautifulsoup4")
    check_package("scheduler")
    print("\n\nChecking Complete!...\n\n")


