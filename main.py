from webserver import keep_alive
import requests

channelID = 1006412585211547682
headers = {
    "authorization":
    "NzY5NTc2OTM3NTMzOTk3MDk2.GI3zGo.WdAn5KbLmRrxwBlxDwT9tHZo0b3zwidzxwtogk"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
