from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

python_jobs = extract_wwr_jobs('python')
print(python_jobs)
