# Table of Contents
- [Testing](#testing)
- [Code Validators and Website Analysis](#code-validators-and-website-analysis)
  * [HTML Markup Validation Service](#html-markup-validation-service)
  * [CSS Validation Service](#css-validation-service)
  * [Chrome Dev tools Lighthouse](#chrome-dev-tools-lighthouse)
    + [Desktop](#desktop)
    + [Mobile](#mobile)
  * [Wave Accessibility](#wave-accessibility)
  * [JSHint](#jshint)
  * [PEP8online](#pep8online)

# Testing

## Bugs during the testing
1. Aria labelledby buttons were missing
2. div and from tags in the wrong order
3. hotel logo wasn't resized to minimum 
4. let were cahnged var to pass js hint validation without warnings
5. ```var $ = window.$;``` was added to script to avoid linting errorsby js hint validation

# Code Validators and Website Analysis

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
authentication/login.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/login_html_validation.png)  
authentication/account.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/account_html_validation.png)  
email/contact.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/contact_html_validation.png)  
errors/404.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/404_html_validation.png)  
profiles/add_profile.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/add_profile_html_validation.png)  
profiles/edit_profile.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/edit_profile_html_validation.png)  
profiles/profiles.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/profiles_html_validation.png)  
reservations/add_reservation.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/add_reservation_html_validation.png)  
reservations/edit_reservation.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/edit_reservation_html_validation.png)  
reservations/reservations.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/reservations_html_validation.png) 
users/add_user.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/add_user_html_validation.png)  
users/edit_user.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/edit_user_html_validation.png)  
users/users.html | Passed, No errors found | [Results](progroup/static/pictures/html_validation/users_html_validation.png)  

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
style.css | Passed, No errors found | [Results](progroup/static/pictures/css_validation/style_css_validation.png)

## Chrome Dev tools Lighthouse 

- I used Lighthouse (https://developers.google.com/web/tools/lighthouse) to test the performance, seo, best practices and accessibility of the site

### Desktop
Page | Result 
------------ | ------------- 
authentication/login.html | [Results](progroup/static/pictures/lighthouse_validation/login_desktop_validation.png)  
authentication/account.html | [Results](progroup/static/pictures/lighthouse_validation/account_desktop_validation.png)  
email/contact.html | [Results](progroup/static/pictures/lighthouse_validation/contact_desktop_validation.png)  
errors/404.html | [Results](progroup/static/pictures/lighthouse_validation/404_desktop_validation.png)  
profiles/add_profile.html | [Results](progroup/static/pictures/lighthouse_validation/add_profile_desktop_validation.png)  
profiles/edit_profile.html | [Results](progroup/static/pictures/lighthouse_validation/edit_profile_desktop_validation.png)  
profiles/profiles.html | [Results](progroup/static/pictures/lighthouse_validation/profiles_desktop_validation.png)  
reservations/add_reservation.html | [Results](progroup/static/pictures/lighthouse_validation/add_reservation_desktop_validation.png)  
reservations/edit_reservation.html | [Results](progroup/static/pictures/lighthouse_validation/edit_reservation_desktop_validation.png)  
reservations/reservations.html | [Results](progroup/static/pictures/lighthouse_validation/reservations_desktop_validation.png) 
users/add_user.html | [Results](progroup/static/pictures/lighthouse_validation/add_user_desktop_validation.png)  
users/edit_user.html | [Results](progroup/static/pictures/lighthouse_validation/edit_user_desktop_validation.png)  
users/users.html | [Results](progroup/static/pictures/lighthouse_validation/users_desktop_validation.png)  
<br>


### Mobile
Page | Result 
------------ | ------------- 
authentication/login.html | [Results](progroup/static/pictures/lighthouse_validation/login_mobile_validation.png)  
authentication/account.html | [Results](progroup/static/pictures/lighthouse_validation/account_mobile_validation.png)  
email/contact.html | [Results](progroup/static/pictures/lighthouse_validation/contact_mobile_validation.png)  
errors/404.html | [Results](progroup/static/pictures/lighthouse_validation/404_mobile_validation.png)  
profiles/add_profile.html | [Results](progroup/static/pictures/lighthouse_validation/add_profile_mobile_validation.png)  
profiles/edit_profile.html | [Results](progroup/static/pictures/lighthouse_validation/edit_profile_mobile_validation.png)  
profiles/profiles.html | [Results](progroup/static/pictures/lighthouse_validation/profiles_mobile_validation.png)  
reservations/add_reservation.html | [Results](progroup/static/pictures/lighthouse_validation/add_reservation_mobile_validation.png)  
reservations/edit_reservation.html | [Results](progroup/static/pictures/lighthouse_validation/edit_reservation_mobile_validation.png)  
reservations/reservations.html | [Results](progroup/static/pictures/lighthouse_validation/reservations_mobile_validation.png) 
users/add_user.html | [Results](progroup/static/pictures/lighthouse_validation/add_user_mobile_validation.png)  
users/edit_user.html | [Results](progroup/static/pictures/lighthouse_validation/edit_user_mobile_validation.png)  
users/users.html | [Results](progroup/static/pictures/lighthouse_validation/users_mobile_validation.png)  
<br>

## Wave Accessibility
* Wave accessibility(https://wave.webaim.org/) was used to test the websites accessibility

authentication/login.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/login_html_validation.png)  
authentication/account.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/account_html_validation.png)  
email/contact.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/contact_html_validation.png)  
errors/404.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/404_html_validation.png)  
profiles/add_profile.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/add_profile_html_validation.png)  
profiles/edit_profile.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/edit_profile_html_validation.png)  
profiles/profiles.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/profiles_html_validation.png)  
reservations/add_reservation.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/add_reservation_html_validation.png)  
reservations/edit_reservation.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/edit_reservation_html_validation.png)  
reservations/reservations.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/reservations_html_validation.png) 
users/add_user.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/add_user_html_validation.png)  
users/edit_user.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/edit_user_html_validation.png)  
users/users.html | 0 errors and 0 contrast errors | [Results](progroup/static/pictures/wave_accessibility_validation/users_html_validation.png)  )

## JSHint
* JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
js/calculation.js |  errors, 0 warnings | [Results](progroup/static/pictures/js_validation/calculation_js_validation.png)  
js/email.js |  errors, 0 warnings | [Results](progroup/static/pictures/js_validation/email_js_validation.png)  
js/script.js |  errors, 0 warnings | [Results](progroup/static/pictures/js_validation/script_js_validation.png)  

## PEP8online
* PEP8online was used to analyse the Python files (https://pep8online.com/)

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
js/calculation.js |  errors, 0 warnings | [Results](progroup/static/pictures/js_validation/calculation_js_validation.png) 

 