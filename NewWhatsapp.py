from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 


target = ['https://wa.me/5511941031501?text=Fala%20Vinicius%20Foi+incr%C3%ADvel+ter+voc%C3%AA+nesses+dois+dias+de+Steiger+Mob%2C+n%C3%B3s+gostar%C3%ADamos+de+saber+se+fez+sentido+tudo+que+foi+falado%2C+e+o+que+Deus+falou+a+voc%C3%AA+durante+esses+dias.+%0D%0ACaso+queira+participar+das+pr%C3%B3ximas+a%C3%A7%C3%B5es+de+evangelismo+e+at%C3%A9+entender+mais+a+fundo+como+funciona+a+miss%C3%A3o+Steiger+vem+comigo+e+vamos+caminhar+juntos%21+%0D%0APergunte+me+como+%3F+%0D%0A%0D%0ACriamos+esse+grupo+para+compartilhar+as+pr%C3%B3ximas+a%C3%A7%C3%B5es+e+informa%C3%A7%C3%B5es+relacionadas+a+miss%C3%A3o+sugest%C3%B5es+e+experi%C3%AAncias+s%C3%A3o+muito+bem+vindas...+Partiu+viver+essa+miss%C3%A3o+juntos%21,https://wa.me/5511980692090?text=Fala%20Aline%20Foi+incr%C3%ADvel+ter+voc%C3%AA+nesses+dois+dias+de+Steiger+Mob%2C+n%C3%B3s+gostar%C3%ADamos+de+saber+se+fez+sentido+tudo+que+foi+falado%2C+e+o+que+Deus+falou+a+voc%C3%AA+durante+esses+dias.+%0D%0ACaso+queira+participar+das+pr%C3%B3ximas+a%C3%A7%C3%B5es+de+evangelismo+e+at%C3%A9+entender+mais+a+fundo+como+funciona+a+miss%C3%A3o+Steiger+vem+comigo+e+vamos+caminhar+juntos%21+%0D%0APergunte+me+como+%3F+%0D%0A%0D%0ACriamos+esse+grupo+para+compartilhar+as+pr%C3%B3ximas+a%C3%A7%C3%B5es+e+informa%C3%A7%C3%B5es+relacionadas+a+miss%C3%A3o+sugest%C3%B5es+e+experi%C3%AAncias+s%C3%A3o+muito+bem+vindas...+Partiu+viver+essa+miss%C3%A3o+juntos%21
']

Def OpenFF:
    ie.get(target)
    



#Creates FireFox Profile
pref = webdriver.FirefoxProfile()
pref.set_preference("browser.helperApps.neverAsk.saveToDisk","application/csv,text/csv")
pref.set_preference("browser.download.manager.showWenStarting", False)
pref.set_preference("browser.download.dir", "C:/Users/vteixeira/tempAutomation/")
pref.set_preference("browser.download.folderList", 2)

#Invoke WebDriver
ie = webdriver.Firefox(firefox_profile=pref)

#Login Credentials
username = 'vteixeira'
password = '0501Baruke'

#Download routine
ie.set_page_load_timeout(20)
ie.get('https://clientsupport.worldlinesweden.com/sr/jira.issueviews:searchrequest-csv-current-fields/11177/SearchRequest-11177.csv')