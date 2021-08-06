import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ADD KEY HERE'
client = texttospeech_v1.TextToSpeechClient()

text = ''

synthesis_input = texttospeech_v1.SynthesisInput(text=text)

voice = texttospeech_v1.VoiceSelectionParams(
    language_code='en-uk',
    ssml_gender= texttospeech_v1.SsmlVoiceGender.MALE
)

print(client.list_voices())

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding =texttospeech_v1.AudioEncoding.MP3
)

response =  client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open('audio-file.mp3','wb') as output:
    output.write(response.audio_content)

