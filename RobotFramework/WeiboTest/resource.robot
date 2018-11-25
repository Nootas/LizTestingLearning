*** Settings ***
Documentation     weibo resource file
...               Test libraries containing the lowest-level keywords.
...               Resource files with variables and higher-level user keywords.
...               Variable files to provide more flexible ways to create variables than resource files.
...               haven't deal with the identifying code
Library           Selenium2Library
Variables         MyVariables.py

*** Variables ***
${HOST}           weibo.com
${BROWSER}        Chrome
${DELAY1}         6
${DELAY2}         3
${DELAY3}         1
${USER}           yourweibousername
${PASSWORD}       yourweibopassword
${LOGIN_URL}      https://${HOST}
${USER_HOME_PAGE}      https://${HOST}/u/XXXX/home?XXXXX


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Sleep           ${DELAY1}
    Login Page Should Open

Login Page Should Open
     Page Should Contain    帐号登录
     Page Should Contain Element    name:username
     Page Should Contain Element    name:password

Input Username
    [Arguments]      ${USER}
    Input Text       name:username    ${USER}

Input Password
    [Arguments]      ${PASSWORD}
    Input Text       name:password    ${PASSWORD}

Submit LogINFO
    Click Element    xpath://*[@id="pl_login_form"]/div/div[3]/div[6]

Home Page Should Open
    Location Should Be    ${USER_HOME_PAGE}
    Title Should Be       我的首页 微博-随时随地发现新鲜事

Input MSG
    [Arguments]     ${MESSAGE}    ${CURRENT_TIME}
    Input Text      xpath://*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea    ${MESSAGE} at ${CURRENT_TIME}

Click SendBTN
    Click Element    xpath://*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a

Post Success Should Show
    Element Should Be Visible    class:send_succpic
