import os

from dotenv import load_dotenv
from multion.client import MultiOn

load_dotenv()
MULTION_API_KEY = os.environ.get('MULTION_API_KEY')
multion = MultiOn(api_key=MULTION_API_KEY)

while True:
    cmd = input("What help do you need?:\n")
    if cmd in ('quit','exit'):
        break
    else:
        browse = multion.browse(
        cmd=cmd,
        url="https://python.langchain.com/v0.2/docs/tutorials/")


        print("Answer :", browse.message)
        print("Source url :", browse.url)
        print("Metadata :", browse.metadata)
        print("Status :", browse.status)


# print("model_config :", browse.model_config)
# print("model_fields :", browse.model_fields)