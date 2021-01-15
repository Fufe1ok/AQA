*** Settings ***
Suite Setup       Open Browser                ${url}                             ${browser}    # setup to open main page
Suite Teardown    Close Browser               # teardown to close the browser
Test Setup        Set Screenshot Directory    ./Screenshots
Library           SeleniumLibrary

*** Variables ***
${URL}        http://openncart.herokuapp.com/
${BROWSER}    chrome

*** Test Cases ***
RegisterButtonClick
    Click Element              class=dropdown
    Capture Page Screenshot    dropdown-click.png
    ${dropdown-opened}=        Get Element Attribute                                              css:div#top-links li.dropdown a    aria-expanded
    Log Many                   Dropdown is opened:                                                ${dropdown-opened}
    Run Keyword If             '${dropdown-opened}' == 'true'                                     Click Element                      css:ul.dropdown-menu-right > li:first-child
    Location Should Be         http://openncart.herokuapp.com/index.php?route=account/register
    Title Should Be            Register Account
    Capture Page Screenshot    register-page-opened.png

RegisterFirstNameInput
    Input Text       name:firstname                                             Yura
    Input Text       name:lastname                                              Paneiko
    Input Text       name:email                                                 yura@gmail.com
    Input Text       name:telephone                                             0630275662
    Input Text       name:address_1                                             Lviv
    Input Text       name:city                                                  Lviv
    Input Text       name:postcode                                              79019
    Input Text       name:lastname                                              Paneiko
    Click Element    name:zone_id
    Click Element    css:#input-zone > option:nth-child(5)
    Input Text       name:password                                              password_123
    Input Text       name:confirm                                               password_123
    Click Element    name:agree                                                 
    Click Element    css:#content > form > div > div > input.btn.btn-primary


