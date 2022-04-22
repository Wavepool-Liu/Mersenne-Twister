import re
import json
a = "[524. 502. 501]"
strinfo = re . compile('. ')
b = json.loads(strinfo.sub(',',a))
print(b[2])