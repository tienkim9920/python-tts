import torch
from TTS.config import load_config
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.vits import Vits
from TTS.utils.audio import AudioProcessor
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from trainer import Trainer, TrainerArgs


def main():
    # ===== LOAD CONFIG =====
    config = load_config("config.json")

    # ===== AUDIO =====
    ap = AudioProcessor.init_from_config(config)

    # ===== TOKENIZER =====
    tokenizer, config = TTSTokenizer.init_from_config(config)

    # ===== DATA =====
    train_samples, eval_samples = load_tts_samples(
        config.datasets,
        eval_split=True
    )

    # ===== MODEL =====
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = Vits(config, ap, tokenizer).to(device)

    # ===== TRAINER =====
    trainer = Trainer(
        TrainerArgs(),
        config=config,
        model=model,
        train_samples=train_samples,
        eval_samples=eval_samples,
        output_path="output"
    )

    # ===== TRAIN =====
    trainer.fit()


if __name__ == "__main__":
    main()