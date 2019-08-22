import json
import datetime
import numpy as np
import random
weather_list=["Clear","Cloudy","Rain Shower","Mist","Sunny"]
#{"index":{"_index":"shakespeare","_id":0}
def write_data(filename,data,mod='w'):
    with open(filename,mod) as fp:
        if type(data) == type(list()):
            for idx,da in enumerate(data):
                fp.write(f'{{"index": {{"_index": "weather_index", "_id":{idx}}}}}')
                fp.write("\n"+da+"\n")
my_data=list()
now = datetime.datetime.now()
for i in range(365):
    tmp=dict()
    tmp["temperature"]=np.random.randint(-40,40)
    tmp["weather"]=random.choice(weather_list)
    tmp["date"]=(now-datetime.timedelta(-i-1)).strftime("%Y-%m-%d %I:%M:%S")
    my_data.append(json.dumps(tmp))
write_data(r"./weather.json",my_data)