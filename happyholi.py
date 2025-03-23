# pip install pyfiglet
# pip install colorama
from colorama import Fore 
import pyfiglet

font = pyfiglet.figlet_format('Happy Holi')
print (Fore.MAGENTA+font)
