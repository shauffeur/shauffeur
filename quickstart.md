
# Quickstart — Run Shauffeur locally (demo)

## Prerequisites
- Python 3.10+
- git, make (optional)
- (Optional GPU) NVIDIA CUDA + drivers for bitsandbytes

## Create virtualenv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run first experiment (mocked)
```bash
python experiments/01_explain_event.py --mock
```

## Run with Hugging Face Mistral (GPU recommended)
1. Install optional deps:
```bash
pip install torch accelerate transformers bitsandbytes sentencepiece
```
2. Edit `shauffeur/config/mistral.yaml` with model id (e.g. mistralai/Mistral-7B-Instruct-v0.2).
3. Run:
```bash
python experiments/01_explain_event.py
```

## ROS2 integration (dev)
- Install ROS2 (humble/galactic/rolling consistent with your OS).
- Run:
```bash
ros2 run shauffeur shauffeur_node.py
```
(See `shauffeur/ros2/` for node and message definitions.)
