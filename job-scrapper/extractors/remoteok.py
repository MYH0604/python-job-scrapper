from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code != 200:
        print("Can't get jobs.")
    else:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all('td', class_="company")
        jobs.pop(0)
        results = []
        for job in jobs:
            company = job.find("h3")
            company = company.string[1:].replace(","," ")
            anchor = job.find("a")
            link = f"https://remoteok.com/{anchor['href']}"
            title = job.find('h2')
            title = title.string[1:-1].replace(","," ")
            condition = job.find("div")
            condition = condition.string.replace(","," ")
            if condition[2] == "$":
                region = None
            else:
                region = condition
            job_data = {'company':company,'position':title,'region':region, 'link':link}
            results.append(job_data)
        return results
