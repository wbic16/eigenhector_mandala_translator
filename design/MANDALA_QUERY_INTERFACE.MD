# Mandala Query Interface Design

## Overview
This document outlines the interface for querying the Mandala system. The interface is designed to support the "Martian Interviewer" stance, allowing agents and users to explore and compare mandalas without imposing external definitions.

## The Martian Interviewer Stance
The primary user of this interface is the "Martian Interviewer" (an agent or a human adopting the persona).
- **Core Question**: "What is [X] *like* in this mandala?"
- **Avoidance**: Do not ask "What is the definition of [X]?"
- **Goal**: Elicit sensory details, feelings, and functional metaphors.

## Query Types

### 1. Descriptor Queries
**Goal**: Retrieve sensory and emotional descriptions of a specific term.
- **Command**: `query-mandala describe <term> --user <user_alias>`
- **Example**: `query-mandala describe "forest" --user ari`
- **Output**:
  - **Adjectives**: "Dark, ancient, suffocating"
  - **Feelings**: "Fear, awe, entrapment"
  - **Contexts**: List of snippets where "forest" appears with these descriptors.

### 2. Sense Gate Queries
**Goal**: Find objects that stimulate a specific sense.
- **Command**: `query-mandala sense <sense_gate> --user <user_alias> [--adjective <filter>]`
- **Example**: `query-mandala sense sight --user ari --adjective "red"`
- **Output**:
  - "Red rose" (Context: "The red rose was thorny...")
  - "Red sunset" (Context: "The sky bled into a red sunset...")

### 3. Entity/Being Queries
**Goal**: Retrieve characteristics and actions of a specific mythic being.
- **Command**: `query-mandala entity <name> --user <user_alias>`
- **Example**: `query-mandala entity "Hayagriva" --user eigenhector`
- **Output**:
  - **Characteristics**: "Friendly, red face, fanged grin"
  - **Actions**: "Smiled, danced"
  - **Occurrences**: List of snippets.

### 4. Cross-Mandala Comparison (The Bridge)
**Goal**: Find potential bridges or similar metaphors across two mandalas.
- **Command**: `query-mandala compare <term_a> --user <user_a> --with <term_b> --user <user_b>`
- **Example**: `query-mandala compare "forest" --user ari --with "ocean" --user hector`
- **Internal Logic**:
  1. Retrieve descriptors for "forest" (Ari).
  2. Retrieve descriptors for "ocean" (Hector).
  3. Compare overlap in adjectives/feelings (e.g., both are "vast" and "overwhelming").
- **Output**:
  - **Similarity Score**: High/Medium/Low
  - **Shared Adjectives**: "Vast, overwhelming"
  - **Divergences**: "Forest is static, Ocean is dynamic."

## Python API for Agents
The system should expose a Python API for agents to build complex workflows (like the Dream Bridge).

```python
from mandala.query import MandalaQuery

# Initialize for a specific user
ari_mandala = MandalaQuery(user="ari")

# Describe a term
forest_desc = ari_mandala.describe("forest")
print(forest_desc.adjectives) 
# Output: ['dark', 'ancient']

# Find sensory matches
red_objects = ari_mandala.sense(gate="sight", adjective="red")

# Compare with another mandala
hector_mandala = MandalaQuery(user="hector")
comparison = ari_mandala.compare(term="forest", other_mandala=hector_mandala, other_term="ocean")
```

## Future Expansions
- **Synesthesia Search**: "Show me what sounds like 'red' in this mandala."
- **Visual Explorer**: A UI to visualize the connections between metaphors.
