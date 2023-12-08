import os
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

from config import history_prompt, text_prompt
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
preload_models()
audio_array = generate_audio(text_prompt,history_prompt=history_prompt)
write_wav("bark_generatio.wav", SAMPLE_RATE, audio_array)
Audio(audio_array, rate=SAMPLE_RATE)


