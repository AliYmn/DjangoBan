Django User Ban Management

# Compatibility

* Django 1.8+
* Python 3.x +

# Installations

    pip install DjangoBan

# Configuration

* Example settings.py : Load the application.
        
          #settings.py
            "
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


# Settings.py Configuration

If you want to change the information;

* BAN_MESSAGE : Ban(True) message
* PERMANENT_BAN_MESSAGE : Permanent(True) Message
* BAN_DESCRIPTION : General description

<img src="http://image.prntscr.com/image/ab5fbfb89d7a4ffb9f51f37818ebeea6.png"/>
----------------

Example ;

    #settings.py
    ban_message = "You were banned by administrator."
    permanent_ban_message = "You were unlimited ban by administrator."
    BAN_DESCRIPTION = "Reason: Rule violation."
           

# How to use?

<img src="http://image.prntscr.com/image/180286313dcd46c28067735d18f5cbc6.png"/>
--------
--------

<img src="http://image.prntscr.com/image/ef3b4a29bc9148b9bd1cf46457891f1f.png"/>


* Ban : Bans the user.
* Permanent Ban : Browser Banners.
