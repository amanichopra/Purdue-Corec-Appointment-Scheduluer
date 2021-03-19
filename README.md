# Purdue Corec Appointment Scheduluer

This program is designed to automate the process of scheduling appointments at the corec. Depending on how the cronjob is set up, the automation can occur hourly, daily, weekly, or at any desired time interval. The usage for linux is summarized below. 

1. Download scheduler.py from the repo. Ensure "imageio" and "selenium" are installed. Place the path to python at the top of the file. The CL arguments for the script are as follows:
   1. username: Purdue Login
   2. password: Duo Password (ex. ####,push)
   3. tries: Number of Times to Attempt Login; default=4
   4. pathToChromeDriver: path/to/chromedriver
   5. d: Display Options; default=None; "headless" hides chromedriver from launching
   6. timeSlot: Desired Time Slot to Schedule (ex. "9:20 - 10:40 AM"); ensure it matches the format on the Purdue Recwell website
2. Download [Google Chromedriver](https://chromedriver.chromium.org/downloads).
3. Open terminal:
   1. ```launchctl start /System/Library/LaunchDaemons/com.vix.cron.plist``` to launch cron.
   2. ```chmod a+x path/to/scheduler.py``` to instanstiate permissions.
   3. ```crontab -e``` to edit cron file.
   4. Use VIM to edit the file and enter: 

```PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin```

```PYTHONPATH=path/to/lib/python3.8/site-packages```

```MAILTO=youremail@gmail.com```

```* * * * * python3 path/to/scheduler.py --username yourUsername --password yourPassword --tries numTries --pathToChromeDriver path/to/chromedriver --d headless --timeSlot "your desired timeslot"```

Be sure to enter the appropriate cron expression for the desired frequency (ex. "30 12 * * *" will run the script daily at 12:30). Refer to these crontab [resources](https://crontab.guru/).

4. Done!



