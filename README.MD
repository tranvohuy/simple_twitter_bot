**Create a Twitter bot for a beginner**

There are many blogs instructing how to build and host a twitter bot. However, most of them are not complete.
For example, some of them  tell us how to type python code to connect to Twitter (via the package Tweepy), but don't tell us how to let the code executes itselft automatically. Some codes on github are old and not applicable anymore.

I see that the following website gives the clearest instruction 
https://tutorials.botsfloor.com/how-to-code-a-simple-twitter-bot-for-complete-beginners-36e37231e67d

Some remarks along the lines of the above blog:
* Twitter does not allow to update two consecutive same statuses.
* We have to install Heroku CLI (and Git, Postgres) in order to use Heroku from command line (cmd).
* I did it in a PC instead of a Mac like the author in the above website.

* Don't need to configure Vars in Heroku website (if you know what it is). All configuration (keys, etc) is saved in ```local_setings.py```
* Open command line (cmd), in the folder containing your code, type ```heroku login```. Follow the instruction to login.
* Then ```git init``` will create a folder ```.git``` (hidden)

* ```git add .```: tell Git to add files
* ```git commit -am "add new stuffs"```: see here https://stackoverflow.com/questions/2745076/what-are-the-differences-between-git-commit-and-git-push

* ```heroku create```: Heroku will create a new app with strange name. You can check it in https://dashboard.heroku.com/apps. For information how to use the command, see https://devcenter.heroku.com/articles/heroku-cli-commands

  * Do ```heroku create``` once for each app. If you accidentally do it twice, go to the folder .git, then check the file ```.config```, change an appropriate name. See more at https://devcenter.heroku.com/articles/git


* ```git push heroku master``` the repository has a "fake" name "heroku". Git push everything to Heroku server. You can change the name to "whatever", then type ```git push whatever```. See more at https://devcenter.heroku.com/articles/git

* ```heroku run worker``` It will run the file specified in the file ```Procfile``` 

