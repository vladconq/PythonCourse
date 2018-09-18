from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL_OR_PHONE = 'YOUR_EMAIL_OR_PHONE'
PASSWORD = 'YOUR_PASSWORD'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.get(
    "https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=fbconnect://success&scope=basic_info%2Cemail%2Cpublic_profile%2Cuser_about_me%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_friends%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_photos%2Cuser_relationship_details&response_type=token&__mref=message")
assert "Facebook" in driver.title

driver.delete_all_cookies()

# user
user = driver.find_element_by_name("email")
user.clear()
user.send_keys(EMAIL_OR_PHONE)
# pass
passw = driver.find_element_by_name("pass")
passw.clear()
passw.send_keys(PASSWORD)
# ENTER
passw.send_keys(Keys.RETURN)
# back
driver.execute_script("window.history.go(-1)")

# ok
try:
    driver.find_element_by_xpath("""//*[@id="u_0_v"]/div[2]/div[1]/div[1]/button""").click()
except:
    driver.find_element_by_xpath("""//*[@id="platformDialogForm"]/div[2]/button[2]""").click()
time.sleep(5)
driver.get("http://tinder.com")
time.sleep(5)
driver.find_element_by_xpath(
    """//*[@id="modal-manager"]/div/div/div[2]/div/div[3]/div[1]/button/span/span""").click()

time.sleep(5)

while True:
    driver.find_element_by_xpath(
        """//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]/span""").click()
    time.sleep(2)
