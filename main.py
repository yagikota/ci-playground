from pathlib import Path
import random
import string

if __name__ == "__main__":
    with open("file.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            rand_str = "".join(random.choices(string.ascii_lowercase, k=10))
            Path("migrations/" + line.split("-")[0] +"-"+str(rand_str) + ".sql" ).touch()
