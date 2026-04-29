with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

result = []
current = ""

for line in lines:
    if line.strip() == "":
        if current:
            result.append(current.strip())
            current = ""
    else:
        current += " " + line.strip()

if current:
    result.append(current.strip())

final_text = "\n\n".join(result)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(final_text)