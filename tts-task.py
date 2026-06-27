from kokoro import KPipeline
import soundfile as sf
import numpy as np
from IPython.display import Audio

bio = """
My name is Saanvi Kulkarni.
I am an engineering student interested in cybersecurity,
web development, and embedded systems.

I enjoy public speaking, technical presentations,
and working on projects involving both hardware and software.
"""

pipeline = KPipeline(lang_code='a')

generator = pipeline(
    bio,
    voice='af_bella',
    speed=1.0
)

audio_chunks = []

for _, _, audio in generator:
    audio_chunks.append(audio)

full_audio = np.concatenate(audio_chunks)

sf.write("biography.wav", full_audio, 24000)

print("Biography audio generated successfully!")
Audio("biography.wav")