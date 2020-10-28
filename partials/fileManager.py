import json
import time
from os import listdir,mkdir
from os.path import isfile,join
loc = "./AppData"
try:
    mkdir(loc)
except OSError as error:
    print(error)
def read(id):
    with open(f"{loc}/{id}.note","r") as f:
        return json.loads(f.read())
def write(obj):
    id = time.time()
    obj["_id"] = id
    with open(f"{loc}/{id}.note","w") as f:
        f.write(json.dumps(obj,indent=4))
    return id
def writeById(id,obj):
    with open(f"{loc}/{id}.note","w") as f:
        f.write(json.dumps(obj,indent=4))
def forEach(fn):
    array = [f for f in listdir(loc) if isfile(join(loc,f))]
    for i in array:
        data = read(i.split(".note")[0])
        fn(json.loads(data))
def isFilled():
    array = [f for f in listdir(loc) if isfile(join(loc,f))]
    if len(array)>0:
        return True
    return False
def raw():
    array = [f for f in listdir(loc) if isfile(join(loc,f))]
    empty = []
    for i in array:
        data = read(i.split(".note")[0])
        empty.append(data)
    print(type(empty[0]))
    print(empty)
    return empty
def seed():
    return [{
        "title" : "My Note 1",
        "body" : "This is my Note Body",
        "theme" : "teal"
    },{
        "title" : "My Note 2",
        "body" : "This is my Note Body",
        "theme" : "dodgerblue"
    },{
        "title" : "My Note 3",
        "body" : "This is my Note Body",
        "theme" : "magenta"
    },{
        "title" : "My Note 4",
        "body" : "This is my Note Body",
        "theme" : "tomato"
    },{
        "title" : "My Note 5",
        "body" : "This is my Note Body",
        "theme" : "red"
    }]
def writeUiMode(mode):
    with open(f"Settings/collection.json","w") as f:
        f.write(str(mode))
def readUiMode():
    with open(f"Settings/collection.json") as f:
        if(f.read()=="True"):
            return True
        else:
            return False