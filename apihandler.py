#used apiLayers API

import requests
import json


class SentimentAPI:
    def __init__(self):
        self.api_key = 'YOUR_API_KEY'
        self.url = "https://api.apilayer.com/sentiment/analysis"
        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.api_key
        }

    def analyze_sentiment(self, text):
        payload = json.dumps({
            "text": text
        })

        response = requests.post(self.url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Status {response.status_code}",
                "message": response.text
            }

    def emotion_analysis(self, text):
        payload = json.dumps({"text": text})
        response = requests.post(url="https://api.apilayer.com/text_to_emotion", headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": True,
                "status": response.status_code,
                "message": response.text
            }
