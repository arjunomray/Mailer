import time
from selenium.webdriver.common.by import By
import csv
from selenium.common.exceptions import WebDriverException

names = ['Name']


def main_path(driver, linkedin_link, company_name, max_names):
    try:
        driver.get(linkedin_link)
        time.sleep(15)
        name_xpath = "org-people-profile-card__profile-title "
        counter = 0
        while True:
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(0.3)
            last_element= names[len(names)-1]
            elements = list(driver.find_elements(By.CLASS_NAME,name_xpath))
            print(len(elements))
            print(elements[counter].text)
            for element in elements:
                if not element or element == last_element:
                    break
                names.append(element.text)
            counter += 1
            if len(elements) >= max_names:
                break
    except WebDriverException as e:
        # Handle WebDriverException, which includes if the browser is closed
        print("WebDriverException occurred:", e)

    finally:
        # Clean up: Close the browser window
        driver.quit()
        serialize_to_csv(set(names), company_name)


def serialize_to_csv(names, company_name):
    with open(f'{company_name}_names.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Name'])  # Write header
        for name in names:
            csv_writer.writerow([name])
