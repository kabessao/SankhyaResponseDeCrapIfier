#!/bin/python3
import json
import sys
import os
import inspect


def parse(response: str, filter_empty_values = False, filter_customized_fields = True):
    jsontext = json.loads(response)

    try:
        root = jsontext["responseBody"]["entities"]
    except Exception: 
        return []

    fields = root["metadata"]["fields"]["field"]

    if "entity" not in root:
        return []

    entities = root["entity"]

    names = list()

    for item in fields:
        names.append(item["name"])

    lista = list()

    def sort(entity):
        sorted_values = dict()
        for i in range(len(names)):
            value = entity["f"+str(i)]
            value = value["$"] if len(value) > 0 else ""

            if filter_empty_values and (not value or str(value) == "0"):
                continue

            if (filter_customized_fields and names[i].startswith("AD_")):
                continue

            sorted_values[names[i]] = value

        lista.append(sorted_values)

    if isinstance(entities, list):
        for entity in entities:
            sort(entity)
    else:
        sort(entities)

    return lista


def io_write(text, file_name = "output"):

    open(f"./{file_name}.json", "+w").write(text)


if __name__ == "__main__":

    input_file = None
    output_file = None

    arguments = {
        "filter_empty_values" : False,
        "filter_customized_fields" : False,
    }

    for arg in sys.argv[1:]:

        if not input_file and not arg.startswith('-') and os.path.isfile(arg):
            input_file = arg
            continue

        if not output_file and not arg.startswith('-') and os.path.isfile(arg):
            output_file = arg
            continue

        if not arg.startswith("--"):
            print(f"No recognized parameter {arg}", file=sys.stderr)
            quit(1)

        arg = arg[2:]

        value = not arg.startswith("no-")

        if not value:
            arg = arg[3:]

        arg = arg.replace("-",'_')

        if arg in arguments:
            arguments[arg] = value

    if not input_file:
        print("No input file informed", file=sys.stderr)
        quit(1)

    with open(input_file, "r", encoding="iso-8859-1") as file:

        text = file.read()

        result = parse(text, **arguments)

        text = json.dumps(result, indent=4)

        if not text:
            print("There were no items in this json", file=sys.stderr)
            quit(1)

        if output_file:
            io_write(text, output_file) 

            print("done!")
            quit(0)

        print(text)
