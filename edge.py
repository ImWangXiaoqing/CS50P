import os
import struct

def extract_urls_from_tabs_file(file_path):
    urls = []

    with open(file_path, "rb") as f:
        data = f.read()

        # Basic sanity check: look for "http" or "https"
        pos = 0
        while pos < len(data):
            if data[pos:pos+4] == b'http':
                end = data.find(b'\x00', pos)
                url = data[pos:end].decode(errors='ignore')
                urls.append(url)
                pos = end
            else:
                pos += 1

    return list(set(urls))  # Remove duplicates

# --- 👇 Update this path to your actual Tabs_ or Session_ file ---
tabs_file = r"C:\Users\nitis\AppData\Local\Microsoft\Edge\User Data\Default\Sessions\Apps_13393615520349513"

if os.path.exists(tabs_file):
    print(f"Parsing: {tabs_file}")
    urls = extract_urls_from_tabs_file(tabs_file)

    print("\n--- Extracted URLs ---")
    for url in urls:
        print(url)
else:
    print("File not found. Make sure the path is correct.")
