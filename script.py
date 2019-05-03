import math
import sys
from os import rename

import requests

print(sys.executable)


def greet(who):
    return f"Hello {who}!"


re = requests.get("https://coreyms.com")

print(re.status_code)
