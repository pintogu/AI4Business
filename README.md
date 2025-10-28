# ⚡ RiskRanger

A lightweight Streamlit app that lets you:
- Upload one or more PDFs
- Automatically detect their language
- Translate them into English (if needed)
- Analyze and visualize the extracted text

---

## 🚀 Getting Started

Follow these steps to run **RiskRanger** locally.

1️⃣ **Clone the repository**
git clone https://github.com/pintogu/AI4Business.git
cd AI4Business/riskranger

2️⃣ **Create a virtual environment (Python 3.12)**
⚠️ Use Python **3.12** — PyMuPDF and tokenizers are not fully supported on 3.13.
python3.12 -m venv .venv
source .venv/bin/activate       # Windows: .\.venv\Scripts\activate

3️⃣ **Install dependencies**
pip install -U pip
pip install -r requirements.txt

4️⃣ **Launch the app**
streamlit run src/app.py

Then open the local URL (usually http://localhost:8501) in your browser.

---

## 🧠 Troubleshooting

🧩 **Wrong `fitz` package error**
If you see an error mentioning `frontend/static` or `StaticFiles(directory=...)`, you have the wrong package installed.
Fix it by running:
pip uninstall -y fitz frontend
pip install pymupdf==1.24.10

🐍 **Check Python version**
python -V
Make sure it says something like:
Python 3.12.x

---

## 🤝 Contributing

If you make improvements, please:
1. Work inside a new branch (`git checkout -b feature/your-feature`)
2. Test locally
3. Push and open a pull request

---

## 🧾 Project Structure

AI4Business/
└── riskranger/
    ├── src/
    │   ├── app.py
    │   └── riskranger_core.py
    ├── sample_data/
    │   └── sample_risks.csv
    ├── requirements.txt
    └── README.md

---

## 💡 Example Use

Upload a PDF document → detect its language → translate → review text output directly in the Streamlit UI.
Perfect for multilingual reports, risk summaries, or compliance documents.

---



