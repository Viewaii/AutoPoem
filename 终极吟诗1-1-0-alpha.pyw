from tkinter import *
from time import sleep
from pyautogui import *
from pyperclip import copy

def callback():
    num =      int(e1.get())
    num_poem = int(e2.get())
    num_line = int(e3.get())
    speed = int(e4.get())
    copy('作品号')
    try:
        for i in range(num_poem):
            click(1275,380)
            click(1356,382)
            hotkey('ctrl','v',duration = 1)
            typewrite(['left'])
            typewrite(str(num))
            press('enter')
            sleep(0.2)
            press('enter')
            num += 1
            sleep(num_line/speed)
    except FailSafeException:
        pass
    finally:
        e1.delete(0,END)
        e1.insert(0,str(num))
            

root = Tk()
root.title('终极吟诗-浮雲·無哀')
Label(root,text = '起始号码').grid(row = 0)
Label(root,text = '吟诗数量').grid(row = 1)
Label(root,text = '诗长').grid(row = 2)
Label(root,text = '作诗速度：行/秒').grid(row = 3)
e1 = Entry(root)
e1.grid(row = 0,column = 1,padx = 10,pady = 5)
e2 = Entry(root)
e2.grid(row = 1,column = 1,padx = 10,pady = 5)
e3 = Entry(root)
e3.grid(row = 2,column = 1,padx = 10,pady = 5)
e4 = Entry(root)
e4.grid(row = 3,column = 1,padx = 10,pady = 5)
Button(root,text = '作诗开始！',width = 15,command = callback).grid(row = 4,column = 0,sticky = W,padx = 10,pady = 5)
Button(root,text = '   退出   ',width = 15,command = root.quit).grid(row = 4,column = 1,sticky = E,padx = 10,pady = 5)
                                                               

    
mainloop()
