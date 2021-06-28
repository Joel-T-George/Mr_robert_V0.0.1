## Mr_robert_V0.0.1
###### Basic Voice Assistant 

Mr Robert Is The Basic Function Hear and Replay To Us It Can Make Same Functions Sending Emails,Get News ,Weather Reports And wepikdea information

###### robert.py =>
```
if __name__ == '__main__':
    clear = lambda: os.system('cls')
```
Intials the bot by calling  this functions in the next line execute the function 
in Command line by text and through Speak of machines

```
    read_write.WishMe()
    read_write.NowtTime()
```
It Call the Function Explain in read_write.py 
it Wish to User And Say the time 

```while True```
it Continue call the function in py file  Same time ocurred same Error 
```
        data = read_write.Hear().lower()
        data.replace("User said:"," ")
```
This Code User Speech Convert into String Format and make into lower case like 'abcd'
data variable return string in format like *User said: Something here Speech*
English Language is supported
```
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
> bot: I am Fine , Thank you How are you

next condition:
> John: Bot What is Time Now 
> bot: Sir the time is hours-minutes-seconds

next condition:
> John: Bot Say About You Self
> bot: I am bot Version Zero Point Zero Point One





