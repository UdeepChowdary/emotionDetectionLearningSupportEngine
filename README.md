# 🧠 Emotion Detection & Learning Support Engine

An AI-powered Streamlit web application that detects a student's emotional state from their study challenge description and delivers personalized, empathetic learning support using **BiLSTM**, **BERT**, and **Gemini AI**.

---

## 📁 Project Structure

```
emotion-detection/
├── .env
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
├── emotion_response_examples.csv        ← auto-created at runtime
├── emotion_response_mapping.csv         ← auto-created at runtime
├── data/
│   └── emotion_text_dataset.csv         ← created by Kaggle notebook
├── models/
│   ├── bltsm/
│   │   ├── bilstm_student_adaptive.keras
│   │   ├── tokenizer.pkl
│   │   └── label_classes.npy
│   └── bert_emotion_model_final/
│       ├── config.json
│       ├── model.safetensors
│       ├── tokenizer.json
│       ├── tokenizer_config.json
│       ├── special_tokens_map.json
│       └── label_mapping.json
├── notebooks/
│   └── kaggle_training.ipynb
└── src/
    ├── __init__.py
    ├── preprocessing.py
    ├── model.py
    ├── bert_model.py
    └── predict.py
```

---

## ⚙️ Setup Instructions

### Step 1 — Get Gemini API Key
1. Go to https://aistudio.google.com/
2. Sign in with Google
3. Click "Get API Key" → "Create API Key"
4. Copy the key into `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   ```

### Step 2 — Local Setup (Windows)
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

### Step 3 — Kaggle Training (GPU required — do NOT run locally)
1. Go to https://www.kaggle.com/
2. Create a new Notebook
3. Enable GPU: Settings → Accelerator → GPU T4 x2
4. Add datasets via "Add Data":
   - `google-research-datasets/go_emotions`
   - `atharvjairath/empatheticdialogues`
   - `kaggle/isear-dataset` (or similar)
5. Copy all cells from `notebooks/kaggle_training.ipynb` in order
6. Run All
7. Download output files from `/kaggle/working/`
8. Place files into local folders:
   - `bilstm_student_adaptive.keras` → `models/bltsm/`
   - `tokenizer.pkl` → `models/bltsm/`
   - `label_classes.npy` → `models/bltsm/`
   - `bert_emotion_model_final/` (entire folder) → `models/`
   - `emotion_text_dataset.csv` → `data/`

### Step 4 — Run the App
```bash
streamlit run app.py
```
Open http://localhost:8501 in your browser.

---

## 🎯 Features

- **Dual-model emotion detection**: BiLSTM (fast, student-adaptive) + BERT (deep semantic)
- **5 emotion classes**: Bored, Confident, Confused, Curious, Frustrated
- **Mixed emotion detection**: Flags when multiple emotions score above 15%
- **Gemini AI responses**: Personalized, field-specific learning guidance (falls back to templates)
- **Analytics dashboard**: Emotion distribution, confidence timeline, field breakdown
- **CSV logging**: Every interaction saved for continuous improvement

---

## 🔑 Key Technical Notes

| Parameter | Value |
|---|---|
| BiLSTM max sequence length | 80 tokens |
| BERT max length | 128 tokens |
| Keyword boost multiplier | 10× |
| Mixed emotion threshold | 15% |
| BERT class weights | [Bored:1.2, Confident:1.8, Confused:0.6, Curious:1.0, Frustrated:1.4] |

---

## ⚠️ Edge Cases Handled

- Models not found → friendly Streamlit error with instructions
- Gemini API key missing/invalid → silent fallback to template responses
- Input < 3 characters → user warning, no inference
- CSV files auto-created on first interaction
