try:
    import requests
    print("requests is installed")
except ImportError as e:
    print(f"requests is NOT installed: {e}")
