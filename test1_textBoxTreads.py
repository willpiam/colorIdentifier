"""
@date 29052018
@author willpiam

"""

import pygame 
import threading #used to thread (the ability to do mulitple things at once)
import time #used to create files specifying the sesion
from superPybrary import pybrary #download project from github, extract to colorIdentifier folder, change name from superPybrary-master to superPybrary, finally use this line.
import pygame_textinput #not mine -->https://github.com/Nearoo/pygame-text-input

class str_input_checker(threading.Thread):
    def __init__(self, screen, textbox):
        threading.Thread.__init__(self)#apparently required
        self.screen = screen
        self.textbox = textbox

    def run(self):#the code which runs        
        while True:
            self.screen.fill((225,225,225))     #fill screen with blank color
            self.events = pygame.event.get()#gets current event
            
            if (self.textbox.update(self.events) == True):# if <enter> has been pressed
                global string#string is a global variable
                string = self.textbox.get_text()#let string hold what the user has typed
                pybrary.varToFile("currentSTRING.txt", string)# an exturnal file is the most global of variables is what I like to say
                pybrary.appFile(fileName, string)
                self.textbox.clear_text()#clears text
                
            self.screen.blit(self.textbox.get_surface(), (10, 10))
            pygame.display.update()
            
            
def main():#main should only be called at the very beggining when the program is launched
    #create file called "startTime_colorImageInfo.txt" where startTime is the epoch time is seconds
    pygame.init()
    global string#global variables need to be declared before a value can be assigned
    string = ""#should be up pretty high.. must be higher than the line inputGetting.start() this varable can be edited anytime
    global fileName
    fileName = str(int(time.time()//1))+"_colorImageInfo.txt"#some reason the time isn't matching my watch but I don't really care enough to do anything about it
    pybrary.appFile(fileName, "")
    """
            RULES ON WRITING TO THIS FILE~
            1. DO NOT EDIT THE VALUE OF fileName variable
            2. ALL EDITING OF THIS FILE WILL BE HANDLED BY pybrary.appFile(fileName , "strings to be written") meaning we only append to this file
            3. WE ONLY WRITE THE FOLLOWING THINGS TO THE FILE:
                a. WHAT A USER HAS ENTERED AS THE FILE THEY WANT TO OPEN.  WE DO THIS REGARDLESS OF WHETEHR OR NOT THE FILE EXCISTS
                b. THE RGB COLOR CODE IN THE FORM 255,255,255

            DATA SHOULD SOMEWHAT RESEMBLE THE FOLLOWING:

                    aPictureName.jpg
                    225,233,255
                    100,225,170
                    adifferentPicture.png
                    100,200,255
                    255,000,000
"""
    print (fileName)
    screen = pygame.display.set_mode((640,480))
    textbox = pygame_textinput.TextInput(repeat_keys_initial_ms = 400)
    inputGetting = str_input_checker(screen, textbox)
    screen.fill((225,225,225))
    pygame.display.update()
    inputGetting.start()

    """ okay im going swiming now. So heres what to think about when I start again.

            1. were going to add the functionality to bring up a photo with the file name string
            2. where should we put this code?
            3. prob should launce a new thread from inside the str_input_checker thread which will handle loading the image into pygame and displaying it

            4. thats all you should do in the next itteration.... after that think about what comes next and start a  ew file
"""
    while True:
        if (string != ""): #if its not a completly blank string
            print (string)
            break
            
        
        
    
    
    
    
    


if __name__=="__main__":
    main()
