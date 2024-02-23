# Using Elevenlabs

import elevenlabs

sounds = elevenlabs.generate(
        text=run_model, voice="wViXBPUzp2ZZixB1xQuM", model="eleven_multilingual_v2"
    )
    # Text to Speech
print("Start Text to Speech Model")
# Play Speech
elevenlabs.play(sounds)
# Save Speech
elevenlabs.save(sounds, CONFIG_DATA["speech_result"])

# Using pyttsx3
import pyttsx3 as pyt

print("Start Text to Speech Model")
engine = pyt.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "id/female")
engine.say(run_model)
engine.runAndWait()
