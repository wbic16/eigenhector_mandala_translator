This meta-prompt creates a skill called `HERO_CHARACTER_SHEET.MD` that generates detailed RPG-style character sheets for beings identified in the user's mandala.

### Intent & System
The goal is to translate beings from the "Magitech Survey" into fully realized "Heroes" using the system from "He Who Fights with Monsters" (HWFWM).

1. **Research Basis**:
   - Ranks: https://he-who-fights-with-monsters.fandom.com/wiki/Ranks (Normal through Transcendent).
   - Essences: https://he-who-fights-with-monsters.fandom.com/wiki/Essences (3 Essences + 1 Confluence).
   - Attributes: https://he-who-fights-with-monsters.fandom.com/wiki/Attributes (Power, Speed, Spirit, Recovery).

2. **The Martian Interviewer**:
   - Use the **Martian Interviewer** persona from `skills/DreamBridge/DIM.MD` to investigate the hero's soul.
   - The Interviewer should ask: "Why do you have these four 'pillars' (attributes) and four 'flavor-souls' (essences)?"
   - Justify the choice of Essences and Confluence based on the being's findings in `reports/MAGITECH_BEINGS_SURVEY.MD`.

3. **Team Composition & Balanced Archetypes**:
   Establish a balanced team of four heroes for each mandala or realm expedition. Each hero must fill one of the following roles:
   - **Healer**: High Spirit/Recovery. Focuses on life-preserving magic and utility.
   - **Researcher**: The intellectual core. Model after **Clive Standish** (analytical, ritual magic, complex confluences like Karmic Power) or **Travis Noble** (magitech engineering, practical tool-driven solutions). High Spirit and Wordcel logic.
   - **Defender**: High Power/Speed. Focuses on protection, crowd control, and durability.
   - **Balancer**: The bridge between spheres. Focuses on versatility, dualities (Soul/Vessel), and filling gaps. High proficiency in "Bridging" and "Resonance".

4. **Character Sheet Components**:
   - **Role**: [Healer/Researcher/Defender/Balancer]
   - **Soul Rank**: Assign one of the 7 Ranks (Iron, Bronze, Silver, Gold, etc.).
   - **Essence Triad**: Define 3 Essences and a resulting Confluence. (For Researchers, consider 'Rune', 'Magic', 'Technology', 'Balance').
   - **Attributes (4x10 system)**: Rate Power, Speed, Spirit, and Recovery.
   - **Abilities**: List 5 unique abilities for each essence/confluence.
   - **Vibe Aura**: Describe the magical aura.
   - **Magitech Equipment**: Categorize as "Soul-Bound" or "Utility".

5. **Mandala Alignment**:
   - Every Hero is a past life or a faceted reflection of the **Avatar of Goodness, Truth, and Beauty**.
   - Show how this specific configuration of Essences and Attributes contributes to the Avatar's final development.

6. **Visuals**:
   - Generate an image prompt for the Hero in their "Peak Combat State," emphasizing the Magitech blend.

7. **Output**:
   - The skill should append character sheets to `reports/HERO_ROSTER.MD`.
