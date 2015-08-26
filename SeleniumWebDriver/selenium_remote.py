#!/usr/bin/env python
#
# AUTHOR        : avimehenwal
# DATE          : Wed Aug 26 15:42:17 IST 2015
# PURPOSE       : Webdriver general usage for frontend attribute checks
#


import unittest
from selenium import webdriver
from ddt import ddt, data, file_data, unpack
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@ddt
class RecommendationWidget(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://127.0.0.1:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.CHROME)

    @data(
    "http://www.amleo.com/arborrain-hydration-system%252c-32-gallon/p/AR32/", 
    "http://www.andrewchristian.com/index.php/trophy-boy-cap-1.html", 
    "http://www.babyearth.com/joovy-caboose-varylight-stand-on-tandem-stroller.html",
    "http://www.cafebritt.com/gourmet-coffee/merito-cosecha-de-mujer",
    "http://www.converse.com/regular/chuck-taylor-all-star-ii/150145C_030.html",
    "http://www.dreamproducts.com/slippers/adjustable-health-slippers.html",
    "http://www.metalmulisha.com/shop/leo-lace-tri-top/",
    "http://www.gandermountain.com/modperl/product/details.cgi?pdesc=Smith-Wesson-MP-Shield-9-Handgun&i=614497"
    "http://www.oneillclothing.com/shop/birdie-dress/",
    "http://www.overtons.com/modperl/product/details.cgi?pdesc=Overtons-Splash-Island-18L-x-6W&i=844086&r=view",
    "http://www.ruvilla.com/men/footwear/basketball/eqt-bball.html",
    "http://www.thesportshq.com/confidence-txi-heavy-duty-motorised-treadmill.aspx",
    "http://www.tombstonetactical.com/catalog/dpms/rflr-repr-repr-rifle-308win-18in-20rd-coyote/",
    "http://www.uniqlo.com/us/product/men-extra-fine-merino-crew-neck-sweater-131399.html#69"
    "http://apparel.fmfracing.com/shop/don-pullover-hoodie-f33121105/"
    )
    def test_rw_number(self, customer):
        #print "-"*30
        #print "URL : ", customer
        self.driver.get(customer)
        # Wait for other services to load
        self.driver.implicitly_wait(5)
        # using css selector
        # rw = self.driver.find_elements_by_css_selector('div.rfk_rw')
        rw = self.driver.find_element_by_class_name('rfk_rw')
        #print "PAGE TITLE : ", self.driver.title
        #print "No of rfk_rw occourence : ", len(rw)

        if len(rw) > 0:
            #print "Class Name : ", rw[0].get_attribute('class')

            attr_dict = self.driver.execute_script('var items = {};'
               'for (index = 0; index < arguments[0].attributes.length; ++index)'
               '{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value };'
               'return items;', rw[0])

            #print "Attribute_dict : ", attr_dict
            #print attr_dict.keys()
            #self.driver.refresh()
            #print self.driver.get_cookies()

    def tearDown(self):
        self.driver.quit()           # closes all the open windows
        #self.driver.close()          # closes the current window


if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(RecommendationWidget)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
