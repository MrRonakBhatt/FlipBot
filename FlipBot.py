import time
from selenium import webdriver
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

configur = ConfigParser() 
configur.read('config.ini')

print ("Loging Your Information.")

Uname = configur.get('Login','Username')
Pass = configur.get('Login','password')
Name = configur.get('Address','Name')
Mob = configur.get('Address','Mobile')
Loc = configur.get('Address','Locality')
Add = configur.get('Address','Address')
pin = configur.get('Address','Pincode')
URLS = configur.get('Product_URL','URL')
URLS = URLS.replace("\t","").split("\n")
#Total_URL = len(URLS)

print ("Information Load Successfully.")
print ("Product Purchasing Process Start.")

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get("https://www.flipkart.com")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(Uname)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(Pass)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
time.sleep(2)

for i,URL in enumerate(URLS):
    driver.get(URL);
    driver.execute_script('''window.open("");''')
    driver.switch_to.window(driver.window_handles[i])
    driver.get(URL);
    driver.refresh()
    
c=0
i=0
while True:
    if i>len(URLS)-1:
        i=0
    try:
        time.sleep(2)
        Buy = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div/div/div[2]/div/ul/li[2]/form/button").click()
        driver.switch_to.window(driver.window_handles[i])
        i += 1
        c += 1
        if c == len(URLS):
            break
    except:
        driver.refresh()

c=0
while True:
    if i>len(URLS)-1:
        i=0
    try:
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
        
        driver.switch_to.window(driver.window_handles[i])

        i += 1
        c += 1
        if c == len(URLS):
            break
    except:
        break

c=0
while True:
    if i>len(URLS)-1:
        i=0
    try:
        Confirm = driver.find_elements_by_class_name('_2AkmmA')
        driver.execute_script("arguments[0].click();", Confirm[0])  
        driver.switch_to.window(driver.window_handles[i])
        i += 1
        c += 1
        if c == len(URLS):
            break
    except:
        break
        
c=0
while True:
    if i>len(URLS)-1:
        i=0
    try:
        time.sleep(2)
        COD = driver.find_elements_by_class_name('_6ATDKp')
        COD[-1].click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[i])
        i += 1
        c += 1
        if c == len(URLS):
            break
    except:
        break

#driver.quit()
#driver.close()

print ("Product Purchase Process Completed.")
print ("Please verify Your Order.")
