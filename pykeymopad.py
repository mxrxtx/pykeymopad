from time import sleep
import pygame
import win32api
import win32con

# We start the necessary modules
pygame.joystick.init()
pygame.display.init()

# checks if the modules are started 
print("Joystick Module Status ==> ", pygame.joystick.get_init(),"\nDisplay Module Status ==> ", pygame.display.get_init())

# Freezes the number of joysticks connected to the system
print("Number of joysticks found ==> ", pygame.joystick.get_count())

# We introduce our chosen game handle to the system
joystick = pygame.joystick.Joystick(0)

# We take care of our work :D 
joystick.init()

#1536 axis move
#1539 Tus down
#1540 Tus up

#Key Hex Code
#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

while True:
    
    global s

    # We expect the user to do something
    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONUP:
            print(s)
     
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(0)):
            print(" /_\ down")            
            s = " /_\ up"
    
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(1)):
            print(" O down")
            s = " O up"

        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(2)):
            print(" X down")
            s = " X up"

        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(3)):
            print("  -\n |_| down")
            s = " |_| up"
       
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(4)):
            win32api.keybd_event(0x21, 0, 0, 0)                                         # page up key down  
            print(" L I down")
            win32api.keybd_event(0x21, 0, win32con.KEYEVENTF_KEYUP, 0)                  # page up key up
            s = " L I up"
     
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(5)):
            print(" R I down")
            s = " R I up"
              
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(6)):
            win32api.keybd_event(0x22, 0, 0, 0)                                         # page down key down 
            print(" L II down")
            win32api.keybd_event(0x22, 0, win32con.KEYEVENTF_KEYUP, 0)                  # page down key up
            s = " L II up"
  
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(7)):
            print(" R II down")
            s = " R II up"

        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(8)):
            pygame.quit()
            print(" Set down")
            s = " Set up"
            exit()
     
        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(10)):
            pos = win32api.GetCursorPos()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1], 0, 0)   #Mouse left key down
            print(" Sl joy down")
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1], 0, 0)     #Mouse left key up
            s = " Sl joy up"

        elif (event.type == pygame.JOYBUTTONDOWN) and ( 1 == joystick.get_button(11)):
            pos = win32api.GetCursorPos()
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN , pos[0], pos[1], 0, 0) #Mouse sag tus basildi
            print(" Sg joy down")
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP , pos[0], pos[1], 0, 0)   #Mouse sag tus birakildi
            s = " Sg joy up"
            
        # The part where we control the mouse in X Y coordinates
        elif event.type == pygame.JOYAXISMOTION:

            if joystick.get_axis(0) >= 0.00:
                durum = 0.89
                print(" X axis is increasing")
        
                while durum >= 0.89:
                    pos = win32api.GetCursorPos()
                    pos = (pos[0] + 4, pos[1] + 0)
                    win32api.SetCursorPos(pos)
                    event = pygame.event.get()    
                    durum = joystick.get_axis(0)
                    print(round(joystick.get_axis(0),1))
                    sleep(0.01)
           
            elif joystick.get_axis(0) <= -0.0078126:
                durum = -0.89
                print(" X axis decreasing")
            
                while durum <= -0.89:
                    pos = win32api.GetCursorPos()
                    pos = (pos[0] - 4, pos[1] + 0)
                    win32api.SetCursorPos(pos)
                    event = pygame.event.get()    
                    durum = joystick.get_axis(0)
                    print(round(joystick.get_axis(0),1))
                    sleep(0.01)
            
            elif joystick.get_axis(1) <= -0.0078126:
                durum = -0.89
                print(" Y axis is increasing")
      
                while durum <= -0.89:
                    pos = win32api.GetCursorPos()
                    pos = (pos[0] + 0 , pos[1] - 4)
                    win32api.SetCursorPos(pos)
                    event = pygame.event.get()    
                    durum = joystick.get_axis(1)
                    print(round(joystick.get_axis(1),1))
                    sleep(0.01)           
         
            elif joystick.get_axis(1) >= 0.00:
                durum = 0.89
                print(" Y axis decreasing")
            
                while durum >= 0.89:
                    pos = win32api.GetCursorPos()
                    pos = (pos[0] + 0 , pos[1] + 4)
                    win32api.SetCursorPos(pos)
                    event = pygame.event.get()    
                    durum = joystick.get_axis(1)
                    print(round(joystick.get_axis(1),1))
                    sleep(0.01)

       
                               
