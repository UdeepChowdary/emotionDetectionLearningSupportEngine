# Product Requirements Document (PRD) — Emotion Detection & Learning Support Engine

**Project Name:** Emotion Detection & Learning Support Engine  
**Version:** 1.0  
**Status:** Approved / Production  

---

## 1. Executive Summary & Product Vision

Students frequently experience emotional roadblocks during self-directed learning—ranging from frustration over complex concepts to boredom from repetitive exercises. Traditional e-learning platforms treat all student queries purely as factual lookups, ignoring the student's affective state.

The **Emotion Detection & Learning Support Engine** bridges this gap by combining machine learning emotion detection with generative AI assistance. It detects 5 specific educational emotional states (**Bored**, **Confident**, **Confused**, **Curious**, **Frustrated**), flags mixed emotions, and generates personalized, empathetic learning support to help students stay motivated and overcome friction.

---

## 2. Target Audience & Core Use Cases

### Target Users
1. **K-12 & University Students:** Individuals engaging in self-study or online learning who need adaptive guidance when stuck.
2. **Educators & Content Creators:** Teachers tracking overall student mood patterns and common conceptual hurdles.

### Key Use Cases
- **Scenario A (Confusion/Frustration):** A student submits *"I don't understand recursion, it's impossible and annoying"*. The system identifies **Frustrated (65%)** and **Confused (30%)**, validates their feelings, and breaks recursion down into real-world visual analogies.
- **Scenario B (Boredom):** A student inputs *"This history reading is so dull and dry"*. The system detects **Bored (85%)**, acknowledges the tedium, and recommends gamified revision techniques.
- **Scenario C (Curiosity):** A student inputs *"What if we combine quantum computing with neural networks?"*. The system detects **Curious (90%)** and provides deep dive resources and experimental prompts.

---

## 3. Functional Requirements

| Req ID | Feature Name | Description & Acceptance Criteria | Priority |
| :--- | :--- | :--- | :--- |
| **FR-01** | **Multi-Class Emotion Classification** | Must classify text into 5 distinct target classes: *Bored*, *Confident*, *Confused*, *Curious*, *Frustrated*. Minimum acceptable validation accuracy $\ge 90\%$. | **P0 (Critical)** |
| **FR-02** | **Dual-Model Inference** | Must run BiLSTM and fine-tuned BERT models concurrently. Must present comparative probability scores for both models in the UI. | **P0 (Critical)** |
| **FR-03** | **Mixed Emotion Detection** | Flag and display secondary emotions whenever class probability scores exceed $15\%$. | **P1 (High)** |
| **FR-04** | **Generative AI Learning Support** | Integrate Google Gemini 2.5 Flash API to deliver customized empathy and step-by-step study strategies within $<1.5$ seconds. | **P0 (Critical)** |
| **FR-05** | **Offline Fallback Handler** | Provide static empathy response templates when Gemini API key is unconfigured or offline. | **P0 (Critical)** |
| **FR-06** | **Live Analytics Dashboard** | Render interactive Plotly charts showing historical emotion distribution, average model confidence over time, and filtering by domain. | **P1 (High)** |
| **FR-07** | **Data Persistence & Audit Log** | Automatically log each transaction into SQLite (`app.db`) and CSV (`emotion_response_examples.csv`). | **P1 (High)** |
| **FR-08** | **Short Input Safeguard** | Reject text inputs under 3 characters with an informative warning to prevent invalid inference on whitespace/empty inputs. | **P2 (Medium)** |

---

## 4. Non-Functional Requirements (NFRs)

### 4.1 Performance & Latency
- **BiLSTM Inference Speed:** $\le 50\text{ ms}$ on standard single-core CPU instances.
- **BERT Inference Speed:** $\le 300\text{ ms}$ on standard CPU instances.
- **AI Response SLA:** End-to-end processing (preprocessing + inference + Gemini generation) completed in $\le 2.0\text{ seconds}$.

### 4.2 Resource Efficiency & Deployment Footprint
- **Memory Optimization:** Configured CPU-only PyTorch builds without CUDA binaries, reducing RAM consumption from ~2.7GB to **<400MB**, preventing cloud deployment `SIGKILL` host crashes.

### 4.3 Reliability & Resilience
- Graceful degradation: The core emotion classification remains fully operational even if external generative API services fail.
- Auto-creation: SQLite databases and CSV files are created automatically at runtime if missing.

---

## 5. System Specifications & Technical Constraints

```
emotion-detection/
├── project_files/
│   ├── app.py                         ← Streamlit interface
│   ├── requirements.txt             ← Managed Python dependencies
│   ├── models/
│   │   ├── bltsm/                   ← Keras BiLSTM artifacts
│   │   └── bert_emotion_model_final/← Fine-tuned BERT model
│   ├── src/
│   │   ├── preprocessing.py         ← Text cleaning & keyword boosting
│   │   ├── model.py                 ← BiLSTM pipeline
│   │   ├── bert_model.py            ← BERT pipeline
│   │   ├── predict.py               ← Dual-model coordinator
│   │   └── database.py              ← SQLite database logger
```

---

## 6. Edge Cases Handled

1. **Missing Trained Model Files:** Displays a clear Streamlit warning box detailing exact missing file paths rather than throwing unhandled exceptions.
2. **Missing/Invalid Gemini API Key:** Silently switches to static pre-defined pedagogical templates without breaking user flow.
3. **Ambiguous or Neutral Inputs:** Applies keyword weight multipliers ($10\times$) to resolve tied probabilities effectively.
4. **Special Character & URL Noise:** Strips links, HTML tags, and punctuation automatically during text preprocessing.
