import os, sys

# import the methods from other files 
from rtu_scrapper import getInfo

# We import WindowsToaster and a toast format we want
from windows_toasts import Toast, WindowsToaster, InteractableWindowsToaster, ToastActivatedEventArgs, ToastButton

def main():
    # "open" method for a file
    with open("hello_world.py") as f:
        exec(f.read())

    value = getInfo()

    # Prepare the toaster for bread (or your notification)
    toaster =  InteractableWindowsToaster('Road to Ultra Countdown!')

    # Initialise the toast
    newToast = Toast()
    
    # Set the body of the notification
    newToast.text_fields = ['\n\n',value+' left for Road to ultra Costa Rica\n\n']
    toaster.AddAction(ToastButton('Lets Celebrate!', 'response=celebrate'))
    # Activate actions
    # newToast.on_activated = lambda _: print('Toast clicked!')

    # And display it!

    toaster.show_toast(newToast)
    # IMPORTANT!!!!!!!!
    # Search if its possible to make last more time o when the user click on the toast
    

if __name__ == "__main__":
        main()
