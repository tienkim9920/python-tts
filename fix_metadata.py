input_file = "dataset/metadata.csv"
output_file = "dataset/metadata_fixed.csv"

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    for line in f_in:
        parts = line.strip().split("|")

        filename = parts[0].replace(".wav", "")  # 🔥 remove .wav
        text = parts[1]

        f_out.write(f"{filename}|{text}|{text}\n")

print("Removed .wav from metadata")