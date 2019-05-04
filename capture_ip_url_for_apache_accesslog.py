# Catch a IP, PATH and URL in Apache Access_log
"""usage
]> python3.7 script_name apache_access.log
regular expressions : https://regex101.com/r/lIHC9G/1
"""
from sys import argv
import re
script, file_name = argv

file = open(file_name, 'r')
lines = file.readlines()

m = re.compile('(?:^[\d]+[.]\d+[.]\d+[.][\d]+)|(?:\s\/.*?\s)|http[s]?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
num = 0
for line in lines:
    ip_path = m.findall(line)
    num = num + 1
    print(f"{num}",ip_path)
file.close()
"""
end of script
"""
