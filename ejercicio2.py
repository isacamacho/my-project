from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www3.animeflv.net/")

link = driver.find_element(By.CSS_SELECTOR, "a[href*='one-piece']")
link.click()

episodio = driver.find_element(By.CSS_SELECTOR, "")
ultimo_episodio = int(episodio)
#fa-play-circle



#assert ultimo_episodio == 1003