from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-dev-shm-usage")

options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

browser = webdriver.Chrome(options=options, service = Service(ChromeDriverManager().install()))

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
browser.implicitly_wait(3)
browser.get_screenshot_as_file('indeed_test.png')

soup = BeautifulSoup(browser.page_source, "html.parser")
jobs = soup.find_all('td', class_="resultContent")

results=[]
for job in jobs:
    job_title = job.select_one("h2 a")
    results.append(job_title['aria-label'])


for result in results:
    print(result[16:])
    print("///////////////////////////")
browser.quit()