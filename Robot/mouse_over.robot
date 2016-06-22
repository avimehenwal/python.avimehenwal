*** Settings ***
Library   Selenium2Library

*** Variables ***
${url}    http://www.fashiontofigure.com/
${loc}    css=body > div.wrapper.mm-page > div.nav-wrapper > div > div


*** Test Cases ***
Mouse over test
    Open Browser   ${url}
    Mouse Over     ${loc}
    Set Selenium Implicit Wait   10
