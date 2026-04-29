from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models.vits import Vits
from TTS.utils.audio import AudioProcessor

config = VitsConfig()

# ===== DATASET =====
config.datasets = [
    {
        "name": "my_dataset",
        "path": "dataset",
        "meta_file_train": "metadata.csv",
        "formatter": "ljspeech"
    }
]

# ===== AUDIO =====
config.audio.sample_rate = 22050

# ===== TRAIN =====
config.batch_size = 8
config.eval_batch_size = 8
config.num_loader_workers = 2
config.num_eval_loader_workers = 2

# ===== OPTIMIZER =====
config.lr_gen = 0.0002
config.lr_disc = 0.0002

# ===== TEXT =====
config.use_phonemes = False
config.text_cleaner = "basic_cleaners"

# ===== SAVE =====
config.output_path = "output"
config.run_name = "tts_vi_voice"

config.save_json("config.json")

print("Generated config.json")