import pyttsx3
import os
#pyttsx3.speak("welcome in my computer")
print(" ================================================================================ ")
print("                                      Welcome")
print(" ================================================================================ ")
while True:
        print("how may i help you:" , end=' ')
        p = input()
        if("run" in p) and ("firefox" in p):
            os.system("firefox")
        elif("run" in p) and ("wmplayer" in p):
             os.system("wmplayer")
        elif("run" in p ) and ( "chrome" in p):
            os.system("chrome")
        elif( "run" in p ) and ( "notepad" in p):
            os.system("notepad")
        elif( "run" in p ) and ( "anydesk" in p):
            os.system("anydesk")
        elif( "run" in p ) and ( "skype" in p) :
            os.system("skype")
        elif( "run" in p ) and ( "teamviewer" in p):
            os.system("teamviewer")
        elif( "run" in p ) and ( "vlc" in p):
            os.system("vlc")
        elif( "run" in p ) and ( "control panel" in p):
            os.system("control panel")
        elif("run" in p) and ("slack" in p):
             os.system("slack")
        elif( "run" in p ) and ( "jupyter notebook" in p):
            try:
                os.system("jupyter notebook")
            except WindowsError:
                task()
        elif("exit"in p) or ("close"in p):
            break
        else:
            print("don't support")
 
