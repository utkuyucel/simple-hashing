import pickle
from hash_core import Transform
from tqdm import tqdm

class Engine:

    def __init__(self, key, wordlist):
        self.key = key
        self.wordlist = wordlist
        self.all = {} #Hashes
        self.encrypted = None

    def __len__(self):
        if (len(self.all) == 0):
            print("Dictionary not created yet.")
            return 0
        else:
            return len(self.all)

    def transform_text_to_hash(self):

        with open(self.wordlist, "r+", encoding = "utf-8") as f:
            x = f.read().split("\n")
            for i in x:
                tfm = Transform(i).hashTo256()
                self.all.update({i: tfm})
        
        print("Text file transformed to hash.")
    
    def save_to_pickle_file(self):
        with open("all.pkl", "wb") as f:
            pickle.dump(self.all, f)
        
        print("Saved to pickle file.")

    def load_from_pickle_file(self):
        with open("all.pkl", "rb") as f:
            pickle.load(f)
    
    def brute(self):
        for i in tqdm(self.all):
            if (self.key == self.all[i]):
                self.encrypted = i
        print("\n") 
        print("SHA256 Encrypted: ", self.key)
        print("Decrypted: ",self.encrypted)

                    



