import json
import uuid
import numpy as np
import time
#{"index":{"_index":"shakespeare","_id":0}
def write_data(filename,data,mod='w'):
    with open(filename,mod) as fp:
        if type(data) == type(list()):
            for idx,da in enumerate(data):
                fp.write(f'{{"index": {{"_index": "uuid_index", "_id":{idx}}}}}')
                fp.write("\n"+da+"\n")

np.random.seed(int(time.time()))
res=np.random.normal(1,3,100000)
my_data=list()
for i in range(100000):
    tmp=dict()
    tmp["uuid"]=str(uuid.uuid1())
    tmp["line"]=i
    tmp["data"]=res[i]
    my_data.append(json.dumps(tmp))
write_data(r"./uuid.json",my_data)