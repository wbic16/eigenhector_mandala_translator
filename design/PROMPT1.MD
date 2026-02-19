Please read README.MD for the overall vision. Read DIM.MD for the definition of a martian interviewer.

The goal is to create a storage system to store fetched or imported documents into a document store for fast retrieval by agents. The documents are organized into mandalas, which are collections of documents organized by user.

consider easy use on windows, mac and linux.

look at C:\Users\hecto\Documents\mystic_corpus for an existing sample of data. You can propose a new way of oranizing the data in a database or file structure in the new design.
use c:\tmp for test output location

Users are mystics who want to analyze their mandala (composed of a corpus of documents in the mystic_corpus) and see what various objects in other peoples mandalas look like.
A mandala is a collection of documents in a corpus organized by user.

We want a user database with at least a short name, e.g. ari, the corpus that was downloaded, the source type (e.g. substack, github, etc) and the url of the source. We want a special alias called "my mandala" to refer to the user's own writings, prompt the user when they are running the tools for the first time their short name and substack location and add an extra reference so they can refer to their own writings as my mandala.

We want to be able to support corpus indexing such as:

sense gate extraction - for each document fetched see what major sense gates are mentioned (sight, touch, sound, smell, taste, proprioception, interoception, etc,) make sure there is easy way for agents to be able to look at a corpus and answer user questions like what smells like what i call rose in my mandala with something in eliade's mandala. display similar smells in eliade's mandala and eigenhector's mandala. support synesthesia between all sense gates. for example if a user asks for something "red sharp and friendly" the indexing should support returning "the red rose was thorny but beautiful", "hayagriva smiled at me with his friendly red face and fanged grin" and "papa smurf's peaked cap hid his eyes but not his friendly smile" in the appropriate manadalas.

mythic being extraction - for each document fetched see what beings in their mandala are referred to for the martian interviewer to refer to. they do not have to be major known beings but may be custom beings for example eigenhector's energon starbird is a custom mythic being. some mythic beings come from standard literature and can be buddhist or hindu figures or from any other pantheon like greek or dmt or ufo. A corpus might contain a mix of beings from different pantheons even in one document. do not assume they refer to the same being even though they might have the same name. for example vajrayana's hayagriva is different from the hindu hayagriva and is different from the mystics's mandala version of hayagriva. always assume that the mystic's mandala mythic being name is just a name and the being is described by the characteristics and actions in the mystic's mandala alone. extract out the appropriate fields during indexing for the martial interviewer.

design the user and mandala / corpus database with the knowledge that we want to do as much ahead of time indexing as possible for pairwise mandala to mandala searching.

for example one skill might be does this mythic being from ari exist in eigenhector's mandala using the characteristics of the mythic being as described in each mystic's mandala.

another possible skill we want to develop is how best for ari and eigenhector to collaborate. see ARI_DREAM_BRIDGE_TEMPLATE.MD support this kind of use case.

make it easy to expand indexing in the future. for example we have the sense gate index and the mythic being index. these indices should be easy for ai agents to use.

because we want to quickly look up documents for mythic beings in one mystic's mandala to another make sure that this indexing is easy for a martian interviewer to then compare two documents a possible match has come from, for example sasha's ekajati with eigenhector's cernnuous. the user might want to compare these beings side by side.

check out docetl and docwrangler to see if it’s useful for these things
see if nlp tools like nltk are helpful considering that the martian interviewer goes by descriptions rather than name of the mythic beings and dream objects

Break down into a series of design documents and create them in design