# This script check the conection to internet
#https://www.youtube.com/watch?v=mVfm74YHEVQ
#https://windows-toasts.readthedocs.io/en/latest/advanced_usage.html
#-------------------------------------
import requests
#-------------------------------------
def check_connection(url):
    # REVISAR SI SE PUEDE USAR EL TIEMPO DE ESPERA COMO VALIDACION EN CASO DE INTERNET LENTO
    try:
        request = requests.get(url, timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        return False
    else:
        return True