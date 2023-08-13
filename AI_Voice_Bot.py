import openai #install these modules if its not installed using pip install openai
import pyttsx3
import speech_recognition as sr #pyaudio need to be enabled else this module would not work
import webbrowser

api_data = "your_OPENAI_API_key" 
#OPENAI Free account would provide API key 
#If you want to use on commericial scale, upgrade the account 
openai.api_key=api_data

completion=openai.Completion()
#Function for the model creation and collection of response
def Reply(question):
    prompt=f'Harsha: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Bye'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#To initate the request for input
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello How Are You? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in') #you can change the language, but OPENAI wont accept other language prompt as of now
        print("Harsha said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        model_answer=Reply(query)
        print(model_answer)
        speak(model_answer)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            break
