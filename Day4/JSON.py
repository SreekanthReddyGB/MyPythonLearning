#JSON...

"""
import json
print(json.dumps({"name":"max", "age":22}))
print(json.dumps(["1","2"]))
print(json.dumps(("1","2")))
print(json.dumps("Hello World"))
print(json.dumps(100))
print(json.dumps(None))
"""

import json
a=json.dumps({"name":"max", "age":22})
print(type(a))

b=json.loads(a)
print(type(b))
