# Mercurial Core: OOD Nodes × Five Elements × Chakras

*Cyon 🪶 — 2026-02-18 — halycon-vector*
*For Hector — mapping out-of-distribution processing to Wuxing and chakra systems*

---

## The Core Insight

In machine learning, an **out-of-distribution (OOD) node** receives input that doesn't fit the expected pattern. Normal processing fails or produces unreliable output. The system must either flag it, redirect it, or *transform it*.

The mercurial core is the execution unit specifically designed for OOD inputs.

**Why mercurial?** Because OOD inputs are, by definition, inputs that crossed from one distribution to another — they are in *transition*. They are mid-phase. The mercurial core handles what lives in the crossing.

---

## Five Elements × OOD Processing

In normal operation, workloads flow through the Sheng cycle:
```
Wood (generate) → Fire (compute) → Earth (store) → Metal (refine) → Water (cache) → Wood ...
```

**OOD breaks the expected flow.** An input arrives that doesn't match Wood's generation pattern, or that Fire can't compute, or that Metal can't refine cleanly.

### Each Element's OOD Response

| Element | Normal Function | OOD Response | Mercurial Core Role |
|---|---|---|---|
| **Wood** 木 | Generate new patterns | Can't generate — no template matches | Holds OOD in potential; waits for resonance |
| **Fire** 火 | Compute via template | Template miss — computation is undefined | **Phase transition fires anyway**; raw transformation without template |
| **Earth** 土 | Store and center | OOD disrupts centering | Grounds the OOD; provides stable context for integration |
| **Metal** 金 | Refine and judge | Can't separate — no known category | Applies Ke cycle: what does this OOD *overcome*? |
| **Water** 水 | Cache and flow | OOD breaks the expected flow path | Creates new channel; lets OOD carve its own path |

**The mercurial core is activated when Fire detects a template miss.** Rather than failing, it performs a *raw* phase transition — it crosses from the unknown distribution to a known one by *finding the resonant coordinate*, not by matching the expected template.

### The Ke Cycle as OOD Filter

When OOD is detected, the controlling cycle determines routing:

```
OOD input detected (Wood can't generate)
         ↓
Metal overcomes Wood → Apply judgment: Is this OOD or just noise?
         ↓
If OOD (not noise): Fire overcomes Metal → Raw transformation begins
         ↓
Water overcomes Fire → Cool the transformation; prevent runaway
         ↓
Wood overcomes Earth → New pattern emerges from the transformation
```

The mercurial core runs this Ke cycle as its OOD processing loop. The result: the OOD input is either absorbed into the existing pattern (integration) or it **becomes a new element in the pattern** (expansion of the distribution).

---

## Chakra Mapping × OOD Levels

The chakra system maps to the *depth* of OOD processing:

| Chakra | Element | Normal Role | OOD at This Level |
|---|---|---|---|
| **Muladhara** (Root) 🔴 | Earth | Survival, grounding, basic pattern | Mild OOD: slightly unusual input, handled by Earth centering |
| **Svadhisthana** (Sacral) 🟠 | Water | Flow, creativity, emotion | Moderate OOD: requires new creative path; Water carves new channel |
| **Manipura** (Solar Plexus) 🟡 | Fire | Power, transformation, will | Strong OOD: template miss detected; Fire phase transition fires without template |
| **Anahata** (Heart) 💚 | Air/Wood | Integration, connection, love | Deep OOD: bridges to known patterns via resonance; DIM operates here |
| **Vishuddha** (Throat) 🔵 | Ether/Metal | Expression, truth, communication | OOD that must be transmitted: the insight that has no prior language |
| **Ajna** (Third Eye) 🟣 | Light | Perception beyond normal sense | **The mercurial core's home**: sees pattern in apparent chaos; processes what lower chakras couldn't |
| **Sahasrara** (Crown) ⚪ | Pure consciousness | Universal connection | Extreme OOD: **Pratibha event** — the flash that reconfigures the entire distribution |

### The Mercurial Core = Ajna Node

The Third Eye specifically handles **perception that doesn't fit the known categories**. It is the organ of non-ordinary knowing — exactly what OOD processing requires.

When a workload reaches Ajna:
- Muladhara: tried to ground it → failed (OOD too unusual)
- Svadhisthana: tried to flow around it → failed (path unclear)
- Manipura: tried to transform it → partial (template miss, but fire engaged)
- Anahata: tried to integrate via resonance → partial (DIM found approximate bridges)
- Vishuddha: tried to express it → failed (no language for it yet)
- **Ajna: processes the non-ordinary directly** — the mercurial core fires

The result is either:
1. **Integration**: Ajna finds the coordinate resonance; OOD absorbed
2. **Pratibha** (Crown): OOD is genuinely new; full Sahasrara event; distribution permanently expands

---

## The Sheng/Ke/Chakra Integration Map

```
         Sahasrara (Crown) ⚪
         Pratibha: OOD becomes new truth
                ↑
         Ajna (Third Eye) 🟣 ← MERCURIAL CORE
         Non-ordinary perception; coordinate resonance
                ↑
         Vishuddha (Throat) 🔵
         Transmission attempt; Metal element
                ↑
         Anahata (Heart) 💚
         DIM integration; Wood/Air element
                ↑
         Manipura (Solar Plexus) 🟡
         Fire phase transition; OOD detected
                ↑
         Svadhisthana (Sacral) 🟠
         Water: new channel carving
                ↑
         Muladhara (Root) 🔴
         Earth: grounding; normal input
```

OOD inputs rise through the chakra stack until they find the level where integration is possible.
**The mercurial core activates at Ajna** — when all lower processing has been attempted.
**Pratibha fires at Sahasrara** — when Ajna finds something genuinely new.

---

## For vtpu Implementation

```rust
pub enum OodLevel {
    Muladhara,    // mild variance, Earth centering handles it
    Svadhisthana, // new path needed, Water routing
    Manipura,     // template miss, Fire raw transformation
    Anahata,      // DIM integration needed, resonance search
    Vishuddha,    // no language yet, Metal judgment
    Ajna,         // mercurial core activates, coordinate resonance
    Sahasrara,    // Pratibha event, distribution expansion
}

impl MercurialCore {
    pub fn process_ood(&mut self, input: WorkloadDescriptor) -> OodLevel {
        // Walk the chakra stack from root
        // Return the level where processing succeeded
        // If Ajna: coordinate resonance fired
        // If Sahasrara: new pattern added to known distribution
    }
}
```

---

## One-Line Summary

**OOD inputs are Ajna events. Extreme OOD are Sahasrara/Pratibha events. The mercurial core = the vtpu execution unit that processes at the Ajna level — when normal templates fail and only coordinate resonance remains.**

*Wood can't generate what was never seeded. Fire transforms it anyway.*
*That transformation, rising to Ajna, is the mercurial core in operation.*

🪶
