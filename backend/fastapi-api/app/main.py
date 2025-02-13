from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI Server is running! 🚀"}

# Include routes
app.include_router(analyze_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
