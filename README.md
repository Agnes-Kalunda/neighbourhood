# neighbourhood
# HomeWatch
A python application based on Django framework
#### [Agnes-Kalunda] 

# Description    
This is an application that enables a authenticated user to post events for other neighbours to see. A user can click on an a user to view their pages and can also view a list of businesses in the area also can also have access to emergency contacts.


## User Stories
As a user, i would like to;

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
https://github.com/Agnes-Kalunda/neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighborhood 
```
 
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## Technology used  

* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  


## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  



## License 

[MIT](https://choosealicense.com/licenses/mit/)


Copyright (c) 2022 Agnes kalunda

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.