# i wanna show a diferent way to show the [hello World]
# pip install Windows-Toasts

#-------------------------------------
# We import WindowsToaster and a toast format we want
from windows_toasts import Toast, WindowsToaster
#-------------------------------------

def greeting():
    print("\n\n Hello World, Github People \n")

    # Prepare the toaster for bread (or your notification)
    toaster = WindowsToaster('Python Services')
    # Initialise the toast
    newToast = Toast()
    # Set the body of the notification
    newToast.text_fields = ['\n\n Hello World... Github People! \n\n']

    # Activate actions
    # newToast.on_activated = lambda _: print('Toast clicked!')

    # And display it!
    toaster.show_toast(newToast)