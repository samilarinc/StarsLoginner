import poplib
from selenium import webdriver
from os import path, remove, mkdir
import urllib.request as urllib2
from zipfile import ZipFile
from time import sleep
from sys import exit

userPath = "C:/Users/$USERNAME"
userPath = path.expandvars(userPath)

def verification(mailAddress, mailPass):
    pop3server = 'mail.bilkent.edu.tr'
    username = mailAddress #email
    password = mailPass #mail password
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

def defRun():
    try:
        file1 = open("{}/chromedriver/bin.dll".format(userPath),'r')

        version = file1.readline().strip().split('.')
        mailAddress = file1.readline().strip()
        mailPass = file1.readline().strip()
        bilkentID = file1.readline().strip()
        srsPass = file1.readline().strip()

        driver = webdriver.Chrome('{}/chromedriver/chromedriver.exe'.format(userPath)) #path
        driver.maximize_window()
        driver.get("https://stars.bilkent.edu.tr/airs")

        driver.find_element_by_xpath("//*[@id=\"LoginForm_username\"]").send_keys(bilkentID) #number
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/div/div/input").send_keys(srsPass) #srs password
        driver.find_element_by_xpath("//*[@id=\"login-form\"]/fieldset/div/div[1]/div[3]/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input").send_keys(verification(mailAddress, mailPass))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[2]/button").click()
        input()

    except Exception as e:
        if "not reachable" in str(e):
            exit()

def getVersion():
    data = str(urllib2.urlopen("https://chromedriver.chromium.org").read())
    start = data.find("Latest stable release:")
    data = data[start:start+300]
    start = data.find("href") + 6
    data = data[start:]
    start = data.find("path=")+5
    stop = data.find("/\"")
    driverUrl = data[:stop]
    data = data[start:stop]
    latestVersion = data.split('.')
    return latestVersion, driverUrl

def downloadDriver(version, driverUrl):
    version = ".".join(version)
    if not path.exists(f"{userPath}/chromedriver"):
        mkdir(f"{userPath}/chromedriver")
    urllib2.urlretrieve(f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip", f"{userPath}/chromedriver/chromedriver.zip")
    with ZipFile(f"{userPath}/chromedriver/chromedriver.zip") as myzip:
        with myzip.open("chromedriver.exe") as myexe:
            with open(f"{userPath}/chromedriver/chromedriver.exe", "wb") as out:
                out.write(myexe.read())
    remove(f"{userPath}/chromedriver/chromedriver.zip")
    return version

def firstRun():
    version, driverUrl = getVersion()
    version = downloadDriver(version, driverUrl)
    infoFile = open(f"{userPath}/chromedriver/bin.dll", "w")
    mailAddress = input("Mail address: ")
    mailPassword = input("Mail password: ")
    studentID = input("Student ID: ")
    starsPassword = input("Stars password: ")
    print(f"{version}\n{mailAddress}\n{mailPassword}\n{studentID}\n{starsPassword}", file = infoFile)
    infoFile.close()
    defRun()

if not (path.exists(f"{userPath}/chromedriver/bin.dll") and path.exists(f"{userPath}/chromedriver/chromedriver.exe")):
    firstRun()
else:
    with open("{}/chromedriver/bin.dll".format(userPath),'r') as file1:
        version = file1.readline().strip().split('.')
        newVersion, driverUrl = getVersion()
        if newVersion[0] > version[0]:
            downloadDriver(newVersion, driverUrl)
    defRun()
