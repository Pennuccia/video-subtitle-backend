from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    video_url: str
    subtitle_mode: str
    target_language: str | None = None
    render_mode: str

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/process_video_subtitles")
def process_video(data: VideoRequest):
    # TEMP MOCK RESPONSE (we'll replace later with real processing)
    return {
        "video_url": "https://example.com/fake-video.mp4",
        "status": "completed",
        "message": "Mock video processed successfully"
    }
