from TTS.utils.synthesizer import Synthesizer

# load model custom
synthesizer = Synthesizer(
    tts_checkpoint="output/tts_vi_voice-April-29-2026_12+58AM-6664710/best_model.pth",
    tts_config_path="output/tts_vi_voice-April-29-2026_12+58AM-6664710/config.json",
)

# generate speech
wav = synthesizer.tts("Hello, My name is Tien")

# save file
synthesizer.save_wav(wav, "result.wav")