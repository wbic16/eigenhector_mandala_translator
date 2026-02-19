# Indexing System Design

## Overview
The goal of the indexing system is to enable fast, semantic retrieval of concepts, sensory experiences, and entities across different "mandalas" (user corpora).

## Key Indices

### 1. Sense Gate Index (`sense_gates.json`)
Maps sensory experiences (sight, sound, smell, taste, touch, proprioception, interoception) to their occurrences in the corpus.

**Target Use Case:** "What smells like 'rose' in Eliade's mandala?"

**Schema:**
```json
{
  "sight": [
    {
      "term": "red rose",
      "adjectives": ["thorny", "beautiful"],
      "context": "The **red rose** was thorny but beautiful...",
      "doc_id": "00001.md",
      "line_number": 42
    }
  ],
  "smell": [
    {
      "term": "rose",
      "adjectives": ["sweet", "faint"],
      "context": "A faint **rose** scent lingered...",
      "doc_id": "00005.md",
      "line_number": 12
    }
  ]
}
```

**Extraction Strategy:**
- **NLP/LLM Assisted:** Use an LLM or NLP tool to scan documents and extract sensory descriptions.
- **Classification:** Classify each extraction into one of the 7 sense gates.
- **Synesthesia Support:** Allow cross-referencing (e.g., query "sharp" in "sight" might return "sharp" in "touch").

### 2. Mythic Being Index (`mythic_beings.json`)
Maps mythic beings, entities, and characters to their descriptions and actions within the specific mandala.
**Critical:** Do not assume "Hayagriva" in Corpus A is the same as "Hayagriva" in Corpus B. Index them as distinct entities within their respective mandalas.

**Target Use Case:** "Compare Sasha's Ekajati with Eigenhector's Cernunnos."

**Schema:**
```json
{
  "beings": [
    {
      "name": "Hayagriva",
      "aliases": ["The Horse-Necked One"],
      "characteristics": ["red face", "fanged grin", "friendly"],
      "actions": ["smiled", "danced"],
      "occurrences": [
        {
          "doc_id": "00002.md",
          "context": "Hayagriva smiled at me with his friendly red face...",
          "line_number": 15
        }
      ]
    }
  ]
}
```

**Extraction Strategy:**
- **Entity Recognition:** Identify proper nouns and personified concepts.
- **Attribute Extraction:** Extract adjectives and verbs associated with the entity.
- **Context Preservation:** Store the sentence or paragraph where the entity appears.

## Cross-Referencing & Backlinks
Every index entry must include a "backlink" to the source document.
- **`doc_id`**: The filename in the `docs/` directory (e.g., `00001.md`).
- **`line_number`**: The approximate line number where the match occurs.
- **`context`**: A snippet of text surrounding the match (e.g., +/- 100 characters).

 This structure allows agents to:
1.  Find a match in the index.
2.  Retrieve the full document content using `doc_id`.
3.  Locate the exact position using `line_number` or text search for the `context`.

## Extensibility
New indices can be added by creating a new JSON file in the `indices/` directory.
- Example: `emotional_states.json`, `locations.json`.
- The schema should always include `occurrences` with `doc_id` and `context`.

## Integration with Dream Bridge
These indices serve as the "raw material" for the Martian Interviewer.
- When the Martian asks "What is [Keyword] like?", the agent queries the `sense_gates` and `mythic_beings` indices for that keyword to get initial descriptors and context.
