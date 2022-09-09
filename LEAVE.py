import unittest
import time
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class TestingOrangeHrm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) 

    def test_succes_ADD_COMENT(self):
        listcoment = ["sanber", "bagus", "nice", "haha", "yuk", "huhu", "yeyeye", "ya", "oke"]
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
        browser.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item active'])[1]") # 
        time.sleep(1)
        #step leave
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]").send_keys("Engineering") # isi sub unit
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div")
        time.sleep(1)

        #step memberikan comen
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/li/button/i").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/li/ul/li[1]/p").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/textarea").send_keys(random.choice(listcoment))
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/div/form/div[2]/button[2]").click()
        time.sleep(1)

    def test2_FAILED_ADD_COMENT(self):
        #listcoment = ["sanber", "bagus", "nice", "haha", "yuk", "huhu", "yeyeye", "ya", "oke"]
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
        browser.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item active'])[1]") # 
        time.sleep(1)
        #step leave
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]").send_keys("Engineering") # isi sub unit
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div")
        time.sleep(1)

        #step memberikan comenT FAILED
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/li/button/i").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[9]/div/li/ul/li[1]/p").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/div/form/div[2]/button[2]").click()
        time.sleep(1)

        #valisadi
        response_message = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div/span").text 
        self.assertEqual(response_message, 'Required')


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
