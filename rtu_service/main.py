#-------------------------------------
import os, sys

# Import the modules from other files 
from rtu_scrapper import getInfo
from package_checker import check
from hello_world import greeting

# We import WindowsToaster and a toast format we want
from windows_toasts import AudioSource, Toast, ToastAudio, WindowsToaster, InteractableWindowsToaster, ToastActivatedEventArgs, ToastButton
#-------------------------------------

def main():
    # Calls a module that check the external libraries
    check()

    # Calls a module that print a greeting
    greeting()
    

    # Gets the data from the rtu_scrapper module "getInfo()"
    value = getInfo()

    # Prepare the toaster for bread (or your notification)
    toaster =  InteractableWindowsToaster('Road to Ultra Countdown ⏱️🔊🎧🎶🔝🇨🇷')

    # Initialise the toast
    newToast = Toast()
    
    # Set the body of the notification
    newToast.text_fields = ['🥳✨🎆🎶',value+' left for... \n¡Road to ultra Costa Rica! ✨🎆🎶🇨🇷🥳\n\n']
    #newToast.AddAction(ToastButton('Lets Celebrate!🎉', 'response=celebrate'))

    # Activate actions
    # newToast.on_activated = lambda _: print('Toast clicked!')
    newToast.launch_action = 'https://costarica.roadtoultra.com'
    newToast.audio = ToastAudio(AudioSource.IM, looping=True)
    # And display it!

    toaster.show_toast(newToast)
    # IMPORTANT!!!!!!!!
    # Search if its possible to make last more time o when the user click on the toast
    

if __name__ == "__main__":
        main()
