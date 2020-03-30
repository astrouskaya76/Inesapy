
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import HtmlTestRunner


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='custom-logo']")))
            print("California Real Estate Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('page_loading_error.png')

        # Checking page title for "California Real Estate" then print it
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

        my_name = driver.find_element_by_name("g2-name")
        my_name.clear()
        my_name.send_keys("Inesa")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        my_name = driver.find_element_by_name("g2-email")
        my_name.clear()
        my_name.send_keys("innadia2014@gmail.com")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        #my_message = driver.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        #my_message.send_keys("Hello World!")
        #my_message.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)

       # my_name = driver.find_element_by_xpath("//button[@class='pushbutton-wide']")
       # my_name.click()
       # driver.implicitly_wait(5)

        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Message Send Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('send_page_loading_error.png')

        my_name = driver.find_element_by_xpath("//a[contains(text(),'go back')]")
        my_name.click()

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page ", driver.title + " has four pictures")

    def test_search_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://qasvus.wordpress.com/")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='custom-logo']")))
            print("California Real Estate Page 1120x550 is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('page_loading_error.png')

        # Checking page title for "California Real Estate" then print it
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + "1120x550 as Page title")

        my_name = driver.find_element_by_name("g2-name")
        my_name.clear()
        my_name.send_keys("Inesa")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        my_name = driver.find_element_by_name("g2-email")
        my_name.clear()
        my_name.send_keys("innadia2014@gmail.com")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        #my_message = driver.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        #my_message.send_keys("Hello World!")
        #my_message.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)

       # my_name = driver.find_element_by_xpath("//button[@class='pushbutton-wide']")
       # my_name.click()
       # driver.implicitly_wait(5)

        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Message Send Page 1120x550 is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('send_page_loading_error.png')

       # my_name = driver.find_element_by_xpath("//a[contains(text(),'go back')]")
       # my_name.click()

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page ", driver.title + " 1120x550 has four pictures")

    def tearDown(self):
        # Close the browser.
        self.driver.quit()

class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='custom-logo']")))
            print("California Real Estate Page Firefox is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('page_loading_error.png')

        # Checking page title for "California Real Estate" then print it
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as  Firefox Page title")

        my_name = driver.find_element_by_name("g2-name")
        my_name.clear()
        my_name.send_keys("Inesa")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        my_name = driver.find_element_by_name("g2-email")
        my_name.clear()
        my_name.send_keys("innadia2014@gmail.com")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        #my_message = driver.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        #my_message.send_keys("Hello World!")
        #my_message.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)

       # my_name = driver.find_element_by_xpath("//button[@class='pushbutton-wide']")
       # my_name.click()
       # driver.implicitly_wait(5)

        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Message Send Page Firefox is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('send_page_loading_error.png')

        my_name = driver.find_element_by_xpath("//a[contains(text(),'go back')]")
        my_name.click()

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page ", driver.title + " Firefox has four pictures")

    def test_search_1250x850(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get("https://qasvus.wordpress.com/")

  # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='custom-logo']")))
            print("California Real Estate Page  Firefox  1120x850 is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('page_loading_error.png')

        # Checking page title for "California Real Estate" then print it
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + "  Firefox 1120x850 as Page title")

        my_name = driver.find_element_by_name("g2-name")
        my_name.clear()
        my_name.send_keys("Inesa")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        my_name = driver.find_element_by_name("g2-email")
        my_name.clear()
        my_name.send_keys("innadia2014@gmail.com")
        my_name.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        #my_message = driver.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        #my_message.send_keys("Hello World!")
        #my_message.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)

       # my_name = driver.find_element_by_xpath("//button[@class='pushbutton-wide']")
       # my_name.click()
       # driver.implicitly_wait(5)

        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Message Send Page  Firefox  1120x850 is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file('send_page_loading_error.png')

       # my_name = driver.find_element_by_xpath("//a[contains(text(),'go back')]")
       # my_name.click()

        assert "No results found." not in driver.page_source

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page ", driver.title + "  Firefox 1120x850 has four pictures")

    def tearDown(self):
        # Close the browser.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()