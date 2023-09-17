#This file will be used to iniate the service, and call other needed files


import os, sys

#sys.path.append('/PythonServices/rumf')

from rumf.rumf_scrapper import getInfo


# We import WindowsToaster and a toast format we want
from windows_toasts import Toast, WindowsToaster

with open("shared/hello_world.py") as f:
    exec(f.read())

value = getInfo()

# Prepare the toaster for bread (or your notification)
toaster = WindowsToaster('Road to Ultra Countdown!')
# Initialise the toast
newToast = Toast()
# Set the body of the notification
newToast.text_fields = ['\n\n',value+' left for Road to ultra Costa Rica\n\n']

# Activate actions
newToast.on_activated = lambda _: print('Toast clicked!')

# And display it!
toaster.show_toast(newToast)