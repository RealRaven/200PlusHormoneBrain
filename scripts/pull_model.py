"""Pre-pull model to local HF cache. Run once to speed up vLLM startup."""

import os

from huggingface_hub import snapshot_download

model_id = os.environ.get("MODEL_ID", "TrueRealRaven/gemma-4-E2B-it-heretic-v1")
token = os.environ.get("HF_TOKEN") or None

print(f"Pulling {model_id}...")
snapshot_download(repo_id=model_id, token=token)
print("Done.")