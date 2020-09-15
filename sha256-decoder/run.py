from main_core import Engine

key = "2f0e3e53406d06f28fe94d24e694b231e165012e682709f609ad3301b03405f6"

eng = Engine(key, "kelime-listesi.txt")


if __name__ == "__main__":
    eng.transform_text_to_hash()
    eng.save_to_pickle_file()
    eng.brute()
