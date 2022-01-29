Bugs:

1. Heroku deployment issue:
I kept getting an error message "failed to push some refs to git@heroku.com" which was due that the Procfile was sitting in the templates foolder instead of the root. After a short research and systematic reference back to the CI modules the issue was indetified and resolved. The heroku deployment was succesful afterwards.
2. Glitch with switch button for is_admin function: the label were name for user and admin but code looking for =="on" therefor the function didn't work properly. Attribute was renamed to == "admin" abd fubction is no working fine. 
3. Login page inputfield label and prefill text were overlapping. Issue solved with placeholder=" " within the input tags. 

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

Photos:

1. hotel_room from Pexels via Pixabay
