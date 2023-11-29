import whisper
from yt_dlp import YoutubeDL

model = whisper.load_model("small")

# yt_dlp のオプション
youtube_urls = ["https://www.youtube.com/watch?v=Aqfd-F0uACw"] 
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
with open("output.txt", "w") as f:
    f.write(result["text"])
