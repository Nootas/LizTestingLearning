*** Settings ***
Documentation     This is a test of GitHub Valid Login
...
...
...
Resource          resource.robot

*** Test Cases ***
1.Valid Login check
    Open Browser To Login Page
    Input Username    yourgithubusername
    Input Password    yourgithubuserpassword
    Submit LogINFO
    Index Page Should Open
    [Teardown]   Close Browser
