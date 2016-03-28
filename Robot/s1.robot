*** Settings ***
Library   Selenium2Library

*** Variables ***
@{PAGES}  http://www.amleo.com/   http://us.oneill.com/shop/womens/ 

*** Test Cases ***
Opening browser pages from Array
    [Teardown]   Close All Browsers
    :FOR  ${PAGE}   IN   @{PAGES}
    \   Log  ${PAGE}
    \   Open Browser  ${PAGE}   firefox
    \   Get Title
    Log   Outside Loop
