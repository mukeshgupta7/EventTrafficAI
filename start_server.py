import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("🚀 Starting Traffic Management API...")
    print(f"📍 API will be available at: http://localhost:{port}")
    print("📊 Open index.html in your browser to use the dashboard")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=False)
