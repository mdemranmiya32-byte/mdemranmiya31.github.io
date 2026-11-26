"""
Set Telegram command menu for Control Center V2.
This only configures Telegram's command list; it does NOT run polling.
Use a NEW token after revoking the token exposed inside the uploaded APK.
"""
import json
import os
import urllib.request
import urllib.error

TOKEN = os.environ.get("BOT_TOKEN") or input("Paste NEW BotFather token: ").strip()
if not TOKEN:
    raise SystemExit("BOT_TOKEN is required")

commands = [
    {"command":"menu","description":"Open Control Center category menu"},
    {"command":"info","description":"Device dashboard and connection"},
    {"command":"connected-device","description":"Show connected device"},
    {"command":"uptime","description":"Device uptime"},
    {"command":"storage","description":"Storage usage"},
    {"command":"ram","description":"RAM status"},
    {"command":"cpu","description":"CPU status"},
    {"command":"network","description":"Network information"},
    {"command":"wifi","description":"Wi-Fi status and scan"},
    {"command":"apps","description":"List installed apps"},
    {"command":"ls","description":"List files: /ls [dir]"},
    {"command":"pwd","description":"Current folder"},
    {"command":"find","description":"Find a file: /find name"},
    {"command":"download","description":"Download an allowed file"},
    {"command":"upload","description":"Upload a selected file"},
    {"command":"location","description":"Share location with device permission"},
    {"command":"gallery","description":"Share recent gallery photos"},
    {"command":"screenshot","description":"Capture screen with consent"},
    {"command":"screenauth","description":"Approve screen capture on phone"},
    {"command":"screen5","description":"Short screen capture (consent required)"},
    {"command":"screenstop","description":"Stop screen capture"},
    {"command":"reclog","description":"Show capture session log"},
    {"command":"lockstatus","description":"Show device lock status"},
    {"command":"help","description":"Show supported commands"},
]

def api(method, payload):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            result=json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(e.read().decode())
        raise SystemExit("Telegram API request failed")
    if not result.get("ok"):
        raise SystemExit(f"Telegram API error: {result}")
    return result.get("result")

api("setMyCommands", {"commands": commands})
api("setChatMenuButton", {"menu_button":{"type":"commands"}})
print("Telegram command menu configured.")
print("Note: The installed APK must use this same NEW token to respond to these commands.")
