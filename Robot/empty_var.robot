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
