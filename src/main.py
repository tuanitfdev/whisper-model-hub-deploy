import stable_whisper as whisper

model = whisper.load_faster_whisper(
    "large-v3", 
    device="cuda", 
    compute_type="float16",
    device_index=[0]
)

print("Model loaded successfully")
