from datetime import date
import socket
today=date.today()
b=socket.gethostname()
a=today.strftime("%d/%m/%Y")
print("Hello World! I am running on {} and today date is {}".format(b,a))
