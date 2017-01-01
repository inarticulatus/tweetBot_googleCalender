from twython import Twython, TwythonError
import time

APP_KEY = 'replace with your customer key'
APP_SECRET = 'replace with your customer secret'
OAUTH_TOKEN = 'your access token'
OAUTH_TOKEN_SECRET = 'your access token secret'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('liners.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n') #Strips any empty line.
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the tweeted line.
				tweetfile.writelines(buff)
			time.sleep(1)
		else:
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line) #Removes the line that has more than 140 characters.
				tweetfile.writelines(buff)
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...") #The lines have been tweeted


except TwythonError as e:
	print (e)
