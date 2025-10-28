# ⚡ RiskRanger — AI Risk Intelligence

Upload PDF/CSV/TXT → detect language (auto-translate to English) → classify risks (regulatory, climate, cyber, …) → score severity → cluster & visualize → export CSV + PDF.

## Run locally (Python 3.12)
```bash
cd riskranger
python3.12 -m venv .venv     # Windows: py -3.12 -m venv .venv
source .venv/bin/activate    # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run src/app.py
