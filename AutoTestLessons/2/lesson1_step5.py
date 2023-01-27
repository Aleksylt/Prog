from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()

    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    c_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    c_box.click()

    r_but = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    r_but.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

