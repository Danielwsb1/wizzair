# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Dane testowe - ("lamerski" hardcode)
valid_name = "Dick"
valid_surname = "Laurent"
gender = 'female'
valid_telephone = '123432456'
invalid_email = "xcvsdfvhsdfjh.wp.pl"
valid_password = "Qwer46@213"

class WizzairRegistration(unittest.TestCase):
    """
    Scenariusz testowy: Rejestracja nowego użytkownika na stronie wizzair.com
    """
    def setUp(self):
        """
        Warunki wstępne:
        Przeglądarka otwarta na https://wizzair.com/pl-pl/main-page#/
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")

    def tearDown(self):
        """ Sprzątanie po teście """
        self.driver.quit()

    def test_wrong_email(self):
        """
        Rejestracja nowego użytkownika
        używając adresu email - dane niepoprawne
        (niekompletny email brak '@')
        """
        driver = self.driver

        # KROKI:
        # ======================
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        # Czekam maks. 5 sekund, aż będzie można kliknąć przycisk ZALOGUJ
        zaloguj_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[data-test=navigation-menu-signin]")))
        zaloguj_btn.click()
        # ======================
        # 2. Kliknij REJESTRACJA
        rejestracja_btn = driver.find_element_by_css_selector('.login-form__footer button.content__link1')
        rejestracja_btn.click()
        # ======================
        # 3. Wprowadź imię
        imie_field = driver.find_element_by_name("firstName")
        imie_field.send_keys(valid_name)
        # ======================
        # 4. Wprowadź nazwisko
        nazwisko_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys(valid_surname)
        # 5.Wybierz płeć
        # ======================
        if gender == 'male':
            # Wybierz MĘŻCZYZNA
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            imie_field.click()
            m.click()
        else:
            # WYBIERZ KOBIETA
            f = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            f.click()
        # ======================
        # 6. Wpisz nr telefonu
        telephone_field = driver.find_element_by_name("phoneNumberValidDigits")
        telephone_field.send_keys(valid_telephone)
        # ======================
        # 7. Wpisz niepoprawny e-mail (brak '@')
        email_field = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_field.send_keys(invalid_email)
        # ======================
        # 8. Wpisz hasło
        password_field = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        password_field.send_keys(valid_password)
        # ======================
        # 9. Wybierz narodowość (Polskę)
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj Polskę
        country_to_choose = driver.find_element_by_xpath('//label[@data-test="booking-register-country-label"][164]')
        # Przewiń i kliknij
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()
        # ======================
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        privacy_policy_checkbox = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy_checkbox.click()
        # ======================
        # 11. Kliknij ZAREJESTRUJ
        register_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        register_btn.click()


        sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
