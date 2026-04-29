import whisper
import os

DATASET_PATH = "dataset/wavs"
OUTPUT_FILE = "dataset/metadata.csv"

# model = whisper.load_model("large").to("cuda")
model = whisper.load_model("medium").to("cuda")
# model = whisper.load_model("small").to("cuda")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    files = sorted(os.listdir(DATASET_PATH))

    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(DATASET_PATH, file)

            print(f"\n {file}")

            result = model.transcribe(
                path,
                language="vi",
                fp16=True,
                beam_size=1,
                best_of=1,
                temperature=0.0
            )

            text = result["text"].strip()

            print("👉", text)

            f.write(f"{file}|{text}|{text}\n")

print("\n Done metadata.csv")