#Table of Contents
- [Project overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code structure](#code-structure)
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
The primary goal of the website from the site 
owners perspective is as follows:
- To create/edit/delete profiles so users can add a reservation
- To allow users reservations to a selected profile
- To allow users modify their reservations and / or profiles
- To allow users delete profiles and / or profiles
- To allow users to send messages to the owners
- To view statistics on the usage of the site

The primary goal of the website from a site users perspective is as follows:
- To allow users reservations to a selected profile
- To allow users modify their reservations and / or profiles
- To allow users delete profiles and / or profiles
- To send messages to the owners
- To view statistics on the usage of the site

## Structure
### Website pages
The website contains 18 pages in a logical structure, information and purpose.
1. Home / Landing Page: The first page the user would see when they access the website before they can login to the site.
2. Login: This page allows the user to login to the website. There was no register page added to the landing page to ensure that only authorised personnel could access the website when given access by one of the admin.
3. Reservations: The first page when user would arrive after successful login. It display all the reservation / navigations and some basic statistics of the exsiting reservations. 
4. Add Reservations: This page allows user add new reservation.
5. Edit Reservations: This page allows user to edit existing reservation.
6. Delete Reservations: This page allows user to delete reservation. 
7. Profiles: This contains all the exisitng group profiles in aplhabetical order.
8. Add Profiles: This page allows user add new profiles.
9. Edit Profiles: This page allows user to edit existing profiles.
10. Delete Profiles: This page allows user to delete profiles. 
11. Users: / admin only / This page lists all existing users but visible only for people with admin role. 
12. Add users: This page allows admin users add new users.
13. Edit users: This page allows admin users to edit existing users.
14. Delete users: This page allows admin users to delete users. 
15. Help: This page allows users to send message to the website owner. 
16. Logout: This link allows the user to logout of the site.
17. 404: The 404 error page is displayed if the user enters an incorrect url when accessing the site.
18. 400, 401, 405 and 500: The error page is displayed if the user encounters an error on the site

### Code structure


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

