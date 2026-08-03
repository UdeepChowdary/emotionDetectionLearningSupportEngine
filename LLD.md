# Low-Level Design (LLD) — Emotion Detection & Learning Support Engine

**Project Name:** Emotion Detection & Learning Support Engine  
**Version:** 1.0  
**Status:** Production / Active  

---

## 1. Directory & Code Base Layout

```
emotion-detection/
├── HLD.md
├── LLD.md
├── PRD.md
├── README.md
├── requirements.txt
├── project_files/
│   ├── app.py                         ← Streamlit application entrypoint
│   ├── performance_test.py            ← Load & execution timing test script
│   ├── emotion_response_examples.csv   ← Runtime CSV transaction log
│   ├── emotion_response_mapping.csv    ← Static emotion fallback templates
│   ├── src/
│   │   ├── __init__.py
│   │   ├── preprocessing.py           ← Text cleaning & keyword boosting module
│   │   ├── model.py                   ← BiLSTM inference loader
│   │   ├── bert_model.py              ← BERT Transformer inference loader
│   │   ├── predict.py                 ← Dual-model prediction coordinator
│   │   ├── database.py                ← SQLite DB interface
│   │   └── train.py                   ← Local/Kaggle model trainer
│   ├── models/
│   │   ├── bltsm/                     ← BiLSTM weights, tokenizer, label classes
│   │   └── bert_emotion_model_final/  ← BERT weights, config, tokenizer
│   └── data/
│       └── emotion_text_dataset.csv   ← Aggregated training dataset
```

---

## 2. Detailed Module Specifications

### 2.1 Module: `src/preprocessing.py`

#### `clean_text(text: str) -> str`
- **Input:** Raw text input from user.
- **Output:** Cleaned string of lowercase words without URLs, punctuation, or NLTK English stopwords.
- **Process:**
  1. Converts input string to lower case: `text = str(text).lower()`.
  2. Strips Web URLs using Regex: `re.sub(r'http\S+|www\S+', ' ', text)`.
  3. Strips non-alphabetic characters: `re.sub(r'[^a-zA-Z\s]', ' ', text)`.
  4. Tokenizes using NLTK `word_tokenize()`.
  5. Filters out NLTK stopwords and tokens with `len <= 1`.

#### `keyword_enhance(raw_text: str, scores: np.ndarray) -> np.ndarray`
- **Input:** Uncleaned `raw_text` string and raw model softmax probability array `scores` of shape `(5,)`.
- **Output:** Renormalized probability array of shape `(5,)`.
- **Logic:**
  Applies a $10\times$ weight boost multiplier to emotion classes matching explicit keyword dictionaries:
  - **Bored:** `['bored', 'boring', 'dull', 'monotonous', 'tedious', 'sleepy']`
  - **Confident:** `['confident', 'sure', 'certain', 'understand', 'got it', 'clear', 'easy']`
  - **Confused:** `['confused', 'lost', 'unclear', "don't understand", 'stuck', 'hard']`
  - **Curious:** `['curious', 'wonder', 'interesting', 'explore', 'learn more']`
  - **Frustrated:** `['frustrated', 'annoying', "can't", 'impossible', 'hate', 'useless']`
  
  $$\text{Boosted Score}_i = \text{Score}_i \times 10.0 \quad (\text{if keyword present})$$
  $$\text{Final Score}_i = \frac{\text{Boosted Score}_i}{\sum_{j=1}^{5} \text{Boosted Score}_j}$$

#### `get_mixed_emotions(scores: dict, threshold: float = 0.15) -> list`
- **Input:** Dictionary of `{emotion_name: score_float}` and threshold float (default `0.15`).
- **Output:** Sorted list of tuples `[(emotion_name, score)]` descending for all emotions with score $\ge 0.15$.

---

### 2.2 Module: `src/model.py` (BiLSTM Classifier)

- **Model Architecture:**
  - `Embedding Layer`: Input dimension `10,000`, Output vector dimension `128`, Sequence max length `80`.
  - `SpatialDropout1D`: Dropout rate `0.2`.
  - `Bidirectional LSTM`: `64` units, returning sequences.
  - `Bidirectional LSTM`: `32` units.
  - `Dense`: `64` units with `ReLU` activation.
  - `Dropout`: Dropout rate `0.3`.
  - `Dense Output`: `5` units with `Softmax` activation.

