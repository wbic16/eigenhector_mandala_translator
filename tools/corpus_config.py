import os

def get_base_dir(storage_root=None):
    """
    Returns the base directory for the corpus.
    If storage_root is provided, it is used.
    Otherwise, it defaults to the user's Documents/mystic_corpus directory.
    """
    if storage_root:
        return storage_root
    
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Documents', 'mystic_corpus')
    else:
        return os.path.join(os.path.expanduser('~'), 'Documents', 'mystic_corpus')

def get_registry_path(base_dir=None):
    """
    Returns the path to the corpus registry file.
    If base_dir is not provided, it is determined using get_base_dir().
    """
    if base_dir is None:
        base_dir = get_base_dir()
        
    return os.path.join(base_dir, 'corpus_registry.json')
