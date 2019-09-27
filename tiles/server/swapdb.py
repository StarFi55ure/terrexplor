import json

DBNAME='terrexplor'
DBUSER='terrexplor'
DBPASSWORD='terrexplor'

PROJECT_FILE='themes/terrexplor-main/project-orig.mml'
TARGET_PROJECT_FILE='themes/terrexplor-main/project.mml'

with open(PROJECT_FILE, 'r') as f:
    jsondata = json.loads(f.read())

print jsondata['Layer'][0]['Datasource'].keys()

for layer in jsondata['Layer']:
    if 'Datasource' in layer:
        print layer['Datasource'].keys()
        d = layer['Datasource']
        d['dbname'] = DBNAME
        d['user'] = DBUSER
        d['password'] = DBPASSWORD


with open(TARGET_PROJECT_FILE, 'w') as f:
    f.write(json.dumps(jsondata, indent=4))


