# -*- coding: utf-8 -*-

import pandas as pd
import json

df =  pd.read_json("data/arxiv-metadata-oai-snapshot.json", lines=True)
names = {}

with open("data/categories.json",'r') as f:
    cat_names = json.load(f)
    for obj in cat_names:
        names[obj["tag"]] = obj["name"]
        

df.categories.map(names)
