from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from requests import get as got

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options, service = Service(ChromeDriverManager().install()))

def extract_wwr_jobs(keyword):
    base_url = f"https://www.indeed.com/jobs?q={keyword}&limit=50"
    browser.get(f"{base_url}")
    response = got(f"{base_url}")
    print(browser.page_source)
    if response.status_code != 200:
        print("Can't requeset website")
    else:
        results=[]
        soup = BeautifulSoup(browser.page_source, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_='title')
                job_data = {'link':f"https://weworkremotely.com{link}",
                'company':company.string,
                'region': region.string,
                'position': title.string
                }
                results.append(job_data)
        return results