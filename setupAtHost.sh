#!/bin/bash
uv run python src/main.py
wget -P data/whl/ https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu12torch2.9cxx11abiTRUE-cp312-cp312-linux_x86_64.whl
mkdir -p data/cacheTorchHub && curl -L https://github.com/snakers4/silero-vad/tarball/master -o data/cacheTorchHub/snakers4_silero-vad_master.tar.gz

