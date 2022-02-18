# ProGroup Group Reservation Manager
ProGroup is a website that allows hotels to keep track and organize their group reservations.   
Users will be able to create/update/delete new Group Profiles and New Reservations based on the Profiles.   
Users also able to see basic statistics and send email to the owner of the website.  
There are two type of users: user and admin.  
Users are able to create/update and delete profiles and reservations but not able to add new users.   
Admin will be able to add new users.   
Login for admin: username: admin password:   
Login for user: username: nikolett password:   
<br>

**View the live site [here](https://progroup-app.herokuapp.com/)**

![Website Mockup Photos](progroup/static/pictures/website-mockup.png)

# Table of Contents
- [Project overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code structure](#code-structure)
    + [Database](#database)
    + [Conceptual Database](#conceptual-database)
    + [MongoDB Database Information](#mongodb-database-information)
  * [Scope](#scope)
    + [User Stories](#user-stories)
    + [User Stories Website Owner](#user-stories-website-owner)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Color Palette](#color-palette)
    + [Typography](#typography)
- [Features](#features)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [APIs](#apis)
  * [Email JS](#email-js)
- [Deployment](#deployment)
  * [Mongo Database](#mongo-database)
  * [Heroku](#heroku)
  * [Local Deployment](#local-deployment)
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
- My project is built using a Blueprints structure
- Flask blueprint is a way to organize a flask application into smaller and re-usable application. 
- Just like a normal flask application, a blueprint defines a collection of views, templates and static assets.
- I found the following videos and website to help my project. 
    - https://www.youtube.com/watch?v=Zcw1cgXwKCg
    - https://prettyprinted.com/
- The project is structured as follows
    - authentication: Contains a flask route for authentication for example login, logout
    - errors: Contains a flask route for error pages for example 404
    - reservation: Contains a flask route for Group reservations, adding, editing etc
    - static
      - css (Project style css)
      - pictures (Project and readme images)
      - js (Project javascript structured into individual files)
    - templates: Html templates to match the routes for Authentication, Email, Errors, Profiles, Reservations,  Users and a base.html file
    - profiles: Contains a flask route for profiles code, adding, editing etc 
    - users: Contains a flask route for users code, adding, editing etc 
    - An app.py that setups, creates and runs the application
    - A local env.py(that is not committed to source control) - This ensures passwords and security-sensitive information are stored in environment variables or in files that
    are in .gitignore, and are never committed to the repository

### Database
- The website is a data-centric one with html, javascript, css used with the materialize framework as a frontend
- The backend consists of Python, flask and jinja templates with a database of a mongodb open-source document-oriented database

#### Conceptual Database

#### MongoDB Database Information

## Scope

### User Stories
### User Stories Website Owner

## Skeleton

### Wireframes

## Surface

### Color palette

- ececec - Light grey colour
### Typography

# Features

# Technologies Used

## Languages

- Html
- Css
- Javascript
- Python
- Jinja

## Libraries and other resources

- JQuery
- Materialize
- Fontawesome
- Heroku
- Flask framework
- Balsamiq
- Google Font
- GitHub
- GitPod
- MongoDB

# Testing

# APIs
## Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid
3. Create an 
 email service in the Email Services section and note the id
4. Create an email template in the Email templates section and note the id
5. Update the script sendEmail.js, method sendMail with your user id, email service id and email template id

# Deployment
There are several applications that need to be configured to run this application locally or on a cloud based service.

## Mongo Database
Mongodb is the database used in the application
1. Create an account at mongodb
2. Create a database cluster
3. Select the cluster, and in the collections section create a database and create 3 collections under the database: reservations, profiles and users
4. In the database access, create a user and allow the user read/write access. Note the username
5. In the network access tab, allow network access from the ip-address of the application connecting to the database
6. In the Databases section click Connect, and select connect your application
7. Note the MONGO_URI, MONGO_DBNAME and user, these parameters are used when deploying locally(env.py file) and deploying on the likes of heroku(config vars)

## Heroku
To deploy this application to Heroku, run the following steps.
1. In the app.py file, ensure that debug is not enabled, i.e. set to True
2. Create a file called ProcFile in the root directory, and add the line <code>web: python app.py</code> if the file does not already exist
3. Create a requirements.txt file by running the command <code>pip freeze > requirements.txt</code> in your terminal if the file doesn't already exist
5. Both the ProcFile and requirements.txt files should be added to your git repo in the root directory
6. Create an account on heroku.com
7. Create a new application and give it a unique name
8. In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo
9. Select the branch for example master and enable automatic deploys if desired. Otherwise, a deployment will be manual
10. The next step is to set the config variables in the Settings section
11. Set key/value pairs for the following keys: IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY
12. Go to the dashboard and trigger a deployment
13. This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app
14. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository syler/MS3-ProGroup-App
3. Click the Code button and copy the HTTPS url, for example: https://github.com/syler11/MS3-ProGroup-App.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/syler11/MS3-ProGroup-App.git```

5. The repository will now be cloned in your workspace
6. Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code><br>
<code>os.environ.setdefault("IP", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("PORT", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_URI", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_DBNAME", TO BE ADDED BY USER)</code><br>
7. Install the relevant packages as per the requirements.txt file
8. Start the application by running <code>python3 app.py</code>

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

Credit to https://codeinstitute.net/ for the lesson on email.js  
Credit to https://favicon.io/favicon-converter/ for the Favicon    
Credit to https://websitemockupgenerator.com/ for the Website mockup picture    
Credit to https://fontawesome.com/ for the Icona displayed on the website    
Credit to https://validator.w3.org/ for the html and css validation  
Credit to https://wave.webaim.org/ for accessibility check for the website  
Credit to https://www.emailjs.com/ for email sending functionality for the website   
Credit to https://www.google.com/ for the Lighthouse report  
Credit to https://stackoverflow.com/ for being a valuabe source for various functions
Credit to https://www.youtube.com/watch?v=Zcw1cgXwKCg & https://prettyprinted.com/ for Flask Blueprint structure


# Content

- Font Awesome (http://fontawesome.com)    
    - The icons used on the site from font awesome

# Media

Photos:

1. hotel_room from Pexels via Pixabay
2. hotel_logo from bridgeoforchy.co.uk website 
3. website-mockup.png from https://websitemockupgenerator.com/

# Acknowledgment

I would like to thank my wife who is also my co-worker who helped me to test the functionalities and gave me ideas how to include certain features. 
I would like to thank my mentor Mo Shami for the guidance and support.
