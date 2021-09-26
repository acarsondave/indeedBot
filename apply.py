import sys
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import *
from selenium.webdriver.chrome.options import Options


def element_exists(element):
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
    except:
        return False


def captcha_check(element='h-captcha'):
    if element_exists(element) is not False:
        captcha = driver.find_element_by_class_name(element)
        if captcha.is_displayed():
            print('CAPTCHA has been found')
            winsound.Beep(3000, 1000)
            try:
                WebDriverWait(driver, long_timeout).until_not(
                    EC.text_to_be_present_in_element((By.ID, 'login-recaptcha-message-error'),
                                                     'Captcha validation unsuccessful. Please try again.'))
            except:
                print('CAPTCHA not solved in time, program terminating\nGood bye')
                sys.exit(1)
            print('CAPTCHA has been solved')
        return True
    else:
        print('CAPTCHA not found')


def popup_check(element='popover-x-button-close'):
    try:
        popup_close = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
        popup_close.click()
        print('POPUP has been found\nPOPUP has been closed')
    except Exception as e:
        # print('POPUP not found')
        # print('error: ' + repr(e))
        pass


def next_weekday(date):
    if date.weekday() in {5, 6}:
        date += timedelta(days=7 - date.weekday())
    return date


chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
driver.get(login_url)

WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'loginform')))
driver.get(login_url)

driver.find_element_by_id('login-email-input').send_keys(account_email)
driver.find_element_by_id('login-password-input').send_keys(account_password)
driver.find_element_by_id('login-password-input').send_keys(Keys.ENTER)

if captcha_check():
    driver.find_element_by_id('login-password-input').send_keys(account_password)
    driver.find_element_by_id('login-password-input').send_keys(Keys.ENTER)

for job in job_titles:
    job_postings_url = base_url + '/jobs?q=' + job.replace(' ', '+').strip() + '&l=' + job_location.strip() + \
                       date_posted[job_posting_age] + job_type[job_posting_type] + \
                       experience_level[job_posting_experience] + job_distance[job_posting_distance]
    driver.get(job_postings_url)
    job_listing_count = 0

    while True:
        page_job_links = driver.find_elements_by_class_name('result')

        for link in page_job_links:
            job_listing_count += 1
            job_urls.append(link.get_attribute('href'))

        popup_check()

        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Next"]'))).click()
        except:
            break

for url in job_urls:
    driver.get(url)

    try:
        apply_button = driver.find_element(By.ID, 'indeedApplyButton')
        apply_button.click()

        while True:
            print('start of while loop')
            continue_button = driver.find_element_by_class_name('ia-continueButton')
            application_heading_raw = driver.find_element_by_class_name('ia-BasePage-heading').text
            application_heading = driver.find_element_by_class_name('ia-BasePage-heading').text.lower()
            unkown_questions = False

            if 'questions' in application_heading:
                questions = driver.find_elements_by_class_name('ia-Questions-item')
                questions_sleep = 0.25
                for question in questions:
                    question_text = question.find_element_by_class_name('ia-QuestionLabelWrapper-question').text

                    if 'linkedin profile' == question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_linkedin)
                        time.sleep(questions_sleep)
                    elif 'website' == question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_personalwebsite)
                        time.sleep(questions_sleep)
                    elif 'list 2-3 dates and time ranges that you could do an interview' in question_text.lower():
                        availability = next_weekday(datetime.now() + timedelta(days=2))
                        availability2 = next_weekday(datetime.now() + timedelta(days=3))
                        question.find_element_by_xpath('.//span/textarea').send_keys(
                            availability.strftime('%m/%d/%Y') + ' after 12pm\n' + availability2.strftime('%m/%d/%Y') + 'after 12pm')
                        time.sleep(questions_sleep)
                    elif 'development leadership' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_leadershipdevelopment)
                        time.sleep(questions_sleep)
                    elif 'years of web development experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_webdevyears)
                        time.sleep(questions_sleep)
                    elif 'salary' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_salary)
                        time.sleep(questions_sleep)

                    elif 'sponsorship' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_sponsorship.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'are you currently a georgia resident or willing to relocate to georgia' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_relocate.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'highest level of education you have completed' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_education.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'authorized to work in the united states' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_workauthorized.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'valid citizen' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_citizen.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'gender' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_gender.title() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'veteran status' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_veteranoptions[apply_veteran].capitalize() + "')]").click()
                        time.sleep(questions_sleep)
                    elif 'disability status' in question_text.lower():
                        question.find_element_by_xpath(".//label/div[contains(text(), '" + apply_disabilityoptions[apply_disability].capitalize() + "')]").click()
                        time.sleep(questions_sleep)

                    elif 'ethnicity' in question_text.lower():
                        question.find_element_by_xpath(".//div/select/option[contains(text(), 'Two or More')]").click()
                        time.sleep(questions_sleep)

                    elif 'java experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_java)
                        time.sleep(questions_sleep)
                    elif 'python experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_python)
                        time.sleep(questions_sleep)
                    elif 'django experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_django)
                        time.sleep(questions_sleep)
                    elif 'aws experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_aws)
                        time.sleep(questions_sleep)
                    elif 'php experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_php)
                        time.sleep(questions_sleep)
                    elif 'react experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_react)
                        time.sleep(questions_sleep)
                    elif 'node experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_node)
                        time.sleep(questions_sleep)
                    elif 'angular experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_angular)
                        time.sleep(questions_sleep)
                    elif 'javascript experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_javascript)
                        time.sleep(questions_sleep)
                    elif 'orm experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_orm)
                        time.sleep(questions_sleep)
                    elif 'sdet experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_sdet)
                        time.sleep(questions_sleep)
                    elif 'selenium experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_selenium)
                        time.sleep(questions_sleep)
                    elif 'test automation experience' in question_text.lower():
                        question.find_element_by_css_selector('[id^="input-q"]').send_keys(apply_testautomation)
                        time.sleep(questions_sleep)

                    else:
                        print('unknown question: ' + question_text.lower())
                        winsound.Beep(3000, 1000)
                        unkown_questions = True
                        while WebDriverWait(question, long_timeout).until_not(
                                EC.text_to_be_present_in_element((By.CLASS_NAME, 'ia-BasePage-heading'),
                                                                 application_heading_raw)):
                            time.sleep(10)
                            print('while loop wait for text change')
                            pass

            # elif 'add a resume' in application_heading:
            #     print('resume')
            #
            # elif 'requires a cover letter for this application' in application_heading:
            #     print('cover letter')
            #
            # elif 'select a past job that shows relevant experience' in application_heading:
            #     print('relevant experience')
            #
            # elif 'consider adding supporting documents' in application_heading:
            #     print('supporting documents')

            elif 'please review your application' in application_heading:
                #continue_button.click()
                #time.sleep(3)
                break

            print('out of heading text if statement')

            if not unkown_questions:
                time.sleep(1)
                continue_button.click()
                WebDriverWait(driver, 15).until_not(EC.text_to_be_present_in_element((By.CLASS_NAME, 'ia-BasePage-heading'), application_heading_raw))

            print('after normal continue button click')

    except Exception as e:
        print('except error for application button')
        print('error: ' + repr(e))
        #continue