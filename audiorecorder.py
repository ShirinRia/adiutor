import pyaudio, wave, threading, os
import speech_recognition as sr

def takeCommand():
# It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source: #microphone k source hishebe use korbe,
        print("Listening...")
        r.pause_threshold = 1 #amar kothar kono part jeno shuna bad na jay
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
class AudioRecorder():

    # Audio class based on pyAudio and Wave
    def __init__(self):
        self.open = True
        self.rate = 44100
        self.frames_per_buffer = 1024
        self.channels = 2
        self.format = pyaudio.paInt16
        file = input("Enter your file name: ")
        self.audio_filename = f"{file}.wav"
        local_path = os.getcwd()

        if os.path.exists(str(local_path) + self.audio_filename):
            self.audio_filename = "temp_audio.wav"
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.frames_per_buffer)
        self.audio_frames = []

    # Audio starts being recorded
    def record(self):
        self.stream.start_stream()
        while (self.open == True):
            data = self.stream.read(self.frames_per_buffer)
            self.audio_frames.append(data)
            if self.open == False:
                break

    # Finishes the audio recording therefore the thread too
    def stop(self):

        if self.open == True:
            self.open = False
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            waveFile = wave.open(self.audio_filename, 'wb')
            waveFile.setnchannels(self.channels)
            waveFile.setsampwidth(self.audio.get_sample_size(self.format))
            waveFile.setframerate(self.rate)
            waveFile.writeframes(b''.join(self.audio_frames))
            waveFile.close()

    # Launches the audio recording function using a thread
    def start(self):
        audio_thread = threading.Thread(target=self.record)
        audio_thread.start()


def start_AVrecording():
    global audio_thread
    audio_thread = AudioRecorder()
    audio_thread.start()


def stop_AVrecording():
    audio_thread.stop()

def rcrd():
    start_AVrecording()

def stp():
    stop_AVrecording()
    print("Done")


while True:
    rcrd()
    d=takeCommand().lower()
    if 'stop recording' in d:
        stp()
        break
