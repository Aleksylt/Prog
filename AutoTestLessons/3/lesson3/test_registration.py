import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        ex_result = "Congratulations! You have successfully registered!"
        browser = webdriver.Chrome()

        #############проверка обязательных полей
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, "input[required].first")
        first_name.send_keys("first_name")
        last_name = browser.find_element(By.CSS_SELECTOR, "input[required].second")
        last_name.send_keys("last_name")
        email = browser.find_element(By.CSS_SELECTOR, "input[required].third")
        email.send_keys("a@b.c")

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
        self.assertEqual(welcome_text, ex_result, f"error registration on {link}")
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        ex_result = "Congratulations! You have successfully registered!"
        browser = webdriver.Chrome()

        #############проверка обязательных полей
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, "input[required].first")
        first_name.send_keys("first_name")
        last_name = browser.find_element(By.CSS_SELECTOR, "input[required].second")
        last_name.send_keys("last_name")
        email = browser.find_element(By.CSS_SELECTOR, "input[required].third")
        email.send_keys("a@b.c")

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
        self.assertEqual(welcome_text, ex_result, f"error registration on {link}")
        browser.quit()

if __name__ == "__main__":
    unittest.main()