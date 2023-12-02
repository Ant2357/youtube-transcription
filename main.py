import whisper
from yt_dlp import YoutubeDL

model = whisper.load_model("large")

# yt_dlp のオプション
youtube_urls = ["https://www.youtube.com/watch?v=uUb4RgbgESY"] 
ydl_opts = {
    "format": "mp3/bestaudio/best",
    "outtmpl": "audio",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }
    ]
}

# mp3 の形式でダウンロード
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(youtube_urls)

# 文字起こし
result = model.transcribe("audio.mp3", verbose=True)

# 歌詞ファイルを出力する
with open("output.txt", "w", encoding="utf-8") as f:
    # 歌詞を出力(配列)
    texts = list(map(lambda x: x["text"].strip(), result["segments"]))
    f.write("\n".join(texts))
