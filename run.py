import uvicorn

if __name__ == "__main__":
    # Use uvicorn import path string so Python path doesn't need manual hacks.
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )