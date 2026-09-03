import urllib.request
import time

time.sleep(45)  # Wait for deploy

urls = [
    "https://ecosort-ai-v2.vercel.app/api/ecosort",
    "https://ecosort-ai-v2.vercel.app/api/health",
]

for url in urls:
    print(f"\n--- {url} ---")
    try:
        r = urllib.request.urlopen(url, timeout=30)
        print(f"Status: {r.status}")
        print(r.read().decode()[:500])
    except Exception as e:
        print(f"Error: {e}")
        try:
            print(f"Body: {e.read().decode()[:500]}")
        except:
            pass
