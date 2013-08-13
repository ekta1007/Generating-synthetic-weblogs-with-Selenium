#lenovo Synthetic Weblogs & Semi-assisted journey with Selenium IDE & Python webdriver

# coding: utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LenoveTestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.lenovo.com/in/en/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_lenove_test_case1(self):
        selections_made=[]
        Pages_browsed=[]
        driver = self.driver
        driver.get(self.base_url)
        Pages_browsed.append(driver.title)
        Selection_1 = driver.find_element_by_xpath("//a[contains(text(),'Laptops & Ultrabooks')]").text
        print "Main selection"
        print selections_made.append(Selection_1)
        driver.find_element_by_xpath("//a[contains(text(),'Laptops & Ultrabooks')]").click()
        Series_Selected_1=driver.find_element_by_css_selector("li.title.LenovoDo-Medium > a").text
        print "Series selected"
        print Series_Selected_1
        ClusterOfSeriesInterestedIn_1 = driver.find_element_by_css_selector("li.subSeriesLink").text
        print ClusterOfSeriesInterestedIn_1
        Prod_Category_view1 = driver.find_element_by_link_text("T430").text
        print Prod_Category_view1
        driver.find_element_by_link_text("T430").click()
        driver.find_element_by_css_selector("#subseries").text
        driver.find_element_by_xpath("//div[@id='subseries']/div[2]/div/p[3]/a").click()
        View_Prod_Card1 = driver.find_element_by_css_selector("li.item.first").text
        print View_Prod_Card1
        driver.find_element_by_xpath("//a[contains(text(),'Thinkpad Edge E530 (Black)')]").click()
        print driver.title
        Prod_name_view_1=driver.find_element_by_xpath("//form[@id='product_addtocart_form']/div[2]/div/div/h1").text
        print Prod_name_view_1
        Prod_price_view_1=driver.find_element_by_xpath("//span[@id='product-price-233']/span").text
        print Prod_price_view_1
        Prod_view_model_1 = driver.find_element_by_css_selector("div.product-code > h3").text
        print Prod_view_model_1
        Added_to_cart_flag = driver.find_element_by_css_selector("button.button.btn-cart").text
        print Added_to_cart_flag
        driver.find_element_by_css_selector("button.button.btn-cart").click()
        driver.find_element_by_css_selector("div.ajaxcart").click()
        print driver.title
        driver.find_element_by_xpath("id('containerDiv')/div")
        driver.find_element_by_xpath("id('viewcart_button')").click()
        prod_in_cart=driver.find_element_by_xpath("id('shopping-cart-table')/tbody/tr/td[2]/h2/a").text
        print prod_in_cart
        unit_price_in_cart=driver.find_element_by_xpath("id('shopping-cart-table')/tbody/tr/td[3]/span/span").text
        print unit_price_in_cart
        Quantity_in_cart=driver.find_element_by_xpath("id('shopping-cart-table')/tbody/tr/td[4]/input").text
        print Quantity_in_cart
        Proceed_to_payment_clicked=driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/div/div/div[2]/div[2]/ul/li/button")
        print Proceed_to_payment_clicked
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        Page_checkout_flag = driver.find_element_by_css_selector("h1.mw-osc-page-tittle").text
        print Page_checkout_flag        driver.find_element_by_id("billing:firstname").clear()
        driver.find_element_by_id("billing:firstname").send_keys("Ekta")
        driver.find_element_by_id("billing:lastname").clear()
        driver.find_element_by_id("billing:lastname").send_keys("Grover")
        driver.find_element_by_id("billing:company").clear()
        driver.find_element_by_id("billing:company").send_keys("XYZ")
        driver.find_element_by_id("billing:email").clear()
        driver.find_element_by_id("billing:email").send_keys("email-id.com")
        driver.find_element_by_id("billing:street1").clear()
        driver.find_element_by_id("billing:street1").send_keys("XYZ")
        driver.find_element_by_id("billing:city").clear()
        driver.find_element_by_id("billing:city").send_keys("Banglore")
        driver.find_element_by_id("billing:region_id").send_keys("Karnataka")
        driver.find_element_by_id("billing:postcode").clear()
        driver.find_element_by_id("billing:postcode").send_keys("560075")
        driver.find_element_by_id("billing:fax").clear()
        driver.find_element_by_id("billing:fax").send_keys("99")
        driver.find_element_by_id("billing:fax").clear()
        driver.find_element_by_id("billing:fax").send_keys("9980777111")
        Place_order_flag = driver.find_element_by_id("nestepcheckout_place_custom").text
        print Place_order_flag
        driver.find_element_by_id("nestepcheckout_place_custom")
        driver.find_element_by_xpath("//button[@id='nestepcheckout_place_custom']").click()
        print driver.title
        PaymentGateway_reached_flag = driver.find_element_by_name("Visa").text
        print PaymentGateway_reached_flag
        PaymentGatewayReachedFlag = driver.find_element_by_name("MasterCard").text
        print PaymentGateway_reached_flag
        driver.find_element_by_name("Visa").click()
        print driver.title
        reached_final_checkout=driver.find_element_by_xpath("id('paymentDetail')/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]").text
        if reached_final_checkout=="Card Number":
                print "Finished the first simulated webjourney"



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
                       
		

		
		
