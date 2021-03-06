




import unittest

from cQube_Dashboard.Teacher_Professional_Development.tpd_enrollment.tpd_enrollment_completion import \
    tpd_enrollment_completion_reports
from reuse_func import GetData


class cQube_enrollment_systemtest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(200)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_enrollment_report()
        self.data.page_loading(self.driver)


    def test_tpd_enrollment_icon(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res = b.test_enrollment_icon()
        self.assertEqual(0,res,msg="Completion icon is not working ")
        self.data.page_loading(self.driver)

    def test_Enrollment_time_periods_overall(self):
        b=tpd_enrollment_completion_reports(self.driver)
        res,res1 = b.test_Enrollment_overall()
        self.assertNotEqual(0,res,msg='Collection names are empty')
        self.assertEqual(res1,0,msg="Enrollment Overall csv file is not downloaded ")
        self.data.page_loading(self.driver)

    def test_Enrollment_time_periods_lastday(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res1 = b.test_Enrollment_last_day()
        # self.assertNotEqual(0, res, msg='Collection names are empty')
        # self.assertEqual(res1, 0, msg="Enrollment lastday csv file is not downloaded ")
        self.data.page_loading(self.driver)

    def test_Enrollment_time_periods_last7day(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res1 = b.test_Enrollment_last7_days()
        # self.assertNotEqual(0, res, msg='Collection names are empty')
        # self.assertEqual(res1, 0, msg="Enrollment last7 days csv file is not downloaded ")
        self.data.page_loading(self.driver)

    def test_Enrollment_time_periods_last30day(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res1 = b.test_Enrollment_last30_days()
        # self.assertNotEqual(0, res, msg='Collection names are empty')
        # self.assertEqual(res1, 0, msg="Enrollment last30 days csv file is not downloaded ")
        self.data.page_loading(self.driver)



    def test_Click_download_icon(self):
        b  = tpd_enrollment_completion_reports(self.driver)
        res = b.test_check_download_icon()
        self.assertEqual(res,0,msg='Districtwise csv file is not downloaded')
        print('Enrollment count is correctly displaying')
        self.data.page_loading(self.driver)

    def test_districtwise_records(self):
        b =tpd_enrollment_completion_reports(self.driver)
        res = b.test_coursetype_with_all_districts()
        self.assertEqual(0,res,msg='Some district csv file is not downloaded')
        print("Districtwise csv file is downloading")
        self.data.page_loading(self.driver)

    def test_blockwise_records(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res = b.test_coursetype_with_all_blockwise()
        self.assertEqual(0, res, msg='Some Blocks csv file is not downloaded')
        print('Blockwise csv file is downloading')
        self.data.page_loading(self.driver)

    def test_clusterwise_records(self):
        b = tpd_enrollment_completion_reports(self.driver)
        res = b.test_coursetype_with_all_clusterwise()
        self.assertEqual(0, res, msg='Some Cluster csv file is not downloaded')
        print('Clusterwise csv file is downloaded')
        self.data.page_loading(self.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()