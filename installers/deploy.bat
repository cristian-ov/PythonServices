
:: Verificar el tipo de sistema 64 o 32 y si el sistema es windows y no linux
:: Puede implementarse para linux despues

:: agregar .exe de python
python-3.11.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 

pip install selenium
pip install webdriver-manager
pip install beautifulsoup4 
pip install pandas