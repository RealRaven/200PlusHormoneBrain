import json
from typing import Iterator

import requests


class GatewayClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_state(self) -> dict:
        r = requests.get(f"{self.base_url}/state", timeout=10)
        r.raise_for_status()
        return r.json()["state"]

    def chat_stream(self, message: str) -> Iterator[dict]:
        with requests.post(
            f"{self.base_url}/chat",
            json={"message": message, "stream": True},
            stream=True,
            timeout=180,
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue
                try:
                    yield json.loads(line[6:])
                except json.JSONDecodeError:
                    continue