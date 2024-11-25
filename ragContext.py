import chromadb
from textContent import *
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt_tab')

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
def create_collection():
    print("Entered")
    chroma = chromadb.PersistentClient(path="chromaStorage/")
    print("+++++++++++++")
    if "ifreenWebsite" not in [c.name for c in chroma.list_collections()]:
        print("Entered")
        # Squish together the entire context
        entireContext = "About Ifreen : " + introduction + " Work Experience : " + company1 + company1_content + company2 + company2_content + company3 + company3_content + " Education : " + school1 + school1_degree + school1_content + school2 + school2_content + school2_degree + " Experiments : " + experiments_title + experiment_name_1 + experiment_content_1 + experiment_name_2 + experiment_content_2 + experiment_name_3 + experiment_content_3 + " Awards : " + award_name_1 + award_content_1 + award_name_2 + award_content_2 + award_name_3 + award_content_3 + award_name_4 + award_content_4 + " Presentations Given : " + presentation_1 + presentation_2 + " Professional certifications taken : " + certification_1_content + certification_2_content + " Courses Undertaken : " + course1_content + course2_content + course3_content + course4_content+". Ifreen Linkedin Profile : https://www.linkedin.com/in/mohamed-ifreen-a60634177/, Ifreen's kaggle profile : https://www.kaggle.com/ifreenibrahim. "+ifreenInfo
        entireContext = nltk.sent_tokenize(entireContext)
        chunkLength = 5
        overlap=1
        documents = []

        # Lets create chunks of documents based on the entire corpus
        for x in range(0,len(entireContext),chunkLength-overlap):
            currentContxt = entireContext[x:x + chunkLength]
            documents.append("->".join(currentContxt))
            print(currentContxt,"+++++++++++++")

        # We have the documents ready
        # Lets add the ids

        ids = list(map(str,list(range(len(documents)))))
        chroma.create_collection("ifreenWebsite")

        currentCollection=chroma.get_collection("ifreenWebsite")
        currentCollection.add(ids=ids[:],documents=documents[:])

    else:
        pass
    return chroma

def get_data(message,client):
    col=client.get_collection("ifreenWebsite")
    return col.query(query_texts=[message],n_results=7)