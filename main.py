from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

URL_SPEED_TEST = 'https://www.speedtest.net'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.speedtest.net')
dic = {}
time.sleep(10)
accept_cooki = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button')
print(accept_cooki.text)
time.sleep(10)
accept_cooki.click()

start_test = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
start_test.click()

time.sleep(25)

downlowd_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
print(downlowd_speed.text)
dic.update({'Download Speed': f'{downlowd_speed.text}'})

time.sleep(25)

upload_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
print(upload_speed.text)
dic.update({'Upload Speed': f'{upload_speed.text}'})

print(dic)

driver.get('https://twitter.com/home?lang=uk')
time.sleep(5)
enter_login = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
enter_login.click()
time.sleep(7)
enter_email = driver.find_element(By.CLASS_NAME,'.r-13qz1uu')
enter_email.send_keys('avalstk')
enter_email.send_keys(Keys.ENTER)
time.sleep(6)
enter_password = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
enter_password.send_keys('')
time.sleep(5)

# post = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
# post.click()

