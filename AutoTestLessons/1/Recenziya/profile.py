from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[1]/input')
    first.send_keys("Test")  # Напишем текст в найденное поле
    time.sleep(5)

    last = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[2]/input')
    last.send_keys("Test")  # Напишем текст в найденное поле
    time.sleep(5)

    fmail = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[3]/input')
    fmail.send_keys("Test")  # Напишем текст в найденное поле
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()