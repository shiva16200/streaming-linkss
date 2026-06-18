#!/usr/bin/env python3
import base64
import hashlib
import time
from datetime import datetime

SERVER_IP = "202.166.192.207"
STREAM_NAME = "wc-Himalaya3"
SECRET_KEY = "nepal123"

def generate_link():
    t = int(time.time())
    auth = f"server_time={t}&valid_minutes=1440&id=200"
    h = hashlib.md5(f"{auth}{SECRET_KEY}".encode()).hexdigest()
    wms = base64.b64encode(f"{auth}&hash_value={h}".encode()).decode()
    link = f"http://{SERVER_IP}/ffplay/{STREAM_NAME}/playlist.m3u8?wmsAuthSign={wms}"
    return link

link = generate_link()
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

content = f"""# STREAMING LINK

LINK:
{link}

Generated: {now}
Expires: 24 hours
"""

with open("README.md", "w") as f:
    f.write(content)

print(link)