- **Functions:**
  - `load_bilstm_model()`: Loads `.keras` model, `tokenizer.pkl`, and `label_classes.npy` from `models/bltsm/`.
  - `predict_bilstm(raw_text: str) -> dict`: Cleans text, tokenizes, pads sequence to length `80`, evaluates model, applies `keyword_enhance()`, and maps predictions to label classes.

---

### 2.3 Module: `src/bert_model.py` (BERT Transformer Classifier)

- **Model Architecture:**
  - Base Model: `bert-base-uncased` via HuggingFace `AutoModelForSequenceClassification`.
  - Sequence Length: Capped at `128` tokens.
  - Output Head: Linear classification layer mapped to 5 target emotion logits.

- **Functions:**
  - `load_bert_model()`: Loads HuggingFace model and tokenizer from `models/bert_emotion_model_final/`.
  - `predict_bert(raw_text: str) -> dict`: Prepares PyTorch tensor inputs with `attention_mask` and `input_ids`, runs forward pass, computes softmax over logits, applies `keyword_enhance()`, and returns class score dictionary.

---

### 2.4 Module: `src/predict.py` (Dual Model Coordinator)

#### `predict_emotion(text: str) -> dict`
Coordinates parallel execution of both BiLSTM and BERT prediction models:
1. Validates input length (`len(text) >= 3`).
2. Calls `predict_bilstm(text)` and `predict_bert(text)`.
3. Selects BERT results as the high-confidence primary prediction (with BiLSTM as comparative baseline).
4. Determines primary emotion (`argmax`) and mixed emotions list (`get_mixed_emotions`).
5. Returns aggregated dictionary:
   ```json
   {
     "primary_emotion": "Confused",
     "confidence": 0.824,
     "mixed_emotions": [["Confused", 0.824], ["Frustrated", 0.162]],
     "bilstm_scores": { ... },
     "bert_scores": { ... }
   }
   ```

---

### 2.5 Module: `src/database.py` (SQLite Persistence)

#### Schema Definition (`transactions` Table)
```sql
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    student_input TEXT NOT NULL,
    primary_emotion TEXT NOT NULL,
    mixed_emotions TEXT,
    bert_confidence REAL,
    bilstm_confidence REAL,
    ai_response TEXT
);
```

#### Functions:
- `init_db()`: Initializes SQLite table `app.db` if missing.
- `save_prediction(...)`: Inserts prediction payload into SQLite table.
- `get_history(limit: int = 100)`: Retrieves recent transactions for analytics display.

---

### 2.6 Module: `app.py` (Streamlit Controller & Gemini Integration)

- **Gemini API Pipeline:**
  Calls `google.generativeai.GenerativeModel('gemini-2.5-flash')` with standard prompt wrapper:
  ```text
  You are an empathetic AI learning companion. A student reported the following study challenge:
  "[Student Input]"
  Our classification model detected that they feel: [Primary Emotion] (Mixed emotions: [Mixed Array]).
  Provide:
  1. A warm, empathetic validation of their feeling.
  2. 3 actionable, step-by-step learning strategies to overcome this issue.
  3. An encouraging closing thought.
  Keep your response clear, structured in markdown, and concise (<200 words).
  ```
- **Fallback Dispatcher:**
  If `GEMINI_API_KEY` is missing or API call throws an exception, loads corresponding fallback text from `emotion_response_mapping.csv`.

---

## 3. Algorithm Complexity & Performance Specs

| Operation | Time Complexity | Space Complexity | Execution SLA |
| :--- | :--- | :--- | :--- |
| **NLTK Text Preprocessing** | $\mathcal{O}(N)$ ($N$ = text length) | $\mathcal{O}(N)$ | $<10\text{ ms}$ |
| **Keyword Boost Renormalization** | $\mathcal{O}(K \cdot E)$ ($K$=keywords, $E$=5 emotions) | $\mathcal{O}(E)$ | $<2\text{ ms}$ |
| **BiLSTM Forward Pass** | $\mathcal{O}(L \cdot H)$ ($L=80$, $H=128$) | $\mathcal{O}(L \cdot H)$ | $<50\text{ ms}$ |
| **BERT Transformer Pass** | $\mathcal{O}(L^2 \cdot D)$ ($L=128$, $D=768$) | $\mathcal{O}(L \cdot D)$ | $<300\text{ ms}$ |
| **Gemini AI API Call** | Network I/O Dependent | $\mathcal{O}(\text{Response})$ | $<1.2\text{ s}$ |
| **SQLite DB Logging** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $<5\text{ ms}$ |
