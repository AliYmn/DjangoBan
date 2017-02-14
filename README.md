Django User Ban Management

# Compatibility

* Django 1.8+
* Python 3.x +

# Installations

    pip install DjangoBan

# Configuration

* Example settings.py : Load the application.
        
          #settings.py
          
          INSTALLED_APPS = [
           ...
           
           'ban',
           
           ]
       
* Example MIDDLEWARE_CLASESS

**ban.middleware.BanManagement**  MIDDLEWARE_CLASESS add.
    
      MIDDLEWARE = [
      ...
        
      'ban.middleware.BanManagement',
        
       ]


* Database Operations

          python manage.py makemigrations
          python manage.py migrate


# Demo

<img src="http://image.prntscr.com/image/ab5fbfb89d7a4ffb9f51f37818ebeea6.png"/>


# How to use?

<img src="http://image.prntscr.com/image/180286313dcd46c28067735d18f5cbc6.png"/>
--------
--------

<img src="http://image.prntscr.com/image/22d7d44c180f4daeaf20f1b6c31fd598.png"/>

# Template Customization

* Ban template : **ban.html**

* Templates included in your application You can create and customize the file named "**ban.html**".
