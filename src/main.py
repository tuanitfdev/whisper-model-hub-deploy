import stable_whisper as whisper

try:
    model = whisper.load_faster_whisper(
        # "deepdml/faster-whisper-large-v3-turbo-ct2", 
        "large-v3", 
        device="cuda", 
        compute_type="float16",
        device_index=[0],
        download_root="data/models",
    )
except Exception:
    pass

try:
    model02 = whisper.load_faster_whisper(
        "deepdml/faster-whisper-large-v3-turbo-ct2", 
        # "large-v3", 
        device="cuda", 
        compute_type="float16",
        device_index=[0],
        download_root="data/models",
    )
except Exception:
    pass

print("Models loaded successfully")
