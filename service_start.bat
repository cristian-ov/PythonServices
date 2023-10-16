:: the idea is to iniciate the main.py as a service with this script.


SCHTASKS /CREATE /SC DAILY /TN "PythonTask\RTU" /TR "C:\Users\crist\OneDrive\Documentos\GitHub\PythonServices\rtu_service\main.py" /ST 09:00