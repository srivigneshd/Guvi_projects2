from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from testdatas.testcontent import orange_data
from testlocators.testlocation import orange_locators
import pytest


class Test_project2:
    #Booting method for running the pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    #TESTCASE1:VALIDATION ON ADMIN PAGE:SEARCH
    def test_tc_pim01(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().admin_locators).click()
        searchbox=self.driver.find_element(by=By.XPATH,value=orange_locators().search_locators)
        print("DISPLAY_STATUS OF SEARCHBOX",searchbox.is_displayed())
        searchlist=["Admin","ADMIN","PIM","pim","Leave","LEAVE","Time","TIME","Recruitment","RECRUITMENT","My Info","Performance","Dashboard","Directory","Maintenance","Buzz","BUZZ"]
        for data in searchlist:
            self.driver.find_element(by=By.XPATH,value=orange_locators().search_locators).send_keys(data)
            self.driver.implicitly_wait(5)
            self.driver.refresh()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:USER CAN ABLE TO SEARCH IN ADMIN PAGE MENU")

    #TESTCASE2:VALIDATION OF PAGE HEADERS:DROP DOWN ON ADMIN PAGE
    def test_login2(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().admin_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().usermanagement_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().user_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().userrole_loc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().userstatusloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN).click().perform()
        sleep(5)
        self.driver.back()
        self.driver.find_element(by=By.XPATH,value=orange_locators().userrole_loc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().userstatusloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:USER ROLE AND STATUS ARE VISIBLE")

    #TESTCASE3:CREATION OF NEW EMPLOYEE UNDER PIM
    def test_tc_pim_3(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().addloc).click()
        self.driver.find_element(by=By.NAME,value=orange_locators().empnameloc).send_keys("ashwiniABwc")
        self.driver.find_element(by=By.NAME,value=orange_locators().empname1loc).send_keys("ashwinQABxc")
        self.driver.find_element(by=By.NAME,value=orange_locators().empname2loc).send_keys("ashwinQABcc")
        empid=self.driver.find_element(by=By.XPATH,value=orange_locators().empidloc)
        empid.send_keys(Keys.BACKSPACE)
        empid.send_keys(Keys.BACKSPACE)
        empid.send_keys(Keys.BACKSPACE)
        empid.send_keys(Keys.BACKSPACE)
        empid.send_keys("875403")
        createlogin=self.driver.find_element(by=By.XPATH,value=orange_locators().createloginloc)
        createlogin.click()
        empusername=self.driver.find_element(by=By.XPATH,value=orange_locators().empusernameloc)
        #empusername.clear()
        empusername.send_keys("dh ashwinAAb")
        #self.driver.find_element(by=By.XPATH,value=self.emppasswordloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emppasswordloc).send_keys("Sri@1234")
        #self.driver.find_element(by=By.XPATH,value=self.empconpasswordloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empconpasswordloc).send_keys("Sri@1234")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsaveloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsave1loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsave2loc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:NEW EMPLOYEE CREATION UNDER PIM")

    #TESTCASE4:VALIDATION OF EMPLOYEE PERSONAL DETAILS PAGE POST UNDER CREATION
    def test_tc_pim_4(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).submit()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empid1loc).send_keys("875424")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        #self.driver.find_element(by=By.XPATH,value=self.empsearchloc).submit()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        tablelists=self.driver.find_elements(by=By.XPATH,value=orange_locators().pimpagealldataloc)
        print(len(tablelists))
        table_text_list=[]
        for item in tablelists:
            print(item.is_displayed(),item.text,"Is Displayed",)
            table_text_list.append(item.text)
        print(table_text_list)
        for table in table_text_list:
            self.driver.find_element(by=By.LINK_TEXT,value=table).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE TABS PRESENT IN EMPLOYEE LIST PAGE")
   
    #TESTCASE5:UPDATING EMPLOYEE PERSONAL DETAILS PAGE POST USER CREATION
    def test_tc_pim_5(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).submit()
        # xyz=self.driver.find_elements(by=By.XPATH,value=self.empsearchloc)
        # print(len(xyz))
        # emptylist=[]
        # for item in xyz:
        #     emptylist.append(item.text)
        # print(emptylist)
        # xyz[1].click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnicknameloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnicknameloc).send_keys("sachine")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empotheridloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empotheridloc).send_keys("TN 2345 3456")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdrivingloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdrivingloc).send_keys("TN 345232545")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empid2loc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empid2loc).send_keys("3452")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empssnloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empssnloc).send_keys("345232545")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsinloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsinloc).send_keys("345232545")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empexploc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empexploc).send_keys("1999-12-09")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdobloc).clear()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdobloc).send_keys("1898-12-03")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnationalityloc).click()
        # x=self.driver.find_elements(by=By.XPATH,value=self.empnationalityloc)
        # print(len(x))
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnationality1loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empmartialloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empbloodloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empgenderloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empmilitaryloc).send_keys("NO")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsave4loc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE FILLED DETAILS OF PERSONAL DETAILS PAGE")

    #TESTCASE6:UPDATING EMPLOYEE CONTACT DETAILS PAGE POST USER CREATION
    def test_tc_pim_6(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empcontactloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empstreetloc).send_keys("1/260ramapuram")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empstreet1loc).send_keys("krishnagiri")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empcityloc).send_keys("krishnagiri")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empstateloc).send_keys("TAMIL")
        self.driver.find_element(by=By.XPATH,value=orange_locators().emppostalloc).send_keys("635115")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empcountryloc).send_keys("INDIA")
        #self.driver.find_element(by=By.XPATH,value=self.emphomeloc).send_keys("KRISHNAGIRI")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empmobileloc).send_keys("8754545555")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empworkloc).send_keys("23+3(4)34")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemailloc).send_keys("sri@123.com")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empothermailloc).send_keys("sri@321.com")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsaveconloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE FILLED DETAILS OF CONTACT DETAILS PAGE")
    
    #TESTCASE7:UPDATING EMPLOYEE EMERGENCY CONTACT DETAILS PAGE POST USER CREATION
    def test_tc_pim_7(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empemergencyloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencyaddloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencynameloc).send_keys("trisha")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencyrelationloc).send_keys("wife")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencyhomeloc).send_keys("79988")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencymobileloc).send_keys("677655")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencyteleloc).send_keys("6655")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empemergencysaveloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empemergencyloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE FILLED DETAILS OF EMERGENCY CONTACT DETAILS PAGE")
    

    #TESTCASE8:UPDATING EMPLOYEE DEPENDENTS CONTACT DETAILS PAGE POST USER CREATION
    def test_tc_pim_8(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empdependentloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdependentaddloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdepdentnameloc).send_keys("arul")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdepentdobloc).send_keys("1999-02-04")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdependentrelaloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empdependentsaveloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE FILLED DETAILS OF EMPLOYEE DEPENDENTS CONTACT DETAILS PAGE")
        
    #TESTCASE9:UPDATING EMPLOYEE JOB DETAILS PAGE
    def test_tc_pim_9(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empjobloc).click()
        #self.driver.find_element(by=By.XPATH,value=self.empjobjoinloc).clear()
        #self.driver.find_element(by=By.XPATH,value=self.empjobjoinloc).send_keys("1999-02-02")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobtitleloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobcateloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobsubunitloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjoblocationloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobempstatusloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        x=self.driver.find_element(by=By.XPATH,value=orange_locators().empjobcontractloc)
        action=ActionChains(self.driver)
        action.click(on_element=x).perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobconstartloc).send_keys("1999-02-03")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobconendloc).send_keys("2001-02-03")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobconsaveloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE ALL THE FILLED DETAILS OF JOB DETAILS PAGE")

    #TESTCASE10:UPDATING EMPLOYEE JOB DETAILS PAGE
    def test_tc_pim_10(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empjobloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empjobterminateloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empterdate).send_keys("1999-02-01")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empterenddate).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptersave).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS:ABLE TO SEE TERMINATION ON JOB DETAILS PAGE")
        
    #TESTCASE11:UPDATING EMPLOYEE JOB ACTIVATION ON JOB DETAILS PAGE
    def test_tc_pim_11(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empjobloc).click()
        assert self.driver.title=="OrangeHRM"
        print("ACTIVATE EMPLOYMENT LINK IS NOT AVAILABLE")

    #TESTCASE12:UPDATING EMPLOYEE SALARY ON SALARY COMPONENT PAGE
    def test_tc_pim_12(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().empsalaryloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryaddloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarycomponentloc).send_keys("123")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarypaygrade).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarypayfrq).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarycurrency).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarycurrency).send_keys("4000")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarycomment).send_keys("salary is paid")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryddloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryaccnoloc).send_keys("123")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryrouloc).send_keys("345")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryamt1loc).send_keys("4000")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalaryacctypeloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsalarysaveloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS: ABLE TO SEE SALARY AND DEPOSIT ON SALARY DETAILS PAGE")
    
    #TESTCASE13:UPDATING EMPLOYEE SALARY ON TAX EXEMPTIONS PAGE
    def test_tc_pim_13(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_locators).send_keys(orange_data().username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_locators).send_keys(orange_data().password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submitbutton_locators).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pimloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emplistloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empnamelocsearch).send_keys("ashwin")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empsearchloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empenterloc).click()
        self.driver.find_element(by=By.LINK_TEXT,value=orange_locators().emptaxloc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxstatusloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxexceploc).send_keys("1")
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxstateloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxstatusloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxexcep1loc).send_keys("2")
        self.driver.find_element(by=By.XPATH,value=orange_locators().empunemploc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().empworkstateloc).click()
        action=ActionChains(self.driver)
        action.send_keys(Keys.DOWN,Keys.DOWN).click().perform()
        self.driver.find_element(by=By.XPATH,value=orange_locators().emptaxsaveloc).click()
        assert self.driver.title=="OrangeHRM"
        print("SUCCESS: ABLE TO SEE TAX EXEMPTION FILLED DETAILS")
