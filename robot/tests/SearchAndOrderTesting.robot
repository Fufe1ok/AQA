*** Settings ***
Suite Setup       Open Browser                ${URL}                             ${BROWSER}    # setup to open main page
Suite Teardown    Close Browser               # teardown to close the browser
Test Setup        Set Screenshot Directory    ./Screenshots
Library           SeleniumLibrary

*** Variables ***
${URL}        http://openncart.herokuapp.com/
${BROWSER}    chrome

*** Test Cases ***
Search
    Maximize Browser Window
    Input Text                                    name:search                                               Macbook
    Click Button                                  class=btn-default
    Click Element                                 xpath=//*[@id="content"]/div[3]/div[2]/div/div[2]/h4/a
    Input Text                                    name:quantity                                             15
    Click Element                                 xpath=//*[@id="button-cart"]
    Capture Page Screenshot                       search-result.png

