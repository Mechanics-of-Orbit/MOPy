import json
import random

load_tips = json.load(open("UI_Functions/tips/tips.json"))

no_of_tips = (len(load_tips["LoadTips"]))
print(load_tips["LoadTips"][random.randint(0,no_of_tips-1)])
