from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

LOGIN = 'LOGIN'
PASSWORD = 'PASSWORD'
PHONE = 'PHONE WITHOUT 8 OR +7'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
driver.get("http://www.tinder.com")
parent = driver.current_window_handle
time.sleep(8)
driver.find_element_by_xpath(
    """//*[@id="modal-manager"]/div/div/div[2]/div/div[3]/div[1]/button/span/span""").click()
time.sleep(8)
child = driver.window_handles[1]
driver.switch_to.window(child)

# FACEBOOK
user = driver.find_element_by_name("email")
user.clear()
user.send_keys(LOGIN)
passw = driver.find_element_by_name("pass")
passw.clear()
passw.send_keys(PASSWORD)
passw.send_keys(Keys.RETURN)

# ALLOW TINDER TO FACEBOOK ACCOUNT
try:
    driver.find_element_by_xpath("""
    //*[@id="u_0_4"]/div[2]/div[1]/div[1]/button""").click()
except:
    pass

try:
    code_block = driver.find_element_by_name("approvals_code")
    CODE = input("Enter code from your phone: ")
    code_block.send_keys(CODE)
    driver.find_element_by_xpath("""//*[@id="checkpointSubmitButton"]""").click()
    driver.find_element_by_xpath("""//*[@id="u_0_3"]""").click()
    driver.find_element_by_xpath("""//*[@id="checkpointSubmitButton"]""").click()
except:
    print("Don't need a phone!")

# BACK TO TINDER
driver.switch_to.window(parent)
time.sleep(5)

try:
    phone = driver.find_element_by_name("phone_number")
    phone.clear()
    phone.send_keys(PHONE)
    driver.find_element_by_xpath("""//*[@id="modal-manager"]/div/div/div[2]/button""").click()

    # CODE
    CODE = input("Enter code from your phone: ")
    code_block = driver.find_element_by_css_selector(
        r"""#modal-manager > div > div > div.Ta\28 c\29.Expand.Mx\28 a\29 > div.D\28 b\29.My\28 24px\29.Whs\28 nw\29 > input:nth-child(1)""")
    code_block.send_keys(CODE)
    driver.find_element_by_xpath("""//*[@id="modal-manager"]/div/div/div[2]/button""").click()
    time.sleep(5)
except:
    pass
# ALLOW GEO
try:
    driver.find_element_by_class_name(
        r"""button Lts($ls-s) Z(0) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Py(0) H(40px) Mih(40px) Lh(40px) button--primary-shadow Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Trsdu($fast) Trsp($background) Bg($primary-gradient) StyledButton Fw($semibold) D(ib) W(225px) W(a)""").click()
except:
    pass
driver.set_window_size(600, 600)
time.sleep(2)

try:
    driver.find_element_by_xpath("""//*[@id="content"]/div/span/div/div[2]/div/div/div[3]/button[1]""").click()
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@id="content"]/div/span/div/div[2]/div/div/div[3]/button[2]""").click()
except:
    print("Already accept geolocation")

try:
    while True:
        time.sleep(2)
        driver.find_element_by_xpath(
            """//*[@id="content"]/div/span/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[4]""").click()
except:
    driver.close()
