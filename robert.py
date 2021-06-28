#Mr.Robert acess code..
#run the module only Mr.robert works
import os
from lib_machines import read_write,updates



if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    read_write.WishMe()
    read_write.NowtTime()

    while True:
        

        data = read_write.Hear().lower()
        data.replace("User said:"," ")
        
        if "fine" in data:
            read_write.Fine()
        elif "time" in data:
            read_write.NowtTime()
        elif"say about you" in data:
            read_write.about()
        elif"day" in data:
            read_write.Day()
        elif"weather" in data or "weather update" in data:
            updates.weather()
        elif "search" in data:
            query = data.replace("search"," ")
            updates.wiki(query)
        elif"close" in data:
            read_write.Speak("i wants to exit say yes or no")
            query=read_write.Hear().lower()
            if "no" in query:
                read_write.Speak("ok I wil work on ") 
            elif "yes" in query or "s" in query:
                read_write.Speak("Are you Sure I wants to Exits ")
                read_write.Speak("thank you for using me")
                break   
        elif"news" in data or "today news" in data:
            read_write.Speak("I going to Tell Top Ten News in India ")
            updates.Update_news()
            read_write.Speak("Thank you for here News ")
        elif "read" in data:
            read_write.Speak("I want to read pdf ")
            read_write.Speak("Enter to Starting Page")
            startnum = int(input("Enter to Starting Page :"))
            read_write.Speak("Enter the ending page number")
            endnum = int(input("Enter the ending page number :"))
            read_write.Speak("You want to select the pdf book")
            read_write.pdfred(startnum,endnum)


        elif "unable to recognize your voice" in data or "Unable to Recognize your voice" in data:
            print("robert is waiting .... ... ...")

        else:
            read_write.Speak("I try to update futrit")  
