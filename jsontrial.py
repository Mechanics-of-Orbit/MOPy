import json
import random

load_tips = json.load(open("UI_Functions/tips/tips.json"))

def fun_fact():
    no_of_tips = (len(load_tips["LoadTips"]))
    return load_tips["LoadTips"][random.randint(0,no_of_tips-1)]

if __name__=='__main__':
    print(fun_fact())
