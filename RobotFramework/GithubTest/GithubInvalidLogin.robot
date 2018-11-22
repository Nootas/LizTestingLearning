*** Settings ***
Documentation    This is a negtive test for github login
...
...
...
Suite Setup      Open Browser To Login Page
Suite Teardown   Close Browser
Test Setup       Go To Login Page
Test Template    Login With Invalid Account Should Fail
Resource         resource.robot

*** Keywords ***
Login With Invalid Account Should Fail
    [Arguments]    ${username}   ${password}
    Input Username    ${username}
    Input Password    ${password}
    Submit LogINFO
    Error Page Should Open

*** Testcase ***                      Username         Password
Invalid Username And Password         invalid          invalid
Invalid Username                      invalid          ${VALID PASSWORD}
Invalid Password                      ${VALID USER}    invalid
Empty Username                        ${EMPTY}         ${VALID PASSWORD}
Empty Password                        ${VALID USER}    ${EMPTY}
Empty Username and Password           ${EMPTY}         ${EMPTY}
