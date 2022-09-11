from requests import get
import selenium
from bs4 import BeautifulSoup

from extractors.wwr import extract_wwr_jobs

jobs=extract_wwr_jobs("python")
print(jobs)
