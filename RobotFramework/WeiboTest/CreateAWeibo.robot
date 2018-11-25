*** Settings ***
Documentation             create a new weibo
...
...
...
Resource                  resource.robot
Variables                 MyVariables.py

*** Test Case ***
1.weibo login
      Open Browser To Login Page
      Input Username    ${USER}
      sleep             ${DELAY3}
      Input Password    ${PASSWORD}
      sleep             ${DELAY3}
      Submit LogINFO
      sleep             ${DELAY2}
      Home Page Should Open

2.write and send a weibo
      Home Page Should Open
      sleep             ${DELAY2}
      Input MSG         ${MESSAGE}    ${CURRENT_TIME}
      sleep             ${DELAY3}
      Click SendBTN
      sleep             ${DELAY3}
      Post Success Should Show
