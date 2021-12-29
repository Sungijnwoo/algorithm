import re

a = "hi123h"

m = re.finditer('h?', a)

for i in m:
    print(i.start())