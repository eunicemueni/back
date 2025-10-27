from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests

app = FastAPI(title="Kairah Studio Backend", description="Cinematic AI video generator API", version="1.0")

# --- Allow all origins for now (for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Root route
@app.get("/")
async def root():
    return {"message": "Kairah Studio Backend is live ✨"}

# --- Example: AI Video generation mock endpoint
@app.post("/generate-video/")
async def generate_video(prompt: str = Form(...), style: str = Form("cinematic")):
    # Mock: return video creation placeholder
    return {
        "status": "success",
        "prompt": prompt,
        "style": style,
        "video_url": "https://example.com/generated_video.mp4"
    }

# --- Example: Payment webhook mock
@app.post("/webhook/")
async def webhook_handler(data: dict):
    return {"status": "received", "data": data}

# --- Example: Upload endpoint (mock)
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}

# --- Run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
