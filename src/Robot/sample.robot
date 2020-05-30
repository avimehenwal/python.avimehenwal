*** Settings ***
Library           OperatingSystem
Library           Selenium2Library
Suite Setup       Open Browser And Resize
Suite Teardown    Close Browser

*** Variables ***
${BIN_DIR}     /Users/reflektion/QA/XCheck2/resources
${customer}    http://us.oneill.com/
${browser}     firefox
${rw_title}    css=div.rfk_header
${rfk_sb}      css=#search   

*** Test Cases ***
Iterate over dictionary
    [Documentation]  
    ...             robot --include iterate experiment/sample.robot
    [Tags]  iterate
    Log  

Reflektion experience is on
    [Tags]   sanity
    Wait Until Element Is Visible  ${rfk_sb}   timeout=10
    ${status}   Execute Javascript  return rfk.selected()
    LOG    ${status}
    Log Environment Variables
    Should Be True  ${status}   msg=rfk.selected() status not ok!

Reflektion Title should be present on recommendation widget
    [Tags]   rw 
    Wait Until Element Is Visible   ${rw_title}   timeout=10
    ${title}   Get Text  ${rw_title}
    Log  ${title}
    Should Contain  ${title}  RECOMMEND
    
*** Keywords ***
Open Browser And Resize
    Open Browser   ${customer}   ${browser}
    Set Window Size  ${1200}  ${1000}          
