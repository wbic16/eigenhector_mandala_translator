# Experiment: NLP Indexing for Dream Interview Method (DIM)

**Goal**: Determine the optimal combination of NLP tools and indexing strategies to support the "Martian Interviewer" stance and cross-mandala bridging.

## Context
Please read the following documents to understand the system architecture and goals:
- `README.md`
- `design/INDEXING_SYSTEM_DESIGN.MD`
- `design/PROMPT1.MD`
- `skills/CORPUS_STRUCTURE.MD`
- `skills/CORPUS_REGISTRY.MD`
- `skills/DreamBridge/DIM.MD` (Dream Interview Method)
- `design/reports/NLP_TOOL_RECOMMENDATIONS.MD` (Contains validated tool choices)

## Evaluation Criteria
- **Recall**: Can we find entities/metaphors that regex misses? (e.g. "The red flower" vs "a flower that was red")
- **Precision**: Do we avoid capturing "Subscribe now" as a metaphor?
- **Token Efficiency**: Does the indexing reduce the context window needed for the final "Martian Interview" agent?
- **"Vibe" Accuracy**: Subjective assessment of the "Vibe Search" results.

## Suggested Tech Stack (from Recommendations)
- **Synesthesia/Vibe**: Sentence Transformers (`sentence-transformers`) for vector embeddings.
- **Entities**: SpaCy (structural extraction) or small LLM (semantic extraction).
- **Storage**: Prototype usage of a lightweight vector store (e.g. ChromaDB) vs flat JSON.

## Objective
We need to pre-index the corpus to support high-recall, context-rich queries without consuming excessive tokens during runtime. The focus is on capturing **embodied processes**, **sense gate metaphors**, and **mythic beings**.

**Key Metaphor**: Imagine projecting a small graph structure (an idea, relationship, or process) from one mandala onto another to find the most structurally similar subgraph.

## Constraints & Environment
- **Corpus Size**: ~10 mystics, ~100 docs each (small enough for heavier analysis).
- **Compute vs. Tokens**: Favor ahead-of-time computational expense over runtime token usage.
- **Recall Priority**: High recall is crucial to find subtle structural similarities.
- **Data Source**: Use `C:\Users\hecto\Documents\mystic_corpus` as the sample corpus.
- **Workspace**:
    - **Working Directory**: Perform all experiments locally in `C:\Users\hecto\Projects\experiments\nlp_indexing\`.
    - **Isolation**: Create a new Python virtual environment/workspace here to avoid polluting the main repository.
- **Output & Iteration**:
    - **Incremental Experimentation**: Agents should feel free to run multiple small experiments to test different hypotheses or tools.
    - **Reporting**: Write detailed results of your specific run to `C:\Users\hecto\Projects\experiments\nlp_indexing\RUN_X.MD` where `X` is an incrementing number (e.g., `RUN_1`, `RUN_2`).
    
    - **Standardized Logging for Continuity (CRITICAL)**:
        - You MUST maintain a running log of findings in `C:\Users\hecto\Projects\experiments\nlp_indexing\EXPERIMENTS_LOG.MD`.
        - **Read First**: Before starting any experiment, read `C:\Users\hecto\Projects\experiments\nlp_indexing\EXPERIMENTS_LOG.MD` to see what has already been tried and what the recommended "Next Steps" are.
        - **Log Format**: Append a new entry for your experiment using this format:
            ```markdown
            ## Experiment [ID]: [Title]
            **Date**: [YYYY-MM-DD]
            **Goal**: [Brief goal]
            
            ### Key Findings
            - [Finding 1]
            - [Finding 2]
            
            ### Artifacts & Resources (Context Recovery)
            - [Path to reused embeddings/indices/data] (Crucial for next agent to know what exists so they don't recompute)
            
            ### Validated Hypotheses
            - [ ] Hypothesis A (Confirmed/Refuted)
            
            ### Recommended Next Steps for Next Agent
            - [Specific instruction for the next agent]
            ```
        - **Recovering Context**: If you generate expensive data (like embeddings or a large index), DO NOT delete it. Save it to `C:\Users\hecto\Projects\experiments\nlp_indexing\artifacts\` and note its location in the `EXPERIMENTS_LOG.MD` so the next agent can load it instead of re-computing.

    - **Deliverables**:
        - Explore and compare "Regex vs Embedding" for Sense Gate extraction, documenting pros and cons.
        - Explore methods for entity extraction based on *roles* (e.g. "The Protector", "The Guide") rather than just names.
        - Explore and propose ways to visualize the "Graph Projection" (connections between beings and metaphors).
        - **Flexible Exploration**: You are encouraged to follow interesting threads and deviations if they promise better insights into the core goal of "Martian Interviewer" support.
    
    - **Iterative Process Improvements**: Suggest improvements to the codebase or tooling that would make *future* iterative experimentation more efficient (e.g. a standard evaluation harness, automated metric calculation, or better corpus sampling tools).

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

