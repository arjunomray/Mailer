from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from send_email import send_mails_to_all
import app

linkedin_link = input("Enter company people linkedin link (copy the whole link with http://): ")
company_name = linkedin_link.split("/")[4]
max_names = int(input("Enter max number of people names: "))


chromeOptions = Options()
# options.headless = True
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
# chromeOptions.add_argument("--headless=new")
chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=./cookies/test") 
driver = webdriver.Chrome("./chromedriver", chrome_options=chromeOptions)


app.main_path(driver, linkedin_link, company_name, max_names, )


wanna_send_mails = bool(input("Want to send mails?:"))
if wanna_send_mails:
    send_mails_to_all(company_name)
