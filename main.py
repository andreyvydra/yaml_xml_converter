from settings import *


class Converter:
    def __init__(self, input_filename: str, output_filename: str) -> None:
        self.input_filename = input_filename
        self.output_filename = output_filename

    def convert(self):
        file = open(self.output_filename, "w", encoding="UTF-8")
        file.write(XML_PROLOGUE + "\n" + self.file_converter())

    def file_converter(self):
        all_lines = ["", ]
        cur_index = 1
        space_before_tags = 0
        prev_tag = ""
        for line in open(self.input_filename, encoding="UTF-8"):
            converted_line, space_before_tags, prev_tag, \
            new_row, delay = self.line_converter(line, space_before_tags,
                                                 prev_tag)
            cur_index += delay
            values = converted_line.split(SPLITER_CHARACTER)
            if new_row and cur_index != 2:
                cur_index = len(all_lines) - 1
            if len(values) == 1:
                all_lines.insert(cur_index, values[0])
                cur_index += 1
            elif len(values) == 2:
                open_tag, close_tag = values
                all_lines.insert(cur_index, open_tag)
                all_lines.insert(cur_index + 1, close_tag)
                cur_index += 1
            elif len(values) > 2:
                for idx, item in enumerate(values, 1):
                    all_lines.insert(cur_index + idx, item)
                cur_index += len(values)

        return "\n".join(all_lines)

    def line_converter(self, line: str, spaces_before_tag: int, prev_tag: str) -> (str, int, str, bool, int):
        data = dict()
        data["values"] = line.split(": ")
        data["key"] = data["values"][0]
        data["cleaned_key"] = self.clear_key(data["key"])
        data["counted_spaces"] = self.count_spaces(line)

        if len(data["values"]) == 1:
            xml_line = self.get_empty_xml_tag(data)
            return xml_line, data.get("counted_spaces"), \
                   data.get("cleaned_key"), data.get("key").startswith("-"), \
                   max((spaces_before_tag - data["counted_spaces"]) // 2 - 1, 0)
        else:

            value = data.get("values")[1].replace("\"", "").strip()
            spaces = " " * data.get("counted_spaces")
            xml_line = spaces + f"<{data.get('cleaned_key')}>{value}</{data.get('cleaned_key')}>"

            if self.count_spaces(line) == spaces_before_tag and self.is_dash_here(data.get('key')):
                prev_spaces = " " * (data.get("counted_spaces") - 4)
                xml_line = prev_spaces + f"<{prev_tag}>{SPLITER_CHARACTER}" + xml_line + \
                           spaces + SPLITER_CHARACTER + prev_spaces + f"</{prev_tag}>"

            return xml_line, data.get("counted_spaces"), prev_tag, \
                   False, max((spaces_before_tag - data["counted_spaces"]) // 2 - 1, 0)

    @staticmethod
    def get_empty_xml_tag(data: dict) -> str:
        spaces = " " * data.get("counted_spaces")
        xml_line = spaces + f"<{data.get('cleaned_key')}>{SPLITER_CHARACTER}" + spaces + f"</{data.get('cleaned_key')}>"
        return xml_line

    @staticmethod
    def clear_key(key: str) -> str:
        # Key clearing
        return key.replace("-", "").replace(":", "").strip()

    @staticmethod
    def is_dash_here(key: str) -> bool:
        # Returns true if it finds "-" before the key
        for i in key:
            if i == "-":
                return True
            elif i == " ":
                continue
            return False
        return False

    @staticmethod
    def count_spaces(line: str) -> int:
        # Count all spaces before key
        counter = 0
        while line[counter] == " " or line[counter] == "-":
            counter += 1
        return counter - YAML_DIFFERENCE


if __name__ == '__main__':
    converter = Converter(INPUT_FILENAME, OUTPUT_FILENAME)
    converter.convert()
