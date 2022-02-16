#Table of Contents
- [Project overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [APIs](#apis)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)



# Project Overview
- ProGroup project is a website that allows users to add/edit/delete Group reservation for submission as milestone project 3 as part of the Code Institute - Diploma in Software Development (Full stack) course. The project based on a real world use when the hotel reservation is able to keep track the various groups arriving in the 2022 seasn. 
- The website is deployed using Heroku pages at the following url: [ProGroup](http://progroup-app.herokuapp.com/)
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/syler11/MS3-ProGroup-App)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices

# UX
## Strategy
### Primary Goal

## Structure
### Website pages

# Features

# Technologies Used

Technologies used:
JQuery
Materialize
Fontawesome
Heroku
Flask framework
Htnl
Css
Javascript
Python
MongoDB

# Testing

# APIs

# Deployment

# Bugs

Bugs:

1. Heroku deployment issue:
I kept getting an error message "failed to push some refs to git@heroku.com" which was due that the Procfile was sitting in the templates foolder instead of the root. After a short research and systematic reference back to the CI modules the issue was indetified and resolved. The heroku deployment was succesful afterwards.
2. Glitch with switch button for is_admin function: the label were name for user and admin but code looking for =="on" therefor the function didn't work properly. Attribute was renamed to == "admin" abd fubction is no working fine. 
3. Login page inputfield label and prefill text were overlapping. Issue solved with placeholder=" " within the input tags. 
4. Populate fileds from exisiting collection into another collection
5. Search by dates
6. Database wasn't registering the PAX and Rooms field value as the field was disabled.

# Credits

# Content

# Media

Photos:

1. hotel_room from Pexels via Pixabay

# Acknowledgment

