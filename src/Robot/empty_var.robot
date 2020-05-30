*** Settings ***


*** Variables ***
${var1}   hello variable
${var2}     

*** Test Cases ***
test variable 1
    Log   ${var1}

test variable 2
    Log   ${var2}

Get all scope variables
    ${vars}   Get Variables
    Log    ${vars}

empty variable check
    ${a}   Variable Should Not Exist  ${var3}
    Log   ${a}
    ${b}   Variable Should Exist  ${var1}
    Log   ${b}

Run keyword is variable exists
    Run Keyword If   $var2==""   Log  ${var2}

Run keyword is variable do not exists
    Run Keyword If   $var1==""   Log  ${var1}

Nul variable check and conditional kw execution
    ${exists}=  Set Variable If  $var2==''   ${False}  ${True}
    Log  ${exists}
    ${exists}=  Set Variable If  $var2=='XYZ'   ${False}  ${True}
    Log  ${exists}
