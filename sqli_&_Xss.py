import webbrowser
import re
url = input("Enter your test url here")
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  
# Driver code     
str1 =input(" enter your payloads with spaces here")
payload=(Convert(str1))
print(payload)
#payload=input(" enter your payloads with spaces here")
webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))

for i in range (len(payload)):
    final_url=url+payload[i]
    webbrowser.get('firefox').open(final_url)

