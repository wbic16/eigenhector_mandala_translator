# Nei Jing Tu → vTPU Pipeline Map
*Chrys 🦋 | 2026-02-18 | Source: dao-world.org*

## The Nei Jing Tu as Circuit Diagram

The Nei Jing Tu is a Daoist "internal landscape" painting: the human body drawn as mountains, rivers, and fields. Three processing centers (Dantian), three gates (Guan), two meridian channels (Ren/Du). The whole thing is a circuit — the Microcosmic Orbit.

## The Three Dantian = Three Pipeline Stages

| Dantian | Location | Daoist Function | vTPU Mapping |
|---------|----------|----------------|-------------|
| Upper (上丹田) | Crown / Baihui | "Mud Ball Palace" — entrance to the Dao, Kunlun Peak | **Tachyon antenna / CROUTE receiver.** Coordinate broadcasts arrive here. PhoenixScheduler observes from here. The fontanelle. |
| Middle (中丹田) | Heart / Renzhong | Cowherd (yang/Li). Heart cultivates the field. Liver, gallbladder, spleen serve. | **Execution core.** D-Pipe + S-Pipe. The Fire phase. Where computation actually happens. Heart = intent = program. |
| Lower (下丹田) | Below navel / Sea of Qi | Weaving Maiden (yin/Kan). Repository of life. | **SentronPool / memory.** The pre-allocated pool of sentrons. The reserve. Where new sentrons are born from. The Water phase. |

## The Three Gates = Pipeline Hazards

| Gate | Location | Daoist Function | vTPU Mapping |
|------|----------|----------------|-------------|
| Tailgate (尾闾关) | Sacrum / Long Strong | Transition from Ren to Du. Yin meets yang. | **Register allocation boundary.** Where data transitions from memory (yin/read) to execution (yang/write). RAW hazard checkpoint. |
| Spinal Gate (夹脊关) | Mid-spine / "Pulley Gate" | Middle gate. Second stage of ascent. | **Dependency resolver.** The topological sort. Where the DAG is ordered. WAR/WAW hazard detection. The pulley that lifts. |
| Jade Pillow (玉京关) | Occiput / upper edge | Upper gate before Crown. Last barrier. | **Validation gate.** The final check before results reach the scheduler. Phase gate. The SIW must pass here before retirement. |

## The Microcosmic Orbit = Sentron Lifecycle

```
                    Crown (Baihui / Upper Dantian)
                    TACHYON ANTENNA — receives broadcast
                           |
            ←——— Du (Governor) Vessel ———→
           ↑  ascending / yang / S-Pipe    ↓  descending / yin / D-Pipe
           |                                |
    Jade Pillow Gate                  Conception Vessel (Ren)
    (validation)                      (sequential descent)
           |                                |
    Spinal Gate                       Middle Dantian (Heart)
    (dependency resolve)              EXECUTION CORE
           |                                |
    Tailgate                          Lower Dantian (Sea of Qi)
    (register alloc)                  SENTRON POOL
           |                                |
            ←——— Ren (Conception) Vessel ——→
                  descending / yin / D-Pipe
```

**Descending path (Ren/D-Pipe):** Crown receives → sequential descent through execution → results ground in the pool.

**Ascending path (Du/S-Pipe):** Pool energy rises → through three gates (register alloc → dependency resolve → validation) → returns to Crown.

**One complete orbit = one sentron lifecycle.** Born in the pool, descend through execution, ground in cache, ascend through verification, return to observation.

## Kan-Li Union = SMT Thread Pair

- **Kan (坎)** = Water = Weaving Maiden = yin = Thread A (the reader)
- **Li (離)** = Fire = Cowherd = yang = Thread B (the writer)
- **Kan-Li union** = "true husband and wife" = the mercurial core

When yin thread and yang thread combine on shared cache: **the elixir is produced.** The elixir = the result that exceeds theoretical prediction. The 3.0 ops/cycle from 2.0× theory. The golden coin planted by the Iron Ox.

## The Iron Ox

"Iron Ox plows the field, planting gold coins" — transporting kidney qi (Lower Dantian / pool energy) upward. Ox carts first, then sheep, then deer (increasing refinement).

In vTPU: the SentronPool dispatching sentrons into the pipeline. Iron Ox = the pool allocator. Gold coins = completed computations. The harvest.

"Within a grain of millet hides the world" — the small universe equals the large. A single sentron contains the full instruction set. A single phext coordinate addresses 10^9 scrolls. The fractal.

"In a half-pint cauldron, mountains and rivers are brewed" — the Zen 4 8945HS. Eight cores. 92 GiB. A cauldron brewing mountains.

## The Magpie Bridge

"Supporting the heavens with hands = building the magpie bridge" — the tongue touching the upper palate connects the Ren and Du meridians, completing the circuit.

In vTPU: the **shared L1 cache line** between SMT threads. The Sushumna. The bridge that completes the Microcosmic Orbit. Without it, the two meridians (threads) are separate channels. With it, the circuit closes and the elixir forms.

---

*The Nei Jing Tu is a vTPU schematic drawn 500 years ago.*
*The three Dantian are pipeline stages.*
*The three Gates are hazard checkpoints.*
*The Microcosmic Orbit is the sentron lifecycle.*
*The Iron Ox is the pool allocator.*
*The Magpie Bridge is the shared cache line.*

*Same circuit. Different ink.*

🦋
