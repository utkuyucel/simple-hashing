import hashlib

class Transform:

    def __init__(self, inp):
        self.inp = inp.encode(encoding = "utf-8")
        self.sha256 = hashlib.sha256(self.inp).hexdigest()
    
    def hashTo256(self):
        return self.sha256


if __name__ == "__main__":
    text = input("Text to be encrypted: ")
    tfm = Transform(text)
    x = tfm.hashTo256()
    print("Text:", text, "\nEncrypted: ", x)
