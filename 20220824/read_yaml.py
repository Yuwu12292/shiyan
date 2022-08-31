import yaml
def read_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    string = file.read()
    args = yaml.safe_load(string)
    return args