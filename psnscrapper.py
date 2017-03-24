## clear && printf '\e[3J'
## clears the entire screen buffer

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class deal:
	game_title = ""
	game_link = ""
	game_original_price = 0.00
	game_sale_price = 0.00
	game_percent_off = 0
	game_platform = ""




path_to_chromedriver = '/Users/matthewbroton/Desktop/projects/psn store scrapper/chromedriver' # change path as needed
## driver = webdriver.Chrome(executable_path = path_to_chromedriver)

driver = webdriver.PhantomJS()

## url = "https://store.playstation.com/#!/en-us/all-deals/cid=STORE-MSF77008-ALLDEALS"
## url = raw_input("What is the PSN Store URL?: ")

url = "https://store.playstation.com/#!/en-us/flash-sale/cid=STORE-MSF77008-FLASHSALE17LP"
## or replace raw_input with the url link
driver.get(url)


wait = WebDriverWait(driver, 10)

driver.implicitly_wait(10) # seconds


## time.sleep(10)
## driver.implicitly_wait(200) # seconds

## thelist = driver.find_elements_by_class_name("cellTitle")


##for game in thelist:
##	newentry = deals()
##	newentry.game_title = game.text
## 	dealslist.append(newentry)



## thelist = driver.find_elements_by_class_name("buyPrice")


## thelist = driver.find_elements_by_class_name("price")


## print "before thingy"

totalpages = 16

dealslist = []

page = 0

while True:
	## print "Enter: while loop"
	time.sleep(30)

	gamenames = driver.find_elements(By.CLASS_NAME,'cellTitle')

	platforms = driver.find_elements(By.CLASS_NAME,'pforms')

	prices = driver.find_elements(By.CLASS_NAME,'buyPrice ')

	links = driver.find_elements(By.CLASS_NAME,'permalink')

	originalprices = driver.find_elements(By.CLASS_NAME,'price')

	def populatelist():
		for i in range(len(gamenames)):
			n = deal()

			n.game_title = gamenames[i].text
			n.game_platform = platforms[i].text
			n.game_sale_price = prices[i].text
			n.game_link = links[i].get_attribute('href')
			n.game_original_price = originalprices[i].text

			dealslist.append(n)


	populatelist()

	try:
		## //*[@id="panelPaginator-10"]/a[4]
		## element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navArrow navLinkNext')))
		element = driver.find_element_by_xpath('.//*[@id="panelPaginator-10"]/a[4]')
		element.click()
	except TimeoutException:
		break

	page = page + 1
	if page + 1 >= totalpages :
		break
	## break

ps4games = []
ps3games = []
vitagames = []

for i in range(len(dealslist)):
	cplatform = dealslist[i].game_platform
	if cplatform == 'PS4':
		ps4games.append(dealslist[i])
	if cplatform == 'PS3':
		ps3games.append(dealslist[i])
	if cplatform == 'PS Vita':
		vitagames.append(dealslist[i])


def getTitle(obj):
	return obj.game_title

sortedps4games = sorted(ps4games, key=getTitle)
sortedps3games = sorted(ps3games, key=getTitle)
sortedvitagames = sorted(vitagames, key=getTitle)

def printarray(arraylist):
	for item in arraylist:
		cplatform = item.game_platform
		if cplatform == 'PS4':
			print ':ps4:'+ '[url="' + item.game_link +'"] ' + item.game_title + '[/url] - ' + item.game_sale_price
		if cplatform == 'PS3':
			print ':ps3:'+ '[url="' + item.game_link +'"] ' + item.game_title + '[/url] - ' + item.game_sale_price
		if cplatform == 'PS Vita':
			print ':vita:'+ '[url="' + item.game_link +'"] ' + item.game_title + '[/url] - ' + item.game_sale_price

print "PS4"
printarray(sortedps4games)
print "\n\n\nPS3"
printarray(sortedps3games)
print "\n\n\nVita"
printarray(sortedvitagames)



##for i in range(len(gamenames)):
##		if platforms[i].text == 'PS4':
##			print ':ps4:'+ '[url="' + links[i].get_attribute('href') +'"] ' + gamenames[i].text + '[/url] - ' + prices[i].text
##		if platforms[i].text == 'PS3':
##			print ':ps3:' + '[url="' + links[i].get_attribute('href') +'"] ' + gamenames[i].text + '[/url] - ' + prices[i].text
##		if platforms[i].text == 'PS Vita':
##			print ':vita:' + '[url="' + links[i].get_attribute('href') +'"] ' + gamenames[i].text + '[/url] - ' + prices[i].text
		## print '[url="' + links[i].get_attribute('href') +'"] ' + gamenames[i].text + '[/url] - ' + prices[i].text
	## [url="https://google.com"]killme[/url]
	## :ps4:  :ps3: Journey - $5.99 - 60% Off - Ends 3/28 N



driver.quit()

