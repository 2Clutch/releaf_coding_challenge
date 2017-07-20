from selenium import webdriver

def get_links(company_name):
	url = "https://www.google.com/"
	browser = webdriver.PhantomJS()
	browser.get(url)
	search_box = browser.find_element_by_name("q")
	search_box.send_keys(company_name)
	search_box.submit()
	try:
		links = browser.find_elements_by_xpath("//ol[class='web_regular_results']//h3//a")
	except:
		links = browser.find_elements_by_xpath("//h3//a")
	results = []
	for link in links:
		href = link.get_attribute("href")
		print(href)
		results.append(href)
	browser.close()
	return results

get_links("dog")