import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("first_name")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("last_name")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("a@b.c")

    load_file = browser.find_element(By.ID,"file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    load_file.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



