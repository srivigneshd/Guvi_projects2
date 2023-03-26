# locators of OrangeHRM for PROJECT2
class orange_locators:

    #test case 1 and constructor loc
    username_locators="username"            #name
    password_locators="password"            #name
    submitbutton_locators="//button[normalize-space()='Login']"     #XPATH
    #admin_locators="//a[@class='oxd-main-menu-item active']"        #XPATH
    admin_locators="/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]"
    search_locators="//input[@placeholder='Search']"                #XPATH
    
    #test case 2

    usermanagement_loc="//span[normalize-space()='User Management']"
    #usermanagement_loc="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"
    #usermanagement_loc="/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]"    #XPATH
    #user_loc="(//a[normalize-space()='Users'])[1]"#XPATH  /html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a
    user_loc='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
    #userrole_loc="(//div[@class='oxd-select-text oxd-select-text--active'])[1]" #XPATH
    #userrole_loc="//*[@class='oxd-select-text oxd-select-text--active' and @xpath='1']" #xpath 
    userrole_loc="(//div[contains(text(),'-- Select --')])[1]"
    #useradmin_loc="(//div[@class='oxd-select-text-input'][normalize-space()='Admin'])[1]"
    userstatusloc='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    useradmin_loc='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    #statusloc="//div[@class='oxd-select-text oxd-select-text--focus']"
    status1loc="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/div[1]/div[1]"


    
    #test case 3

    #pimloc="//a[@class='oxd-main-menu-item active']"  #XPATH
    pimloc="(//span[normalize-space()='PIM'])[1]"
    #addloc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]"    #xpath
    addloc="//button[normalize-space()='Add']"
    #createloginloc="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    createloginloc="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span"
    empnameloc="firstName" #name
    empname1loc="middleName"#name
    empname2loc="lastName"#name 
    empidloc="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    imgloc="//img[@class='employee-image']"
    empusernameloc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]"
    #emppasswordloc="//input[@class='oxd-input oxd-input--active oxd-input--error']"
    emppasswordloc="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"
    #empconpasswordloc="//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    empconpasswordloc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]"
    empsaveloc="//button[normalize-space()='Save']"
    #empsave1loc="(//button[@type='submit'][normalize-space()='Save'])[1]"
    empsave1loc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/button[1]"
    empsave2loc="(//button[@type='submit'][normalize-space()='Save'])[2]"
    empsave2loc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/button[1]"


    #test case4 data and locators

    #emplistloc="//li[@class='oxd-topbar-body-nav-tab --visited']"
    emplistloc="(//li[@class='oxd-topbar-body-nav-tab --visited'])[1]"
    empnamelocsearch="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    empid1loc="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    empsearchloc="//div[@class='oxd-form-actions']/button"
    #empsearchloc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"
    #empsearchloc='//button[@type="submit"]'
    empenterloc="//div[@class='oxd-table-card']"
    #empenterloc="(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]"
    pimpagealldataloc="//div[@class='orangehrm-tabs']//a"
    empnicknameloc="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[2]//div[1]//div[1]//div[2]//input[1]"
    empotheridloc="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[1]/div[2]/div[1]/div[2]/input[1]"
    empdrivingloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
    empssnloc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    empsinloc='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    #empsinloc='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]'
    empid2loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    empexploc="(//input[@placeholder='yyyy-mm-dd'])[1]"
    empdobloc="(//input[@placeholder='yyyy-mm-dd'])[2]"
    empnationalityloc="(//div[@class='oxd-select-wrapper'])[1]"
    empnationality1loc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    empmartialloc="(//div[@class='oxd-select-wrapper'])[2]"
    empbloodloc="(//div[@class='oxd-select-wrapper'])[3]"
    empgenderloc="//label[normalize-space()='Male']"
    empmilitaryloc="(//input)[15]"
    empsave3loc="(//button[@type='submit'][normalize-space()='Save'])[1]"
    empsave4loc="(//button[@type='submit'][normalize-space()='Save'])[2]"

    #test case 6

    empcontactloc='Contact Details'
    #empstreetloc="(//input[@class='oxd-input oxd-input--active'])[2]"
    empstateloc="//div[4]//div[1]//div[2]//input[1]"
    #empstreet1loc="(//input[@class='oxd-input oxd-input--active'])[3]"
    empstreetloc="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[1]//div[1]//div[2]//input[1]"
    empstreet1loc="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[2]//div[1]//div[2]//input[1]"
    empcityloc="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[3]//div[1]//div[2]//input[1]"
    empstateloc="(//input[@class='oxd-input oxd-input--active'])[5]"
    emppostalloc="(//input[@class='oxd-input oxd-input--active'])[6]"
    empcountryloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"
    emphomeloc="(//input[@class='oxd-input oxd-input--active'])[7]"
    empmobileloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"
    empworkloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"
    empemailloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input"
    empothermailloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input"
    empsaveconloc="//button[@type='submit']"

    #test case 7

    empemergencyloc="Emergency Contacts"
    empemergencyaddloc="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/div[@class='orangehrm-action-header']/button[1]"
    empemergencynameloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"
    empemergencyrelationloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"
    empemergencyhomeloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"
    empemergencymobileloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"
    empemergencyteleloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"
    empemergencysaveloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]"
    #empemergencyenterloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]"


    #test case 8

    empdependentloc="Dependents"
    empdependentaddloc="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button"
    #empdependentbrowseloc="//div[@class='oxd-file-button']"
    empdepdentnameloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"
    empdependentrelaloc="//div[@class='oxd-select-text oxd-select-text--active']//div[1]"
    empdepentdobloc="//div[@class='oxd-date-wrapper']//div[1]//input[1]"
    empdependentsaveloc='//button[@type="submit"]'
    
    #test case 9

    empjobloc='Job'
    empjobjoinloc="(//input[@placeholder='yyyy-mm-dd'])[1]"
    #empjobjoinloc="(//input[@placeholder='dd-mm-yyyy'])[1]"
    #empjobtitleloc="(//div[contains(text(),'-- Select --')])[1]"
    empjobtitleloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"
    empjobcateloc='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]'
    #empjobcateloc="(//div[contains(text(),'-- Select --')])[2]"
    empjobsubunitloc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]"
    #empjobsubunitloc="(//div[contains(text(),'-- Select --')])[3]"
    #empjoblocationloc="(//div[contains(text(),'-- Select --')])[4]"
    empjoblocationloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[1]/div[1]"
    empjobempstatusloc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]"
    #empjobempstatusloc="(//div[contains(text(),'-- Select --')])[5]"
    #empjobcontractloc="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    empjobcontractloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span"
    #empjobcontractloc="(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]"
    empjobconstartloc="//div[3]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]"
    empjobconendloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input"
    empjobconsaveloc="//button[normalize-space()='Save']"
    
    #test case10
    empjobterminateloc="//button[normalize-space()='Terminate Employment']"
    empterdate="//div[@role='document']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@placeholder='yyyy-mm-dd']"
    empterenddate="//div[@role='document']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div[@class='oxd-select-text oxd-select-text--active']"
    emptersave="//div[@role='document']//button[@type='submit'][normalize-space()='Save']"

    #test case 12

    empsalaryloc="Salary"
    #empsalaryaddloc="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/div[@class='orangehrm-action-header']/button[1]"
    empsalaryaddloc="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/div[@class='orangehrm-action-header']/button[@type='button'][normalize-space()='Add']/i[1]"    
    empsalarycomponentloc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    empsalarypaygrade='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]'
    empsalarypayfrq='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]'
    empsalarycurrency='//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]'
    empsalaryamtloc="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/input[1]"
    empsalarycomment="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea[1]"
    empsalaryddloc="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/label[1]/span[1]"
    empsalaryaccnoloc="//div[4]//div[1]//div[1]//div[1]//div[2]//input[1]"
    empsalaryrouloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input"
    empsalaryamt1loc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input"
    empsalaryacctypeloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]"
    empsalarysaveloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]"

    #test case 13

    emptaxloc="Tax Exemptions"
    emptaxstatusloc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    #emptaxstatusloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]"
    #emptaxstatusloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    emptaxexceploc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"
    emptaxstateloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]"
    emptaxstatus1loc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]"
    emptaxexcep1loc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"
    empunemploc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]"
    empworkstateloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]"
    emptaxsaveloc="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button"
