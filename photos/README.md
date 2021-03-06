# Gallery

## Author
 Lorna Kirui

### Description  
This is a web application that enables users to view different categories of images per locations and also anable them to copy the link and share it to other friends

### Deployed link

 https://lornas-gallery.herokuapp.com/

### Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/LornaMoringa/Gallery
```
##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photos
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
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.3](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Git](for version control)
  
## Known Bugs  
* There are no known bugs currently,though i encountered many of it during deployment,but i finally managed 
  
## Contact Information   
If you have any question or contributions, please email me at [lornakirui023@gmail.com] 


## License
 
 Licensed under[MIT license](https://github.com/kiptoo-097/Blog-App/blob/master/LICENSE.md)
