*** Settings ***
Documentation      A resource file with Keywords and Varieties
...                
...
...
Library            Selenium2Library

*** Variables ***
${HOST}            github.com
${BROWSER}         Chrome
${DELAY}           1
${VALID USER}      yourgithubusername
${VALID PASSWORD}  yourgithubuserpassword
${LOGIN URL}       https://${HOST}/login
${INDEX URL}       https://${HOST}/
${ERROR URL}       https://${HOST}/session

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}   ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Open

Login Page Should Open
    Title Should Be    Sign in to GitHub · GitHub

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Open

Input Username
    [Arguments]    ${username}
    Input Text    id:login_field    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id:password    ${password}

Submit LogINFO
    Click Button    name:commit

Index Page Should Open
    Location Should Be    ${INDEX URL}
    Title Should Be    GitHub

Error Page Should Open
    Location Should Be    ${ERROR URL}
    Element Should Contain   id : js-flash-container    Incorrect username or password.
