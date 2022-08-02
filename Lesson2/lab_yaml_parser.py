#yaml looks like bullet points
#parses yaml to a dict
import yaml

with open('doe-a-deer.yaml', 'r', newline='') as f:
    try:
        data = yaml.load(f)
        print(data)
       # print(type(yaml.load(f))) #nested dict
    except yaml.YAMLError as ymlexcp:
        print(ymlexcp)

with open('lab_newyamlfile.yaml', 'w') as f:
    yaml.dump(data, f, sort_keys=True) #sorts the keys by alphabetical order