from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()

    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text

    result = int(x) + int(y)

    answer = Select(browser.find_element(By.TAG_NAME, "select"))
    answer.select_by_visible_text(str(result))

    submit_but = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_but.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
