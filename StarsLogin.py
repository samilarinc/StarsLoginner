import time
import poplib
import os
from selenium import webdriver

path = "C:/Users/$USERNAME"
path = os.path.expandvars(path)


mailAdress2 = ""
mailPass2 = ""
bilkentID2 = ""
srsPass2 = ""
    
file1 = open("{}/chromedriver/bin.dll".format(path),'r')

mailAdress = file1.readline().strip()
mailPass = file1.readline().strip()
bilkentID = file1.readline().strip()
srsPass = file1.readline().strip()

def decrypter():
    l1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #This sequence is private. If you don't want to use, just use previous version.
    j = 0
    
    global mailAdress2
    global mailPass2
    global bilkentID2
    global srsPass2
    
    for i in mailAdress:
        mailAdress2 += chr(ord(i) - l1[j])
        j += 1
    for i in mailPass:
        mailPass2 += chr(ord(i) - l1[j])
        j += 1
    for i in bilkentID:
        bilkentID2 += chr(ord(i) - l1[j])
        j += 1
    for i in srsPass:
        srsPass2 += chr(ord(i) - l1[j])
        j += 1
    

def verification():
    pop3server = 'mail.bilkent.edu.tr'
    username = mailAdress2 #email
    password = mailPass2 #mail password
    pop3server = poplib.POP3_SSL(pop3server, port=995)

    pop3server.user(username)
    pop3server.pass_(password)
    pop3info = pop3server.stat() 
    mailcount = pop3info[0] 

    x = []
    x = pop3server.retr(mailcount)[1]

    q = x[-2]
    q = q.decode("utf-8")       
    x = q.find("Code: ")
    q = q[x+6:x+11]
    
    pop3server.quit()
    return q

def program():
    global driver
    driver = webdriver.Chrome('{}/chromedriver/chromedriver.exe'.format(path)) #path
    driver.maximize_window()
    driver.get("https://stars.bilkent.edu.tr/srs")

    driver.find_element_by_xpath("//*[@id=\"LoginForm_username\"]").send_keys(bilkentID2) #number
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/div/div/input").send_keys(srsPass2) #srs password
    driver.find_element_by_xpath("//*[@id=\"login-form\"]/fieldset/div/div[1]/div[3]/button").click()

    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input").send_keys(verification())


    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/button").click()

decrypter()
program()
