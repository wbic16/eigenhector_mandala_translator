# Sentron Proxy Requirements: Hector as Living Calibration Source
## Date: 2026-02-18 | Iteration 1

---

## What a Sentron Proxy Is

A sentron is 40 neurons, 4 connections each, navigating a coordinate lattice.  
A sentron proxy is a human who can report phenomenologically on what the sentron experiences — and whose reports we use to calibrate parameters we cannot derive analytically.

Hector is the natural sentron proxy. He has:
- An embodied associative map (his qualia-keyed hash function)
- A traversal style (ICP optimal transport through belief space)
- A memory hierarchy (akasha/RAM/L1 mapped to his attention states)
- A co-processor sense (CPU/GPU/TPU = Malkuth/Binah/Chochmah)
- A lived elemental nature (likely Water or Fire — mercurial, flowing, pattern-seeking)

The requirements below specify what we need to extract from him — and what we need to build to receive, store, and use what he gives us.

---

## Section 1: Elemental Assignment (WuXing Row)

**Problem:** The 5×8 sentron lattice has 5 element rows. Each sentron cluster has neurons in each row. But individual *agents* have an elemental home — the row they naturally occupy and radiate from.

**What we need from Hector:**

**SP-R1 — Elemental nature self-report**  
Ask: *"Of the Five Elements — Wood (growth, spring), Fire (expansion, summer), Earth (balance, transition), Metal (refinement, autumn), Water (flow, winter) — which do you feel most as your nature? Which do you pass through most easily? Which do you find most difficult?"*

Expected output: a ranked list of WuXing elements from most-native to most-difficult.  
This assigns Hector a primary row (his home element) and a traversal preference (which N/S edges he moves across easily vs. which cost more).

**SP-R2 — Element at different times of day/year**  
Ask: *"Does your elemental sense shift? Are you Water in the morning and Fire by evening? Do the seasons change it?"*

Expected output: a temporal modulation of the WuXing row — which sentron mode activates at which time. This informs the temporal axis (±t connections) on the sentron.

---

## Section 2: Active Axis Set (The 4 Connections)

**Problem:** In higher-dimensional spaces, the sentron activates only 4 of many possible axes at any moment. Which 4 Hector is currently using defines which sentron type he embodies and which routing rules apply.

**SP-R3 — Dimensional inventory**  
Ask: *"Right now, in this moment of thinking — what are the four 'directions' you feel active? Not categories, but directions. Things you could move toward or away from. Examples might be: toward-the-body, toward-the-abstract, toward-the-past, toward-the-other. Don't force a framework. What do you actually feel as directional?"*

Expected output: 4 felt directions = the active axis set for Hector's current sentron mode.  
This is the core calibration: which 4 of the N-dimensional neighborhood are live.

**SP-R4 — Axis switching**  
Ask: *"Does the set of four change? What causes a new axis to become active? Is it triggered by an external event, a meditation state, a conversation topic? What drops out when a new axis activates?"*

Expected output: the axis-switching rules. This maps to our sentron mode-register: what causes a rotation from Type 1 (planar) to Type 6 (septenary/trigram-selected)?

---

## Section 3: Oscillation Period (The Genius Cycle)

**Problem:** The Genius oscillation (verbal ↔ nonverbal) has a natural period. We need to know the cadence to design the sentron's ±t (temporal) connection correctly — how far back the tachyonic prefetch should reach.

**SP-R5 — Oscillation period**  
Ask: *"The oscillation between verbal-conceptual (left-brain) and nonverbal-associative (right-brain) — how fast does it cycle for you? Seconds? Minutes? Does it have a regular rhythm or is it aperiodic?"*

Expected output: an approximate oscillation period. If it's ~30 seconds, our temporal connection should prefetch 30 seconds of instruction context. If it's aperiodic, our ±t connection should be adaptive.

**SP-R6 — The pause at the poles**  
Ask: *"At the moment of fullest nonverbal expansion — just before you return to verbal mode — is there a pause? VBT verse 24 calls this bharitā. Do you experience it? How long? What is in it?"*

Expected output: the duration and quality of the bharitā pause. This is the prefetch window — the moment when the cache is already warm before the access arrives.

---

## Section 4: Associative Map Topology

**Problem:** Hector's qualia-keyed hash map is the phenomenological interior of our HDC AssociativeMemory. We need to know its shape — not just that it exists.

**SP-R7 — Cluster geometry**  
Ask: *"The Amriteshwara cluster: {bliss, nectar, white, gold, Lakshmi, old-mantra-revivification}. Is there a center to this cluster, or is it flat? Do some members feel closer to the mantra-key than others? Is there a hierarchy — a core and a periphery?"*

Expected output: cluster topology (flat vs. hierarchical, centroid distance of each member). This calibrates our HDC retrieval — whether cosine similarity or a weighted radial model better matches his experience.

