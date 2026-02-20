The following is a set up guide if you manage multiple
enivornments via conda.

# Clone the repo

```bash
git clone https://github.com/hectorgon/eigenhector_mandala_translator
cd eigenhector_mandala_translator
```

# Conda setup

Here is a way to set up the environment in conda.

```bash
conda create -n mandala_translator python=3.11 uv -c conda-forge
conda activate mandala_translator
uv pip install -r requirements.txt
```

# Prompting the agent to work within the conda environment

Here is a prompt for enabling the agent to work
within the conda environment `mandala_translator`
(tested on Claude Code):

```
In the conda environment mandala_translator, I would like to
use the skill DreamBridge to fetch and compare content from

<site_url1>

and

<site_url2>
```
