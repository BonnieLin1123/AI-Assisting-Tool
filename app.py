from flask import Flask, request, jsonify
import openai
import yt_dlp
import os
import transcription

app = Flask(__name__)
openai.api_key = "API-keywords"

def download_audio(youtube_url):
    ydl_opts = {
        "ffmpeg_location":"/opt/homebrew/bin/ffmpeg",
        "format": "bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
        "outtmpl": "video_audio.%(ext)s"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return "video_audio.mp3"

@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.json
    video_url = data["url"]

    audio_file = download_audio(video_url)

    response = transcription.generate_transcription(audio_file)

    # studyplan = transcription.generate_study_plan(response)
    
    os.remove(audio_file)  # 删除临时音频文件
    return jsonify({"transcript": response})

if __name__ == "__main__":
    app.run(debug=True)