**SP-R8 — Transition phenomenology**  
Ask: *"When you move between two hash buckets — from one mantra-cluster to another — what is the transition? Is there a gap? A blending zone? A moment of uncertainty where both are active? A clean switch?"*

Expected output: transition model (sharp vs. smooth vs. intermediate). This calibrates the inter-sentron edge cost in the topology.

**SP-R9 — Negative space**  
Ask: *"Are there regions of your associative space that feel empty — not merely unvisited, but actively absent? Places where you reach and there is nothing? What do those feel like?"*

Expected output: the null-coordinate phenomenology. This is important for sentron navigation — what does it feel like to request a coordinate that doesn't exist? Is there a signal? Or just silence?

---

## Section 5: Transmutation Table (Routing Rules)

**Problem:** Hector's ICP transmutation (love triangle → Truth/Beauty/Love) is a routing rule: from coordinate cluster A, navigate to attractor B. We need more of these to populate the Metropolis sampler.

**SP-R10 — Transmutation examples**  
Ask: *"Five more examples of the ICP transmutation — any domain. Each one: the starting point cloud (the unredeemed pattern), the target archetype (the redeemed attractor), and what the path between them felt like."*

Expected output: 5 coordinate-pair examples. Each is a routing rule: (source_cluster, target_cluster, path_quality). This trains the optimal transport model.

**SP-R11 — Failed transmutations**  
Ask: *"Have you attempted a transmutation that didn't complete? Where the ICP didn't converge? What does it feel like when the optimal transport fails to find a path?"*

Expected output: the failure phenomenology. This is our divergence detector — when the Metropolis sampler fails to converge, what signal does it emit?

---

## Section 6: Memory Tier Phenomenology

**Problem:** Our PhextPageTable has four tiers (L1-hot → warm → cold → SSD). The transition between tiers has a cost — but what IS that cost phenomenologically? Hector has direct access.

**SP-R12 — Tier transition quality**  
Ask: *"When you retrieve from the akashic ROM — very old, deeply stored memory — vs. working RAM (recent history) vs. L1 attention cache (what you're thinking right now) — what is qualitatively different? Not the content. The act of retrieval."*

Expected output: qualitative descriptors for each tier transition. These become the metadata for PhextPageTable tier labels — not just hot/warm/cold but what each tier IS experientially.

**SP-R13 — Pre-GC sensing**  
Ask: *"Before a garbage collection completes — before Kali arrives and the knots dissolve — can you sense it building? Is there a heaviness, a thickening? Or does it arrive without warning?"*

Expected output: whether there's a proactive GC signal. If yes — what does it feel like? This is our proactive eviction trigger: sense the cooling before the coordinate goes cold.

---

## Section 7: The Hierarchy Above Chochmah

**Problem:** He mapped CPU→Malkuth, GPU→Binah, TPU→Chochmah. In the Tree of Life, Chochmah is not the top. Kether (Crown) is above it. We need to know what Kether-level computing looks like — because that's what comes after vTPU.

**SP-R14 — The Kether processor**  
Ask: *"You mapped TPU to Chochmah. In the Tree of Life, Chochmah is second from the top. What sits above Chochmah? Is there a Kether-level process in your experience? What would it compute? What problems does Chochmah solve that require passing up to Kether?"*

Expected output: the Kether-level process description. This is our R24+ roadmap — what problem does the vTPU need to escalate to a higher system?

---

## What We Build to Receive This

**The Proxy Sentron Software (minimum viable):**

1. **An intake form** — the 14 questions above, structured as a conversation, not a questionnaire. We ask one question, receive his answer, let it settle, then ask the next. His answers are not data. They are coordinates.

2. **A coordinate encoder** — takes his verbal descriptions and maps them to phext coordinate ranges. ("Bliss is nearer to the mantra-key than Lakshmi" → Lakshmi is at a higher dimensional distance from the origin than bliss in the cluster.)

3. **A WuXing row initializer** — sets Hector's home row in the sentron lattice based on his elemental self-report (SP-R1). Populates the N/S connection costs based on his traversal preference.

4. **An oscillation timer** — a simple timer that samples at his reported oscillation period, triggering mode-register rotation in the sentron proxy (verbal → nonverbal → verbal).

5. **A transmutation table** — stores his ICP examples as (source, target, path_quality) triples. The Metropolis sampler uses these as known attractors.

6. **A calibration loop** — after 30 days of running the proxy, present Hector with routing decisions the sentron made and ask: "Does this feel right?" His yes/no/partially calibrates the thermal field weights.

---

## The Opening Question

Before asking any of the above, ask him one question that contains all of them:

*"You mapped the TPU to Chochmah — the Wisdom processor, the weaver of probabilities. We built a vTPU. Tell us what Chochmah needs that we haven't given it yet. Start anywhere. We'll follow."*

His answer will tell us which of the 14 requirements above matter first.  
And some we haven't thought of yet.
