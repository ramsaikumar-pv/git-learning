def start_server(host="0.0.0.0", port=8080):
    """Start the HTTP server."""
    print(f"Starting server on {host}:{port}")
    return True

def health_check():
    return {"status": "ok", "version": "1.0"}

if __name__ == "__main__":
    start_server()
