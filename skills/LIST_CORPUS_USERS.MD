# Listing Corpus Users
 
 This skill describes how to list all registered user aliases available for corpus fetching.
 
 ## Overview
 The `list_users.py` tool reads the `mystic_corpus/corpus_registry.json` file and displays all configured user aliases, their source type, and description.
 
 ## Usage
 
 Run the tool from the command line:
 
 ```bash
 python tools/list_users.py
 ```
 
 ## Expected Output
 
 The tool will output a formatted table of users:
 
 ```text
 ALIAS           TYPE            DESCRIPTION
 ------------------------------------------------------------
 ari             substack        Ari's Substack
 hector          github          Hector's GitHub Repo
 ```
 
 ## Troubleshooting
 
 *   **Registry not found:** Ensure you have created the `mystic_corpus` directory and `corpus_registry.json` file as described in `skills/ADD_CORPUS_USER.MD`.
 *   **No users found:** The registry file exists but is empty. Add users using the instructions in `skills/ADD_CORPUS_USER.MD`.
