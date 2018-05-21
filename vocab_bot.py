from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import secrets


#define variables
username = "YOUR USERNAME HERE"
password = "YOUR PASSWORD HERE"
path = "PATH TO THE CHROMEDRIVER HERE"
practice_list  = "LINK TO YOUR PRACTICE LIST HERE"
keys = ["1A","2B","3C","4D"]
b = keys
vocabulary = []
q = False

#define some helper functions
def gogo(browser):
    if browser.find_element_by_class_name("type"):
        browser.find_element_by_class_name("type").click()
    else:
        browser.find_element_by_class_name("title").click()

def nexter(browser):
    if browser.find_element_by_class_name("next").is_displayed():
        browser.find_element_by_class_name("next").click()

    
#open browser webpage, login
browser = webdriver.Chrome(path)
browser.get("https://www.vocabulary.com/login/")
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_class_name("green").click()
time.sleep(1)




gogo(browser)
while 1==1:
    nexter(browser)
#Check if the question type is audio and skip if it is
    if browser.find_element_by_class_name("label").text == "Spell the word:":
        q = True
        while q == True:
            try:
                gogo(browser)
            except:
                browser.get("https://www.vocabulary.com/login/")
                browser.get(practice_list)
            time.sleep(1)
            if browser.find_element_by_class_name("label").text == "Spell the word:":
                q = True
            else:
               q = False

    if not browser.find_element_by_class_name("label").text == "Spell the word:" and q == False:       
        time.sleep(2)
        
        #find the word that is being asked and check if it's already recorded
        word = browser.find_element_by_css_selector("strong").text
        print(word)
        if not word in vocabulary:
            vocabulary.append(word)
            vars()[word] = []
            print(vocabulary)
            
            #randomly click one of the options if the word isn't recorded yet
            a = secrets.choice(keys)
            browser.find_element_by_css_selector("[accesskey = '"+ a + "']").click()
            time.sleep(0.5)
    
            #check if it's correct
            choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").get_attribute("class")

            #keep guessing until it's correct
            while not choice == "correct":
                b.remove(a)
                a = secrets.choice(b)
                choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").click()
                time.sleep(0.5)
                choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").get_attribute("class")
                time.sleep(0.5)

        # If the word is already recorded, check if its definition is already recorded
        elif browser.find_element_by_css_selector("[accesskey = '1A']").text in vars()[word]:
            choice = browser.find_element_by_css_selector("[accesskey = '1A']").click()
            choice = browser.find_element_by_css_selector("[accesskey = '1A']").get_attribute("class")
            
        elif browser.find_element_by_css_selector("[accesskey = '2B']").text in vars()[word]:
            choice = browser.find_element_by_css_selector("[accesskey = '2B']").click()
            choice = browser.find_element_by_css_selector("[accesskey = '2B']").get_attribute("class")

        elif browser.find_element_by_css_selector("[accesskey = '3C']").text in vars()[word]:
            choice = browser.find_element_by_css_selector("[accesskey = '3C']").click()
            choice = browser.find_element_by_css_selector("[accesskey = '3C']").get_attribute("class")

        elif browser.find_element_by_css_selector("[accesskey = '4D']").text in vars()[word]:
            choice = browser.find_element_by_css_selector("[accesskey = '4D']").click()           
            choice = browser.find_element_by_css_selector("[accesskey = '4D']").get_attribute("class")
        # If the word is recorded, but the question has a new definition, randomly guess and add the correct definition    
        else:
            a = secrets.choice(keys)
            browser.find_element_by_css_selector("[accesskey = '"+ a + "']").click()
            time.sleep(0.5)
    
            #check if it's correct
            choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").get_attribute("class")
    
            while not choice == "correct":
                b.remove(a)
                a = secrets.choice(b)
                choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").click()
                time.sleep(0.5)
                choice = browser.find_element_by_css_selector("[accesskey = '"+ a + "']").get_attribute("class")
                time.sleep(0.5)
            
        if choice == "correct":
            time.sleep(1)
            keys = ["1A","2B","3C","4D"]
            b = keys
            a = secrets.choice(keys)
            c = browser.find_element_by_css_selector('a.correct').text
            print(c)
            if not c in vars()[word]:
                vars()[word].append(c)
                time.sleep(1)
                print(vars()[word])
            nexter(browser)
            time.sleep(3)
            #reload the quiz
            try:
                gogo(browser)
            except:
                browser.get("https://www.vocabulary.com/login/")
                browser.get(practice_list)
            time.sleep(1)
