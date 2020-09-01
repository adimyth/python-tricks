"""
Text files are collection of bytes. Character encoding is a look up table that provides a mapping from bytes to characters.
Each file can be stored & read from using different encodings.
Default in python is UTF-8. Using different encoding to write or read a file gives garbled text.

# encode -> str to bytes
# decode -> bytes to str
"""
from typing import BinaryIO, TextIO

import chardet

with open("text-files/sample.txt", encoding="ISO-8859-1") as f:  # type: TextIO
    s = f.read()
print(f"Type: {type(s)}\nContent: {s}")

"""
We can also use `chardet` python package to detect the type of encoding.
It is not 100% guranteed to give accurate result but makes a good guess in general
"""

with open("text-files/sample.txt", "rb") as file:  # type: BinaryIO
    raw_data = file.read()
result = chardet.detect(raw_data)
charenc = result["encoding"]

print(f"Result: {result}\nEncoding: {charenc}")
