import re
from typing import Dict


class Decoder:
    tokens_ru: Dict[str, str] = {
        "if ": "если ",
        "else ": " инначе ",
        " THEN": " тогда ",
        "writeln ": "записать в новую строку ",
        "+": " плюс ",
        "-": " минус ",
        "*": " умножить ",
        "/": " делить ",
        ":=": " присвоить ",
        "<>": " не равно ",
        ">": " больше ",
        "<": " меньше ",
        ";": "\n",
        "(": "(",
        ")": ")",
    }

    tokens_decoded: Dict[str, str] = {
        "\n": "\n",
        "(": "(",
        ")": ")",
        "если ": " 1 ",
        " инначе ": " 2 ",
        " тогда ": " 3 ",
        "записать в новую строку ": " 4 ",
        " плюс ": " 5 ",
        " минус ": " 6 ",
        " умножить ": " 7 ",
        " делить ": " 8 ",
        " присвоить ": " 9 ",
        " не равно ": " 10 ",
        " больше ": " 11 ",
        " меньше ": " 12 ",
    }

    tokens_numbers = {}
    variables = {}

    def __init__(self) -> None:
        self.code: str = ""

    def decoding(self, code: str) -> str:
        code = "".join(code.split("\n"))
        self.code = code
        self.tokens_numbers = {}
        for number in set(re.findall(r'\d+', self.code)):
            self.tokens_numbers[number] = f"конс. {number}"
        for key, value in {**self.tokens_ru, **self.tokens_numbers}.items():
            self.code = self.code.replace(key, value)
            code = code.replace(f"{key}", " ")
        for variable in list(set(code.split(" "))):
            if variable != "":
                self.variables[variable] = f"переменная {variable}"
        for key, value in self.variables.items():
            self.code = self.code.replace(key, value)

        d = self.code
        for key, value in self.tokens_decoded.items():
            d = d.replace(key, value)
        # print(d)
        return self.code


with open("../temp/code.txt", "r") as file:
    code_file = file.read()

print("/*--------------------------*/")
print(code_file)
decoder = Decoder()
decoded = decoder.decoding(code_file)
print("/*--------------------------*/")
print(decoded)

with open("../temp/decoded code.txt", "w") as file:
    file.write(decoded)