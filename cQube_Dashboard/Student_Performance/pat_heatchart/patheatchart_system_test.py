
import unittest

from cQube_Dashboard.Student_Performance.pat_heatchart.Periodic_Assessment_Test_Heat_chart import \
    Periodic_Assessment_Test_Heat_chart
from reuse_func import GetData


class cQube_heatchart_system_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_heatchart_report()


    def test_Catagory_series(self):
        b =Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.viewbys_options()
        self.assertEqual(0,res,msg='View by csv file is not downloaded')
        self.data.page_loading(self.driver)


    def test_subject_levels(self):
        b =Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.subjects_types()
        self.assertEqual(res,0,msg="Subject's csv file is not downloaded")
        self.data.page_loading(self.driver)


    def test_Homebtn_functions(self):
        b = Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.test_homebutton()
        self.assertEqual(res,0,msg='Homebtn is not working')
        self.data.page_loading(self.driver)

    def test_year_selection(self):
        b = Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.test_year_dropdown()
        self.assertEqual(0,res,msg='Year is not selected ')
        self.data.page_loading(self.driver)


    def test_districtwise(self):
        b = Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.District_select_box()
        self.assertEqual(0,res,msg='Some districtwise csv file is not downloaded')
        self.data.page_loading(self.driver)


    def test_clusterwise(self):
        b = Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.Clusters_select_box()
        self.assertEqual(0,res,msg='Some cluster wise csv file is not downloaded ')
        self.data.page_loading(self.driver)

    def test_gradewise_records(self):
        b =Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.grades_files()
        self.assertEqual(0,res,msg='Some grade files are not downloaded')
        self.data.page_loading(self.driver)

    def test_Random_test(self):
        b = Periodic_Assessment_Test_Heat_chart(self.driver)
        res = b.test_randoms()
        self.assertEqual(0,res,msg='Random selection is failed ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()