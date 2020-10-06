*** Settings ***
Library    AppiumLibrary

***Test Cases***
Test1
        [Documentation]    login with valid username and invalid password.
        Log    Testcase 1 is started
        Open Application    http://127.0.0.1:4723/wd/hub    automationName=UiAutomator2    deviceName=Pixel    udid=FA6A40301235    platformName=Android    appActivity=com.swaglabsmobileapp.SplashActivity    appPackage=com.swaglabsmobileapp
    Wait Until Page Contains Element    accessibility_id=test-Username    timeout=12    error=None
    Input Text    accessibility_id=test-Username    standard_user
    Input Text    accessibility_id=test-Password    invalidpassword
    Click Element    accessibility_id=test-LOGIN
    Wait Until Page Contains Element    xpath=//android.view.ViewGroup[@content-desc=\"test-Error message\"]/android.widget.TextView    timeout=10    error=None
    Get Element Attribute    xpath=//android.view.ViewGroup[@content-desc=\"test-Error message\"]/android.widget.TextView    text
    Element Name Should Be    xpath=//android.view.ViewGroup[@content-desc=\"test-Error message\"]/android.widget.TextView    Username and password do not match any user in this service.
    Close Application
    Log    Testcase 1 is Passed
