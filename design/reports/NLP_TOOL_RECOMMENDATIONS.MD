# Python NLP Tool Recommendations for Corpus Indexing

## Executive Summary

To upgrade `tools/index_corpus.py` from basic regex matching to a semantic "Martian Interviewer" system, we recommend a hybrid approach:
1.  **SpaCy** for robust structural processing and initial Entity Recognition.
2.  **Sentence Transformers (SBERT)** for "Sense Gate" synesthesia and semantic search (e.g., finding "sharp red" concepts).
3.  **LLM-based Extraction (via API or Local)** for complex "Mythic Being" characterization and context extraction.

## 1. Sense Gate Indexing (Synesthesia & Semantic Search)

**Current Problem:** The current regex approach fails on:
- **Context:** "Blue" might mean sad, not the color.
- **Implicit Sensory Details:** "The scent of rain" doesn't strictly match a list of chemical smells but is a strong olfactory signal.
- **Cross-Modal Queries:** Matching "sharp" (touch) to "red" (sight).

**Recommended Tool: Sentence Transformers (sbert.net)**
-   **Library:** `sentence-transformers`
-   **Why:** It converts sentences/paragraphs into dense vector embeddings.
-   **Application:**
    -   Create embeddings for the 7 sense keys (e.g., embedding of "visual experience", "olfactory experience").
    -   Score paragraphs against these sense keys to classify them into sense gates dynamically.
    -   **Search:** Allows the user to ask "What smells like X?" by comparing the vector of "X" to the vectors of all indexed sensation snippets.

**Alternative/Add-on: NLTK / TextBlob**
-   Useful for simple noun-phrase chunking if embeddings are too heavy, but less semantically aware.

## 2. Mythic Being Extraction (Custom Entities)

**Current Problem:** "Mythic beings" in this corpus are often custom (e.g., "Energon Starbird") or context-specific variants ("Eigenhector's Hayagriva" vs "Hindu Hayagriva"). Standard NER (Named Entity Recognition) models are trained on people/orgs (PER/ORG/LOC) and will likely miss these or misclassify them.

**Recommended Tool: LLM-Assisted Extraction (Instructor / Outlines)**
-   **Library:** `openai` (or `anthropic`, `ollama` for local) + `instructor` (for structured JSON output).
-   **Why:** LLMs effectively understand context and can extract custom fields like "Actions", "Characteristics", and distinguish between "The Horse-Necked One" and a literal horse.
-   **Workflow:**
    1.  Pass text chunk to LLM.
    2.  Prompt: "Extract all mythic beings, their aliases, descriptions, and actions."
    3.  Force JSON output matching your `mythic_beings.json` schema.

**Lighter Alternative: SpaCy with Entity Ruler**
-   **Library:** `spacy`
-   **Why:** You can manually add patterns for known beings.
-   **Limitation:** It won't discover *new* or *unknown* beings effectively without extensive manual rule maintenance.

## 3. Data Cleaning & Preprocessing

**Current Problem:** Substack boilerplate ("Subscribe", "Share", comments) pollutes the index.
-   The current `mask_content` in `index_corpus.py` is a good start but fragile.

**Recommended Tool: Trafilatura or BeautifulSoup**
-   **Library:** `trafilatura` (focused on main text extraction) or `beautifulsoup4`.
-   **Why:** `trafilatura` is excellent at extracting the main content text and discarding sidebars, footers, and "subscribe" buttons automatically.

## Proposed Tech Stack Upgrade

| Feature | Primary Tool | Fallback / Lightweight |
| :--- | :--- | :--- |
| **Preprocessing** | `trafilatura` | `BeautifulSoup` + Regex |
| **NLP Pipeline** | `spacy` (en_core_web_sm/lg) | `nltk` |
| **Sense Indexing** | `sentence-transformers` (all-MiniLM-L6-v2) | `spacy` Similarity |
| **Mythic Beings** | LLM (GPT-4o or Local Llama 3) via `instructor` | `spacy` EntityRuler |
| **Storage** | `chromadb` or `faiss` (for vectors) + JSON | JSON (current) |

## Implementation Strategy

1.  **Phase 1 (Immediate - "Sense Gates"):**
    -   Replace regex keywords with `sentence-transformers`.
    -   Compute similarity scores between text sentences and "sense gate description prompts".
    -   Threshold the score to decide if a sentence belongs to a sense gate.

2.  **Phase 2 (Immediate - "Mythic Beings"):**
    -   Use a small efficient LLM call to extract entities from documents.
    -   Consolidate references (resolve "He", "The Starbird" to "Energon Starbird").

3.  **Phase 3 (Storage):**
    -   As the corpus grows, JSON processing will slow down. Introduce a lightweight vector store like `chromadb` (which uses SQLite under the hood) to store the embeddings for fast retrieval.

## Code Snippet Example (Concept)

```python
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define sense anchors
sense_anchors = {
    "sight": model.encode("Visual description, color, light, appearance"),
    "smell": model.encode("Olfactory description, scent, smell, aroma"),
    # ...
}

def classify_sense(text_chunk):
    chunk_embedding = model.encode(text_chunk)
    results = {}
    for sense, anchor in sense_anchors.items():
        score = util.cos_sim(chunk_embedding, anchor)
        if score > 0.4:  # Threshold
            results[sense] = score
    return results
```
