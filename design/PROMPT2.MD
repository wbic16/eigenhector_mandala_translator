The goal of this prompt is to run experiments to determine the best combination of tools and techniques for indexing and analyzing the corpus
for use with agents in the Dream Interview Method (DIM). 

Read READ_ME.MD , INDEXING_SYSTEM_DESIGN.MD PROMPT1.MD, CORPUS_STRUCTURE.MD, CORPUS_REGISTRY.MD DIM.MD and NLP_TOOL_RECOMMENDATIONS.MD for context.

We want to have the NLP tools provide the best possible context for the agents to work with.
The corpus is not too large, 10 mystics with 100 docs each in their mandala in the corpus. So we can afford to be a bit more computationally expensive
in our analysis but we probably don't want to use up too many tokens with the subscription based agents people use so we want some ahead of time indexing to nlp tools.

Favor higher recall so the agents have a better chance at finding structural similarity betweeh the two mandalas being projected onto each other.
As a metaphor assume some kind of small graph structure in one mandala is being projected onto another small graph structure on another mandala for explanaing an idea or relationship or process from one mystic to another (usually the user's mandala or my mandala).

You may be as creative as you like for experimenting, the instructions in this document are meant to be starting points for exploring not requirements.

For this run, focus on the indexing of individual mandalas to enable the indexing of an embodied process (perhaps described in sense gate metaphors) or idea or mythic being from one mandala's document to another mandala's document. Some example queries we want to support:

** Example queries **

Please describe Ekajati in sasha's manda in their metaphors into my_mandala, find the most similar being and pull out the martian interview description
and bridging bteween the two beings.

Please extract out the different kinds of beings in eigenhector's mandala and describe them in terms of their sense gate metaphors.

What are the relationships between the different beings in my mandala (my mandala is eigenhector, if you need to modify the bit in corpus_registry go ahead)?

** experimentation environment **

Use C:\Users\hecto\Documents\mystic_corpus as the sample corpus, batch access granted for experimentation.
You can create subdirectories in the folder for testing.
Please use a new python virtual environment for this project so as not pollute the repo.
You can use c:\tmp for scratch space for experimentation, batch access granted for this folder.

Please write experiment results reports\NLP_INDEXING_EXPERIMENTS1.MD for future agents to implement the best strategy for INDEXING_SYSTEM_DESIGN.MD.
Document any potentially useful or missing tools for corpus manipulation and indexing for future implementation.