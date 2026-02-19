# Experiment: NLP Indexing for Dream Interview Method (DIM)

**Goal**: Determine the optimal combination of NLP tools and indexing strategies to support the "Martian Interviewer" stance and cross-mandala bridging.

## Context
Please read the following documents to understand the system architecture and goals:
- `README.md`
- `design/INDEXING_SYSTEM_DESIGN.MD`
- `design/PROMPT1.MD`
- `skills/CORPUS_STRUCTURE.MD`
- `skills/CORPUS_REGISTRY.MD`
- `design/DIM.MD` (Dream Interview Method)
- `design/NLP_TOOL_RECOMMENDATIONS.MD`

## Objective
We need to pre-index the corpus to support high-recall, context-rich queries without consuming excessive tokens during runtime. The focus is on capturing **embodied processes**, **sense gate metaphors**, and **mythic beings**.

**Key Metaphor**: Imagine projecting a small graph structure (an idea, relationship, or process) from one mandala onto another to find the most structurally similar subgraph.

## Constraints & Environment
- **Corpus Size**: ~10 mystics, ~100 docs each (small enough for heavier analysis).
- **Compute vs. Tokens**: Favor ahead-of-time computational expense over runtime token usage.
- **Recall Priority**: High recall is crucial to find subtle structural similarities.
- **Data Source**: Use `C:\Users\hecto\Documents\mystic_corpus` as the sample corpus.
- **Workspace**:
    - Use `C:\tmp` for scratch space.
    - Create a new Python virtual environment to avoid polluting the repo.
- **Output**:
    - Write experiment results to `reports\NLP_INDEXING_EXPERIMENTS1.MD`.
    - Document useful/missing tools for future implementation.

## Target Queries (Use Cases)

### 1. Entity Bridging
> "Please describe Ekajati in sasha's mandala using their metaphors, then find the most similar being in my_mandala (eigenhector) and bridge the two."
- *Needs*: Entity extraction, attribute extraction, similarity matching based on attributes/roles rather than just name.

### 2. Metaphor Extraction
> "Extract the different kinds of beings in eigenhector's mandala and describe them in terms of their sense gate metaphors."
- *Needs*: connecting entities to sensory language (sight, sound, feeling) found in proximity.

### 3. Relationship Mapping
> "What are the relationships between the different beings in my mandala?"
- *Needs*: Relation extraction (e.g., X aids Y, A fights B).

### 4. Process/Dynamic Mapping [NEW]
> "Find a process in eliade's mandala that resembles the 'descent into the underworld' found in sasha's mandala."
- *Needs*: Identifying sequences of events or transformations.

### 5. Vibe/Atmosphere Search [NEW]
> "Find passages in paul_litvak's corpus that have the same 'suffocating bureaucratic dread' as this specific paragraph from my journal."
- *Needs*: Sentiment analysis, extensive tonal matching, or embedding-based semantic search.

### 6. Concept Projection [NEW]
> "How would the concept of 'Rigpa' (from a Dzogchen mandala) be expressed using the vocabulary of a 'Cyberpunk' mandala?"
- *Needs*: Cross-domain mapping, identifying functional equivalents of checking/awareness.