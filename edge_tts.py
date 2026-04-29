import asyncio
import edge_tts

VOICE = "vi-VN-NamMinhNeural"

async def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("output.mp3")

asyncio.run(main())