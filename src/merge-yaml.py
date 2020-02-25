'''
  merge yaml file
'''
import argparse
import yaml

parser = argparse.ArgumentParser(description='merge yaml file')
parser.add_argument('base', metavar='base', type=str, help='base yaml file')
parser.add_argument('diff', metavar='diff', type=str, help='diff yaml file')

args = parser.parse_args()


def load_yaml(file_name: str):
    with open(file_name) as file:
        return yaml.load(file.read())


def merge(base_dict: dict, diff_dict: dict):
    result = dict()
    base = set(base_dict.keys())
    diff = set(diff_dict.keys())

    for key in base - diff:
        result[key] = base_dict[key]

    for key in diff - base:
        result[key] = diff_dict[key]

    for key in base & diff:
        v1 = base_dict[key]
        v2 = diff_dict[key]
        if isinstance(v1, dict) and isinstance(v2, dict):
            value = merge(v1, v2)
        else:
            value = v2
        result[key] = value

    return result


base, diff = map(load_yaml, [args.base, args.diff])

result = yaml.dump(merge(base, diff))

print(result)
