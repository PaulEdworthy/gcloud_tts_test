import os
import playsound

# from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_cloud_credentials.json"

client = texttospeech_v1.TextToSpeechClient()

# test text to pass into speech synthesis
text = """
Text to speech test
"""

synthesis_input = texttospeech_v1.SynthesisInput(text=text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code="en-gb",
    # name='en-GB-Standard-D',
    # name='en-GB-Wavenet-D',
    name="en-GB-Neural2-D",
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE,
)

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3, speaking_rate=1.25
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio written to file 'output.mp3'")
    playsound.playsound("output.mp3")

# https://cloud.google.com/text-to-speech/docs/list-voices
# def list_voices():
#     voices = client.list_voices()

#     for voice in voices.voices:
#         if 'en-GB' in voice.name and '-D' in voice.name and voice.ssml_gender.name == "MALE":
#             print(f'Name: {voice.name}')

#     My chosen voices:
#     # en-GB-Standard-D
#     # en-GB-Wavenet-D
#     # en-GB-Neural2-D

# list_voices()
