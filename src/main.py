import stable_whisper as whisper

model = whisper.load_faster_whisper(
    # "deepdml/faster-whisper-large-v3-turbo-ct2", 
    "large-v3", 
    device="cuda", 
    compute_type="float16",
    device_index=[0],
    download_root="data/models",
)

model02 = whisper.load_faster_whisper(
    "deepdml/faster-whisper-large-v3-turbo-ct2", 
    # "large-v3", 
    device="cuda", 
    compute_type="float16",
    device_index=[0],
    download_root="data/models",
)

print("Models loaded successfully")
