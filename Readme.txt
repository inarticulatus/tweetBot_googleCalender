TweetBot with google calender Windows.


The bot is not a high end AI bot that would talk to you. This is a project under development
This project is build to explain working of twitter libraries, python language, google api and integrating the two.

We will be using a python library called twython and google calender api for the bot

Python is used due to its simple yet powerful language. 
However the method to much extent remains same in other languages, except of course the syntax and the dependencies.


1. Setting up Python


[1.1] Installing Python, its Dependencies and tweeter libraries
 
 This application is compatible with Python versions 2.7 and above(3.4.3 at time of writing the readme).
 Assuming that you have installed Python and included it in the PATH variable at the time of installation of Python.
 IF YES THEN SKIP THE FOLLOWING STEP [1.1.1]


 [1.1.1] If you have installed python but not included in the PATH variable then follow the next step:

        * Hold Win and press Pause .
        * Click Advanced System Settings.
        * Click Environment Variables.
	* Append ;C:\pythonXX to the Path variable.(replace XX with your python directory)
	* Restart Command Prompt.




 [1.2] It is crucial that you have pip installed for the next step. Good news! python 2.7.9 and above come with pip installed.

 [1.3] Open command prompt and type in the command

	> pip install twython	
        This will install the twython library
	
	> pip install google-api-python-client
	The google calendar API

That's all for first step.


2. Setting up the bot

 [2.1] Creating a twitter account.I will assume that you have not been in cryosleep since 2006 or have not come from another space time or dimension and know how to setup an account on twitter

 [2.2] Attaining developer account options for twitter
 You will need developer access to your account if you want to use it via a script.
 Follow along to get the developer access. 
	
        * Go to apps.twitter.com
	* Click on the ‘Create New App’ button.
	* Fill out the details on the form. You have to give your app a name, description, and 	 website (this can be a simple place holder, like http://www.example.com. Change it to the future              website you may hold or even your github site.)
	* Read the Developer Agreement, and check the box at the bottom if you agree. 
	* Then click on the ‘Create your Twitter application’ button.

 [2.3] Getting the keys and tokens to give the bot access to your account

 This is an important step, as you will need the keys and access tokens for you app. They allow you to sign in to your account via a Python script.

 After creating your new app go to apps.twitter.com and click on your apps name.
 On the app’s page, click on the ‘Keys and Access Tokens’ page.
 At the bottom of this page, click on the ‘Create my access token’ button.
 Make sure you make note of the following four keys, as you will need these later. Make sure nobody else can access them.


	* Consumer Key (API Key)	[ copy this value from Consumer Settings ]
	* Consumer Secret (API Secret)	[ copy this value from Consumer Settings ]
	
	* Access Token	                [ copy this value from Your Access Token ]
	* Access Token Secret	        [ copy this value from Your Access Token ]
 

############################################################################################
#                                   [VERY IMPORTANT]                                       # 
#    YOU WILL HAVE TO WRITE THESE KEYS IN THE "tweetBot.py".                               # 
#    Just open the file in any text editor and replace the text within the inverted commas #
#    with the codes against respective variables                                           #
############################################################################################




3. Setting up Google Calender API

[3.1] Turn on the Google Calendar API

	* Go to this wizard (https://console.developers.google.com/start/api?id=calendar) to create or select a project in the Google Developers Console and automatically turn on the API. Click 		  Continue, then Go to credentials.
	* On the Add credentials to your project page, click the Cancel button.
	* At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
	* Select the Credentials tab, click the Create credentials button and select OAuth client ID.
	* Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
	* Click OK to dismiss the resulting dialog.
	* Click the file_download (Download JSON) button to the right of the client ID.
	* Move this file to your working directory and rename it client_secret.json.

[3.1.1] Authenticate your account
	* Type the following code in the cmd prompt
	> python quickstart.py
        
	* This will open an authentication page in the default web browser
	* Click "Accept".
        * This is one time process only.From now it won't open the page.
	* The sample example at goole's website prints the events to the console.
        * I have modified the code a bit to write only the event (not the date and time) to a file named liners.txt


Now that all the dependencies are met and bot has been set up properly to tweet just run the batch file every time you want to tweet the current days event every hour  :-D 
