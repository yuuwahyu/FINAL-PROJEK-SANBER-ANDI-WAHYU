from lib2to3.pgen2 import driver
import unittest
import time
import random
from xmlrpc.client import Boolean
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select 

class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 

    def test_SUCCES_ADD_REQUITMENT(self):
        listkandidat = ["eko", "jualianto", "mawar", "wian", "ojan", "heri", "untung", "wardoyo", "sri"]
        listlastname = ["yu", "he", "ha", "lu", "ye", "haha", "ben", "yowes", "wes"]
        listemail = ["wele@gmail.com", "jo@gmail.com", "cobain@gmail.com", "terus@gmail.com", "terakhir@gmail"]
        
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)

        # step login
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi nama
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # jika email sudah terdaftar maka tidak bisa 
        time.sleep(1) #jika ingin run di ganti emailnya dengan yg belum terdaftar
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign up
        time.sleep(1)
         # step pilih menu Recruitment
        browser.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment'])[1]").click() # menu Recruitment
        time.sleep(1)

         #steb add Recruitment
        browser.find_element(By.XPATH,"(//button[normalize-space()='Add'])[1]").click() # klik menu add
        time.sleep(1) 
        browser.find_element(By.XPATH,"(//input[@placeholder='First Name'])[1]").send_keys(random.choice(listkandidat)) #isi nama kandidat
        time.sleep(2)
        browser.find_element(By.XPATH,"(//input[@placeholder='Last Name'])[1]").send_keys(random.choice(listlastname)) #isi last nime
        time.sleep(2)
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[1]").send_keys(random.choice(listemail)) #isi email
        time.sleep(2)
        browser.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click() # klik save
        time.sleep(2) 

    def test__requitmend_failed(self):
        listkandidat1 = ["eko", "jualianto", "mawar", "wian", "ojan", "heri", "untung", "wardoyo", "sri"]
        listlastname2 = ["yu", "he", "ha", "lu", "ye", "haha", "ben", "yowes", "wes"] 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)

        # step login
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi nama
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # jika email sudah terdaftar maka tidak bisa 
        time.sleep(1) #jika ingin run di ganti emailnya dengan yg belum terdaftar
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign up
        time.sleep(1)

         # step pilih menu Recruitment
        browser.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment'])[1]").click() # menu Recruitment
        time.sleep(1)

         #steb add Recruitment
        browser.find_element(By.XPATH,"(//button[normalize-space()='Add'])[1]").click() # klik menu add
        time.sleep(1) 
        browser.find_element(By.XPATH,"(//input[@placeholder='First Name'])[1]").send_keys(random.choice(listkandidat1)) #isi nama kandidat
        time.sleep(2)
        browser.find_element(By.XPATH,"(//input[@placeholder='Last Name'])[1]").send_keys(random.choice(listlastname2)) #isi last nime
        time.sleep(2)
        browser.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click() # klik save
        time.sleep(2) 

        #valisadi
        response_message = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/span").text 
        self.assertEqual(response_message, 'Required')

    def tearDown(self): 
        self.browser.close() 


if __name__ == "__main__": 
    unittest.main()