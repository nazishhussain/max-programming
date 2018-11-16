import speech_recognition as sr  

# record audio                                                              
r = sr.Recognizer() 
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("say something !")
	audio = r.listen(source)                                                                                  

# speech recognition using Google Speech recognition
try:
	# for testing purposes, we are using the default API key
	# to use another APL
    print("You said : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))