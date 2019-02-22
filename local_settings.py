#These strings can be found in Twitter Dev App.
#Then you can put these strings (KEY and VALUE) in Heroku Config Vars

Consumer_key='' #fill in by yourself

Consumer_secret = ''#Your Consumer Secret Key set in Heroku config

Access_token = ''#Your Twitter API Access Token Key set in Heroku config

Access_token_secret = '' #Your Access Token Secret set in Heroku config

#There are several versions of this file on the internet. 
#For example:
# CONSUMER_KEY= Consumer_key
# ACCESS_KEY = Access_token_key = Access_token
# We should not put this file in public (i.e. github) with the true keys above.
# Another way is to use ".gitignore" and use "from os import environ"
