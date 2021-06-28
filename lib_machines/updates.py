#update of current news ,weather ,and others
import speech_recognition as ear
import requests
import json
import pyttsx3 as vocal
import wikipedia
import smtplib
from email.message import EmailMessage

def Hear():#it regcognition voices 
    #intital the speech recognition organ
    r = ear.Recognizer()
    # open the robert ears ...
    with ear.Microphone() as source:     
        print("Listening...")
        r.pause_threshold = 1 #it decide to open audio inputs 
        audio = r.listen(source) #it is process hearing by the rober
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')# it convert the audio to text ...
        print(f"User said: {query}\n")
    except Exception as e: #exception case was handle by this
        print(e)
        value = "Unable to Recognize your voice"    
        print(value) 
        return value # hear organ is formed .....................
    return query #return in text format


def Speakon(content_to_speak):
    mouth = vocal.init()
    mouth.setProperty('rate',150)
    mouth.say(content_to_speak)
    mouth.runAndWait()#speak organ is formed.................
#here the weather update process is happends ......
def weather():
    weather_api ="54851e0215834b520af256de1255e551"
    location = "chennai"


    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+weather_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
   
    if api_data['cod'] == '404':
        print("invalid city {}, please check you city name ".format(location))
    else:
        temp_city = ((api_data['main']['temp'])-273.15)
        weather_des = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']

        temp_city_rob = "Current Temperture is {} Degree Celsius".format(temp_city)
        weather_climate = "Today a Climate is {} .".format(weather_des)
        humidity_rob = "Humidity is {} Percentage".format(humidity)
        wind_speed_rob = "Wind Speed is {} kilometre per hour".format(wind_speed)

        Speakon(temp_city_rob)
        Speakon(weather_climate)
        Speakon(humidity_rob)
        Speakon(wind_speed_rob)

        print(temp_city_rob)
        print(weather_climate)
        print(humidity_rob)
        print(wind_speed_rob)
# it say the today news 
def Update_news():       
    web = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=12ce725c33b241e9aa4370739dbf8d32")

    content = web.content
    news = json.loads(content)

    for i in range(10):
        start = "News Number",str(i+1)
        Speakon(start)
        print("################################## ",str(i+1)," News #############################")
        news_paper =news['articles'][i]['source']['name']
        print("\n--------------------------------", news_paper ,"--------------------------------")
        Headlines = news['articles'][i]['title']
        Speakon(Headlines)
        print("\n Headlines ",str(i+1)," : ",Headlines)
        desrptions = news['articles'][i]['description']
        desi = "matter is {}".format(desrptions)
        Speakon(desi)
        print("\n  Description : ",desrptions)
        urls_of_news =news['articles'][i]['url']
        print("\n \n See in website :",urls_of_news)
        print("\n \n -------------------------------------------------------------------------------------")


def wiki(query):
    run = True
    while run:
        try:
            res=wikipedia.summary(query,sentences= 3)
            print(res)
            Speakon(res)
        except wikipedia.exceptions.DisambiguationError :
            print("more relevant answers ")
            Speakon("more relevant answers ")
        except wikipedia.exceptions.HTTPTimeoutError :
            print("net work is slower please increase internet ")
            Speakon("net work is slower please increase internet ")
        except wikipedia.exceptions.PageError :   
            print("the query was invalid ") 
            Speakon("the query was invalid")
        finally:
            print("thank for using ") 
            Speakon("thank for using ")

        Speakon("again serach anything from me ")     
        Speakon("say yes or no  ") 
        queryes = Hear()
        queryes.lower()
        if "yes" in queryes:
            Speakon("what want to serach ..")
            quest = Hear()
            question= quest.lower()
            question.replace("user said:"," ")
            wiki(question)
        elif "no" in queryes:
            Speakon("thank you sir ") 
            print("serach is ends......")
            run =False
            return run
        else:
            run = False
            return run
mail_id_list = {
    "daisy":"daisythomas2007j@gmail.com",
    "kings":"kecbme016@kingsedu.ac.in",
}

def sender( to_mail,subject,messages):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('joelthomas0203@gmail.com','ezidvtbiwnzwlyek')
    emails = EmailMessage()
    emails['From'] =  'joelthomas0203@gmail.com'
    emails['To'] = to_mail
    emails['Subject'] = subject
    emails.set_content(messages)
    server.send_message(emails)

def sendmail():
    Speakon("To whom I send email")
    reciver = Hear().lower()
    reciver = reciver.replace("User said:"," ")
    reciver = reciver.replace('desi','daisy')
    id = mail_id_list[reciver]
    print(id)
    Speakon("What was the Subject of the message")
    subject_to = Hear().replace('User said:'," ")
    Speakon("What was the content or message")
    messages = Hear().replace('User said:'," ")
    sender(id,subject_to,messages)
    Speakon("the mail sended successfully")
    print("email sended ....")
