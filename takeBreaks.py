import time
import webbrowser

#To get the current time
current_time = time.ctime()
print ("Start time = "+current_time)
i=0
while i<3:
	#for test purposes, it will temporarily suspend the web browser for 10 secs and then plays the video
	time.sleep(10)
	if i==0:
		webbrowser.open("https://www.youtube.com/watch?v=5nyFfZnsyNY")
		time.sleep(300)
	elif i==1:
		webbrowser.open("https://www.youtube.com/watch?v=pMmCvixJS8c")
		time.sleep(300)
	elif i==2:
		webbrowser.open("https://www.youtube.com/watch?v=Spfaub0sVk0")
		time.sleep(300)
	else:
		webbrowser.open("https://www.youtube.com/watch?v=9ZsRQNUQ8Vo")
		time.sleep(300)
	i=i+1