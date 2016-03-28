*** Settings ***
Library           Selenium2Library
Suite SetUp       Open Browser   http://us.oneill.com/    firefox
Suite Teardown    Close Browser

*** Variables ***
${rw_products}   css=ul.rfk_products
${rw_p1}   css=ul.rfk_products > li:nth-child(1)
${rw_p2}   css=ul.rfk_products > li:nth-child(2)

 ul.rfk_products > li:nth-child(2)
*** Test Cases ***
Test recommendation product list is not empty
    ${v}   Element Should Be Visible   ${rw_products}
    Log   ${v}

If first products are visible
    Get Webelement     ${rw_p1}
    ${c}    Get Element Attribute        ${rw_p1}@class
    Log     ${c}
    Run Keyword If  'rfk_buffer' in "${c}"    Element Should Not Be Visible    ${rw_p1}
    Run Keyword If  'rfk_buffer' not in "${c}"    Element Should Be Visible    ${rw_p1}


If second products are visible
    Get Webelement     ${rw_p2}
    ${c}    Get Element Attribute        ${rw_p2}@class
    Log     ${c}
    Run Keyword If  'rfk_buffer' in "${c}"    Element Should Not Be Visible    ${rw_p2}
    Run Keyword If  'rfk_buffer' not in "${c}"    Element Should Be Visible    ${rw_p2}


*** Keywords ***
Is rfk_buffer
    [Arguments]    ${str}
    Should Contain   ${str}   rfk_buffer 
