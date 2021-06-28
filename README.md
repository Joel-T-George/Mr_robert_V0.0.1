# Mr_RobertV0.0.1
###### Basic Voice Assistant 

Mr Robert Is The Basic Function Hear and Replay To Us It Can Make Same Functions Sending Emails,Get News ,Weather Reports And wepikdea information

##robert.py =>
```python
if __name__ == '__main__':
    clear = lambda: os.system('cls')
```
Intials the bot by calling  this functions in the next line execute the function 
in Command line by text and through Speak of machines

```python
    read_write.WishMe()
    read_write.NowtTime()
```
It Call the Function Explain in read_write.py 
it Wish to User And Say the time 

```python
while True
```
it Continue call the function in py file  Same time ocurred same Error 
```python
        data = read_write.Hear().lower()
        data.replace("User said:"," ")
```
This Code User Speech Convert into String Format and make into lower case like 'abcd'
data variable return string in format like *User said: Something here Speech*
English Language is supported
```python
         if "fine" in data:
            read_write.Fine()
        elif "time" in data:
            read_write.NowtTime()
        elif"say about you" in data:
            read_write.about()
        elif"day" in data:
            read_write.Day()
```
This lines Basic Upadated it Text predefine Word
Now make Example Conversation Between Bot and Human
> John: Bot Are you fine
```
bot: I am Fine , Thank you How are you
```

next condition:
> John: Bot What is Time Now 
```
 bot: Sir the time is hours-minutes-seconds
```

next condition:
> John: Bot Say About You Self
```
 bot: I am bot Version Zero Point Zero Point One
```
next condition:
> John: Bot Say Day 
```
 bot: I am bot Version Zero Point Zero Point One
```
This are Way call the functions one by one 
```
        elif"weather" in data or "weather update" in data:
            updates.weather()
        elif "search" in data:
            query = data.replace("search"," ")
            updates.wiki(query)
        elif"news" in data or "today news" in data:
            read_write.Speak("I going to Tell Top Ten News in India ")
            updates.Update_news()
            read_write.Speak("Thank you for here News ")
            
  ```
This lines Call Api it was Code in Update.py and explain later on and now Say function Call in by voice
Explain :
> John: bot say current Weather  
```
Replay:
 bot: temperture,humidity, wind_speed,climate
```
next condition:
> John: bot search Tajmahal
```
Replay:
 bot: --say informations from wikipedia Api--
```
next condition:
> John: bot Top news Now happens
```
Replay:
 bot: --say top ten news--
```
Special Lines Go to explain in coming lines..
```python
        elif "read" in data:
            read_write.Speak("I want to read pdf ")
            read_write.Speak("Enter to Starting Page")
            startnum = int(input("Enter to Starting Page :"))
            read_write.Speak("Enter the ending page number")
            endnum = int(input("Enter the ending page number :"))
            read_write.Speak("You want to select the pdf book")
            read_write.pdfred(startnum,endnum)
      elif"email" in data:
            update.sendmail()
 ```
 It code buliding the Conversation Between User and Bot to read
 How many pages and selecting pdf files this line says
 'read_write.pdfread()' read the files content without error by select .pdf extension files
 > Error:
 > picture content not Readed to solve use python packages image to charater packages later added in repo
 > non stop playing the audio 
 Sending Email 'sendmail' function
 
 ##lib_machines/updates.py  =>
 Importing  packages  
 Call the api link for weather,news,wikipedia
 Collect data from the api and handle json formated data 
 and make more functionality in the update.py file
## INSTALL PACKAGES
 ```
    pip install pyttsx3
    pip install SpeechRecognition
    pip install wikipedia
    pip install pyjokes
    pip install googletrans
    pip install PyPDF2
    
 ```
##Docs of Packages
    Docs of pyttsx3 [click](https://pypi.org/project/pyttsx3/).
    Docs of SpeechRecognition [click](https://pypi.org/project/SpeechRecognition/).
    Docs of wikipedia [click](https://pypi.org/project/wikipedia/).
    Docs of googletrans [click](https://pypi.org/project/googletrans/).
    Docs of PyPDF2 [click](https://pypi.org/project/PyPDF2/).
     
##API WEBSITES LINK
    For Weather api use this link [Openweather](https://api.openweathermap.org).
    For News api use this link[newsapi](http://newsapi.org/).
 
 
 
 
 
 







