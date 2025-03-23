import pywhatkit
from datetime import datetime
 
# using Exception Handling to avoid 
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+918408833293", 
                        "Hello!", 
                        datetime.now().hour, datetime.now().minute + 2)
  print("Successfully Sent!")
 
except:
  print("An Unexpected Error!")