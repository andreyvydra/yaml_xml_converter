import xmlplain
from settings import *


def main(input_filename, output_filename):
    with open(input_filename, "r", encoding="UTF-8") as yaml_file:
        root = xmlplain.obj_from_yaml(yaml_file)
    with open(output_filename, "w", encoding="UTF-8") as xml_file:
        xmlplain.xml_from_obj(root[0], xml_file, pretty=True)


if __name__ == '__main__':
    main(INPUT_FILENAME, OUTPUT_FILENAME)
