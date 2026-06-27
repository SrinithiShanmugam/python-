
import text_to_speech
import speech_to_text
import datetime 
import weather 
import webbrowser
import os  






def Action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is virtual assistant")
        return "my name is virtual assistant"


    elif "hello virtual assistant" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech("hey,sir how can i help you ")
        return "hey,sir how can i help you "

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir ")
        return "good morning sir "

    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        Time = (str)(current_time)+"Hour :",(str)(current_time.minute)+"Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif " play rowdy baby" in user_data or "rowdy" in user_data:
        os.system("start https://www.youtube.com/results?search_query=rowdy+baby+song")
        text_to_speech.text_to_speech("playing rowdy baby song now")
        return "playing rowdy baby song now"
    
   
    
    elif " play golden sparrow" in user_data or "golden" in user_data or "sparrow" in user_data:
        os.system("start https://www.youtube.com/results?search_query=golden+sparrow+tamil+song")
        text_to_speech.text_to_speech("playing golden sparrow song now")
        return "playing golden sparrow song now"
    
  

    elif " play kanima" in user_data or "kaneema" in user_data or "ka nima" in user_data or "kanema" in user_data:
        os.system("start https://www.youtube.com/results?search_query=kanima+tamil+song")
        text_to_speech.text_to_speech("playing kanima song now")
        return "playing kanima song now"
    
    elif " play kanadi poove" in user_data or "kanadi" in user_data or "poove" in user_data or "kanadipoove" in user_data or "kannadi poove" in user_data or "kannadi" in user_data:
        os.system("start https://www.youtube.com/results?search_query=kanadi+poove+tamil+song")
        text_to_speech.text_to_speech("playing kanadi poove song now")
        return "playing kanadi poove song now"
    

    elif "aalaporaan tamizhan" in user_data or "aalaporaan" in user_data:
        os.system("start https://www.youtube.com/results?search_query=aalaporaan+tamizhan+song")
        text_to_speech.text_to_speech("playing aalaporaan tamizhan song now")
        return "playing aalaporaan tamizhan song now"
    
    elif "mersalaayitten" in user_data or "mersala" in user_data:
        os.system("start https://www.youtube.com/results?search_query=mersalaayitten+song")
        text_to_speech.text_to_speech("playing mersalaayitten song now")
        return "playing mersalaayitten song now"

    elif "youtube" in user_data or "you tube" in user_data or "utube" in user_data:
       os.system("start https://www.youtube.com")
       text_to_speech.text_to_speech("youtube.com is ready now")
       return "youtube.com is ready now"
    

    elif "google" in user_data:
        os.system("start https://www.google.com") # ← changed
        text_to_speech.text_to_speech("google.com is ready now")
        return "google.com is ready now"

    elif "weather" in user_data:
        ans = weather.weather("chennai")
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"
    

#Action("what is your name" )

