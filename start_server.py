import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Traffic Management API...")
    print("📍 API will be available at: http://localhost:8000")
    print("📊 Open index.html in your browser to use the dashboard")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
