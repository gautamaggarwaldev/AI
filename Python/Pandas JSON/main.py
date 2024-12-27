import pandas as pd

data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'

df = pd.read_json(data)

print(df)

print(pd.read_json(data,orient='records'))
print(pd.read_json(data,orient='index'))
print(pd.read_json(data,orient='columns'))


df = pd.DataFrame([['a','b'],['c','d']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])

print(df)
print(df.to_json())
print(df.to_json(orient='index'))
print(df.to_json(orient='columns'))
print(df.to_json(orient='records'))
print(df.to_json(orient='split'))
print(df.to_json(orient='table'))

schema = '{"schema":{"fields":[{"name":"index","type":"string"},{"name":"col 1","type":"string"},{"name":"col 2","type":"string"}],"primaryKey":["index"],"pandas_version":"1.4.0"},"data":[{"index":"row 1","col 1":"a","col 2":"b"},{"index":"row 2","col 1":"c","col 2":"d"}]}'

print(pd.read_json(schema, orient='table'))

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)

print(df.head())

print(df.to_json(orient='index'))

data = [{"employee_name": "James", "email": "james@gmail.com", "job_profile": {"title1":"Team Lead", "title2":"Sr. Developer"}}]

print(pd.json_normalize(data))


data = [
    {
        "id": 1,
        "name": "Cole Volk",
        "fitness": {"height": 130, "weight": 60},
    },
    {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},
    {
        "id": 2,
        "name": "Faye Raker",
        "fitness": {"height": 130, "weight": 60},
    },
]

print(pd.json_normalize(data))
print(pd.json_normalize(data, max_level=0))
print(pd.json_normalize(data, max_level=1))

data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]

print(pd.json_normalize(data))

print(pd.json_normalize(data, "counties",["state", "shortname",["info",'governor']]))