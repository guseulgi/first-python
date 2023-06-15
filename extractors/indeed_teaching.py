from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options)
    base_url = f'https://kr.indeed.com/jobs?q={keyword}'
    browser.get(base_url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    paginations = soup.find('nav', attrs={'aria-label': 'pagination'})
    if paginations == None:
        return
    pages = paginations.select('div a')
    print(len(pages))


def extract_indeed_jobs(keyword):
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options)
    base_url = f'https://kr.indeed.com/jobs?q={keyword}'
    browser.get(base_url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    job_list = soup.find('ul', class_='jobsearch-ResultsList')
    jobs = job_list.find_all('li', recursive=False)
    results = []
    for job in jobs:
        zone = job.find('div', class_='mosaic-zone')
        if zone == None:
            anchor = job.select_one('h2 a')
            link = anchor['href']
            title = anchor['aria-label']
            company = job.find('span', class_='companyName')
            location = job.find('div', class_='companyLocation')
            job_data = {
                'link': f"https://kr.indeed.com/viewjob?{link}",
                'company': company.string,
                'location': location.string,
                'position': title,
            }
            results.append(job_data)
    for result in results:
        print(result)
        print('/////')
    return results


# extract_indeed_jobs('python')
get_page_count('python')
