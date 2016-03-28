*** Settings ***
Library   OperatingSystem
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
    
Get all environment variables
    [Tags]   env
    ${ENV}   Get Environment Variables 
    Log   ${ENV}
    
Some built in variables
    [Tags]   curdir
    Log    ${CURDIR}
    Log    ${TEMPDIR}
    Log    ${/}
    Log    ${:}
    Log     ${EXECDIR}
    ${l}   List Directory   ${EXECDIR}
    Log    ${l}
    ${m}   List Files In Directory   ${EXECDIR}
    Log    ${m}
