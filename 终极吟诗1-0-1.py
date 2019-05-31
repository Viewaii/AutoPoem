from time import *
from pyautogui import *

a = int(input("请输入作品号码 "))
input('按回车开始吟诗')
click(917,183)
b = input('按回车保存，按“kill”退出 ')
while True:
          if b == 'kill':
              break  
          click(1027,185)
          typewrite(['z','u','o','p','1'])
          typewrite(str(a))
          typewrite(['h','a','o','1'])
          press('enter')
          sleep(0.2)
          press('enter')
          a += 1
          click(917,183)
          moveTo(296,686)
          b = input()
          sleep(0.1)
          moveTo(247,755,duration = 0.1)
          #click(296,686)
          #click()
         # click()
print('下一次输入',a)          
input()
