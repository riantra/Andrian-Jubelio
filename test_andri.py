from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Mengatasi web yang langsung tertutup setelah dijalankan
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#login flow ke jubelio
driver.get("https://<qa.rakamin.jubelio@gmail.com>:<Jubelio123!>@app.jubelio.com/home/inventory")
driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
driver.find_element(By.CSS_SELECTOR, 'button.ladda-button').click()
time.sleep(10)
#masuk ke halaman inventory
driver.get("https://<qa.rakamin.jubelio@gmail.com>:<Jubelio123!>@app.jubelio.com/home/inventory")
#memilih seluruh produk untuk mengatur persediaan
driver.find_element(By.ID, "select-all-checkbox").click()
#export persediaan online (sync online)
driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[1]').click()

