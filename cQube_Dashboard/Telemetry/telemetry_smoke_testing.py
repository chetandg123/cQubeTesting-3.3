import time
import unittest
from Locators.parameters import Data
from cQube_Dashboard.Telemetry.telemetry_details_report import telemetry_map_report

from get_dir import pwd
from reuse_func import GetData


class Test_Telemetry(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_telemetry()
        time.sleep(3)

    def test_navigate_to_telemetry(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.back()
        self.data.page_loading(self.driver)
        if "dashboard" in self.driver.current_url:
            print("cqube landing page is displayed")
        else:
            print("homebutton is not working ")
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_telemetry()
        self.assertEqual(0,count,msg='Homebtn is not worked ')
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_navigate_by_dashboard(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        if '' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0,count,msg='Telemetry page is not displayed')
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_click_on_blocks(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on block level ")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)


    def test_click_on_cluster(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on cluster level ")
        self.data.page_loading(self.driver)
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_click_on_school(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count, msg="Markers not present on cluster level ")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)


    def test_homeicon(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)


    def test_clickon_homebtn(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0, count, msg='Telemetry page is not displayed')
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)



    def test_logout(self):
        self.data.page_loading(self.driver)
        self.driver.back()
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(5)
        self.assertEqual('Log in to cQube',self.driver.title,msg="logout is not working ")
        self.data.login_cqube(self.driver)
        time.sleep(2)
        print("url of page: ",self.driver.current_url)
        self.data.navigate_to_telemetry()
        time.sleep(2)
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is displayed")
        else:
            print('Failed to navigate to telemetry report page ')
        self.data.page_loading(self.driver)


    def test_last7day_download(self):
        b =telemetry_map_report(self.driver)
        res = b.test_last_7_records()
        self.assertTrue(res,msg="last7day's csv file is not downloaded")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_lastday_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastday_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_overall_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_overall_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_lastmonth_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastmonth_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.back()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()