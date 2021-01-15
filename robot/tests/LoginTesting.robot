*** Settings ***
Suite Setup       Open Browser                ${url}                             ${browser}    # setup to open main page
Suite Teardown    Close Browser               # teardown to close the browser
Test Setup        Set Screenshot Directory    ./Screenshots
Library           SeleniumLibrary

*** Variables ***
${URL}                      http://openncart.herokuapp.com/
${BROWSER}                  chrome

*** Test Cases ***
LoginButtonClick
    Click Element              class=dropdown
    Capture Page Screenshot    dropdown-click.png
    ${dropdown-opened}=        Get Element Attribute                                           css:div#top-links li.dropdown a    aria-expanded
    Log Many                   Dropdown is opened:                                             ${dropdown-opened}
    Run Keyword If             '${dropdown-opened}' == 'true'                                  Click Element                      css:ul.dropdown-menu-right > li:nth-child(2)
    Location Should Be         http://openncart.herokuapp.com/index.php?route=account/login
    Title Should Be            Account Login
    Capture Page Screenshot    login-page-opened.png

LoginAllValid
    Input Text                 name:email                  yura@gmail.com
    Input Text                 name:password               password_123
    Capture Page Screenshot    before-LoginAllValid.png
    Click Button               class=btn-primary
    Title Should Be            My Account
    Capture Page Screenshot    after-LoginAllValid.png