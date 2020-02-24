import time
from selenium import webdriver
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

configur = ConfigParser() 
configur.read('config.ini')

print ("Loging Your Information.")
URL = configur.get('Login','Product_URL')
Uname = configur.get('Login','Username')
Pass = configur.get('Login','password')
Name = configur.get('Login','Name')
Mob = configur.get('Login','Mobile')
Loc = configur.get('Login','Locality')
Add = configur.get('Login','Address')
pin = configur.get('Login','Pincode')
print ("Information Load Successfully.")
print ("Product Purchasing Process Start.")

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get("https://www.flipkart.com");
time.sleep(1)

Uname = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(Uname)
Pass = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(Pass)
time.sleep(2)
Btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
time.sleep(1)
driver.get(URL);

while True:
    try:
        Buy = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div/div/div[2]/div/ul/li[2]/form/button").click()
        break
    except:
        driver.get(URL);
        time.sleep(3)
        driver.refresh()
        
time.sleep(2)
Find_New_Adds = driver.find_elements_by_class_name("_2Y8lQ1")
for New_Add in Find_New_Adds:
    New_Add.click()

time.sleep(1)

Find_Inputs = driver.find_elements_by_class_name("_16qL6K")

Find_Inputs[0].send_keys(Name)
Find_Inputs[1].send_keys(Mob)
Find_Inputs[2].send_keys(pin)
Find_Inputs[3].send_keys(Loc)
Find_Inputs[4].send_keys(Add)
Add_type = driver.find_elements_by_class_name('_6ATDKp')
Add_type[4].click()
Sub_Add = driver.find_elements_by_class_name('_2AkmmA')
Sub_Add[1].click()

time.sleep(2)

Confirm = driver.find_elements_by_class_name('_2AkmmA')
driver.execute_script("arguments[0].click();", Confirm[0])

time.sleep(4)
COD = driver.find_elements_by_class_name('_6ATDKp')
COD[9].click()

#driver.quit()
#driver.close()

print ("Product Purchase Process Completed.")
print ("Please verify Your Order.")
