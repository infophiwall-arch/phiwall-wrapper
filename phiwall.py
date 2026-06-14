import requests

class PhiWall:
    """The official zero-overhead PII redaction shield for AI builders."""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://phiwall-phiwall-engine.hf.space/v1/clean"
        
    def clean(self, text: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        try:
            res = requests.post(self.url, json={"text": text}, headers=headers)
            if res.status_code == 200:
                return res.json().get("clean_text", text)
            elif res.status_code == 402:
                print("[PhiWall Security Alert]: Subscription Expired. Please Renew.")
            return text
        except Exception:
            return text
