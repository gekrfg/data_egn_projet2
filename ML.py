import pandas as pd
import difflib
import time


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


df = pd.read_csv("tweets.csv")

timenow = time.time()
lis = []
for i in range(0, df.shape[0]):
    sim = string_similar("it's so interesting in 24 hours", str(df['text'][i]))
    if sim >= 0.5:
        lis.append(str(df['text'][i]))

print("total use:" + str(time.time() - timenow))
