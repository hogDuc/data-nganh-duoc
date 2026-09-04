import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DRUG_TYPES_TEMPLATE = os.getenv("DRUG_TYPES_TEMPLATE")