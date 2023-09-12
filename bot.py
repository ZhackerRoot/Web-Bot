from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pag
import pyfiglet as pf

# Directory my file Pwd
driver = webdriver.Chrome(executable_path="C:/Users/Zhacker/Desktop/Test/chromedriver.exe")
# Starting webdirver > find web elements
try:
    text = pf.print_figlet(text='\nZhac4er', colors='green')
    print()
    print("Created By: Zhac4er" + '\n' 'Social media me: Instagram : Zhac4er, Youtube : Zhac4er, Github : ZhackerRoot')
    #file = input('File name: ')
    #with open(f'C:/Users/Zhacker/Desktop/Test/file/{file}.txt', 'r')as files:
     #   while len(files.read()) > inx:
            # file add to databe until greater then inx value 
    inx = -1
    while True:
       inx += 1
       driver.get('https://5tashabbus.uz')
       driver.maximize_window()
       time.sleep(5)
       pag.leftClick(x=1350, y=600)
       time.sleep(2)
       select = driver.find_element(By.XPATH, '//*[@id="__BVID__26___BV_modal_body_"]/div[2]/div/div/div/input').click()
       time.sleep(3)
       number = driver.find_element(By.XPATH, '//*[@id="__BVID__26___BV_modal_body_"]/div[2]/div/div/div/input').send_keys('901940306')
       time.sleep(3)
       print('Wating sms massage.........')
       button = driver.find_element(By.XPATH, '//*[@id="__BVID__26___BV_modal_body_"]/div[3]/div[2]/div/button').click()
       time.sleep(3)
       sms_msg = input('Enter a sms: ')
       sms = driver.find_element(By.XPATH, '//*[@id="__BVID__26___BV_modal_body_"]/div[3]/div[2]/div/div/div/input').send_keys(sms_msg)
       time.sleep(8)
       button = driver.find_element(By.XPATH, '//*[@id="__BVID__26___BV_modal_body_"]/div[3]/div[3]/div/button').click()
       # I'm using Pyauto Gui because some button xpath unable found
       time.sleep(5)
       pag.leftClick(x=655, y=282)
       pag.leftClick(x=603, y=369)
       time.sleep(3)
       # file handling 
       with open('C:/Users/Zhacker/Desktop/Test/file/serial.txt', 'r') as file:
          
           lst = []
           for x in file.read().split():
               lst.append(x)
              
           select = driver.find_element(By.XPATH, '//*[@id="__BVID__27___BV_modal_body_"]/div[2]/div/div/div/div/div[1]/div[2]/div/div/input').send_keys(lst[inx]) # past index 
       
       with open('C:/Users/Zhacker/Desktop/Test/file/digits.txt', 'r') as file:
           
           ls = []
           for i in file.read().split():
               ls.append(i)
               
           select = driver.find_element(By.XPATH, '//*[@id="__BVID__27___BV_modal_body_"]/div[2]/div/div/div/div/div[1]/div[3]/div/div/input').send_keys(ls[inx]) # past index
       
       with open('C:\\Users\\Zhacker\\Desktop\\Test\\file\\date_b.txt', 'r') as file:
           
           l = []
           for w in file.read().split():
               l.append(w)
    
           select = driver.find_element(By.XPATH, '//*[@id="__BVID__27___BV_modal_body_"]/div[2]/div/div/div/div/div[1]/div[4]/div/div[1]/div/input').send_keys(l[inx]) # past index
       
       button = driver.find_element(By.XPATH, '//*[@id="__BVID__27___BV_modal_body_"]/div[2]/div/div/div/div/div[1]/div[6]/button/p').click()
       time.sleep(3)
       select = driver.find_element(By.XPATH, '//*[@id="vs8__combobox"]/div[1]/input').click()
       pag.press('enter')
   
       select = driver.find_element(By.XPATH, '//*[@id="vs9__combobox"]/div[1]/input').click()
       select = driver.find_element(By.XPATH, '//*[@id="vs9__combobox"]/div[1]/input').send_keys('Samarqand viloyati')
       pag.press('enter')
       time.sleep(3)
       select = driver.find_element(By.XPATH, '//*[@id="vs10__combobox"]/div[1]/input').click()
       select = driver.find_element(By.XPATH, '//*[@id="vs10__combobox"]/div[1]/input').send_keys('sha')
       time.sleep(2)
       pag.press('enter')
       time.sleep(5)
       pag.leftClick(x=1057,y=705)
       pag.typewrite('17892')
       time.sleep(3)
       pag.press('enter')
   
       select = driver.find_element(By.XPATH, '//*[@id="vs11__combobox"]/div[1]/input').click()
       pag.press('enter')
   
       select = driver.find_element(By.XPATH, '//*[@id="vs12__combobox"]/div[1]/input').click()
       time.sleep(3)
       pag.press('enter')
       time.sleep(3)
       button = driver.find_element(By.XPATH, '//*[@id="__BVID__27___BV_modal_body_"]/div[2]/div/div/div/div/div[4]/div/button').click()
    
    
except Exception as ex: 
    print(ex)
    print('Bu yoshdagi Shaxs malumotlari yuborib bulmaydi? yoki internet tezligingiz Botning talabiga javob bermaydi')
finally:
    print(f'Sizda {inx} ta Shaxs qabul qilindi !!')
    driver.quit()
    driver.close()


