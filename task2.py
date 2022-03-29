import json
from task1 import movie_data
with open("task1.json") as file:
        a=json.load(list,file,indent=4)
def group_by_year(movie):
    b={}
    for i in movie:
        c=[]
        year=i["year"]
        if year not in b:
            for j in movie:
                if year==j["year"]:
                    c.append(j)
                    b[year]=c
            with open("task2.json","w+") as file:
                json.dump(list,file,indent=4)
                d=json.dumps(b)
e=group_by_year(movie_data)
            

        