


import unittest

from Locators.parameters import Data
from cQube_Dashboard.Teacher_Professional_Development.usage_course.Diksha_usage_by_course import \
    diksha_usage_course_report

from reuse_func import GetData


class cQube_diskha_course_regression_report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.driver.implicitly_wait(100)
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_course()
            self.data.page_loading(self.driver)


    def test_navigation_from_hamburger(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_course()
        self.data.page_loading(self.driver)
        if 'usage-by-course' in self.driver.current_url:
            print('Home button is working')
        else:
            print("usage-by-course should be display in url ")
            count = count + 1
        self.assertEqual(0,count , msg="Navigatation to diksha couse report is failed ")
        self.data.page_loading(self.driver)

    def test_hyperlink(self):
        b = diksha_usage_course_report(self.driver)
        result = b.test_hyperlink()
        print('Checked with hyper link functionality is working ')
        self.data.page_loading(self.driver)

    def test_overalldownload(self):
        b = diksha_usage_course_report(self.driver)
        res = b.download_csv_file()
        self.assertEqual(0,res,msg='Failed due to mismatch found on content plays')
        self.data.page_loading(self.driver)


    def test_test_course_based_on_last30days(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last30_days()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_last7days(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last7_days()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_lastday(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last_day()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)


    def test_Diksha_homeicon(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_homeicon()
        print("Home icon is working")
        self.data.page_loading(self.driver)


    def test_Diksha_logout(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_logout()
        self.assertEqual(res, 'Log in to cQube', msg="Logout is not working")
        self.data.page_loading(self.driver)


    def test_download_raw_files_overall_period(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_overall_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_last_30days_period(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last_30_days_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_last_7_day_period(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last_7_days_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    def test_download_raw_files_lastday_period(self):
        b = diksha_usage_course_report(self.driver)
        res = b.test_last_day_rawfile_download()
        self.assertEqual(0,res,msg='Raw file is not downloaded')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
