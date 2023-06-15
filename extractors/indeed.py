# from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def extract_indeed_jobs(keyword):
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options)
    base_url = f'https://kr.indeed.com/jobs?q={keyword}'
    browser.get(base_url)

    results = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    jobs = soup.find_all('ul', class_='jobsearch-ResultsList')
    for job in jobs:
        contents = job.find_all('td', class_='resultContent')
        for content in contents:
            infos = content.find_all('span')
            anchor = content.find('a')
            link = anchor['href']
            title = infos[0]
            company = infos[1]
            job_info = {
                'title': title.string,
                'company': company.string,
                'link': f"https://kr.indeed.com/viewjob?{link}",
            }
            print(job_info)
            results.append(job_info)
            print('///////////')


extract_indeed_jobs('python')
