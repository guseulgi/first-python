from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

total_pages = 5
onepage_list_count = 10


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
        return 1
    pages = paginations.select('div a')
    count = len(pages)
    if count >= total_pages:
        return total_pages
    else:
        return count


def extract_indeed_jobs(keyword):
    results = []
    pages = get_page_count(keyword)
    for page in range(pages):
        options = Options()
        options.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                   options=options)
        base_url = f'https://kr.indeed.com/jobs?q={keyword}&start={page * onepage_list_count}'
        browser.get(base_url)

        soup = BeautifulSoup(browser.page_source, 'html.parser')
        job_list = soup.find('ul', class_='jobsearch-ResultsList')
        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find('div', class_='mosaic-zone')
            if zone == None:
                anchor = job.select_one('h2 a')
                link = anchor['href']
                title = anchor['aria-label']
                company = job.find('span', class_='companyName')
                location = job.find('div', class_='companyLocation')
                job_data = {
                    'position': title.replace(',', ' '),
                    'company': company.string.replace(',', ' '),
                    'location': location.string.replace(',', ' '),
                    'link': f"https://kr.indeed.com/viewjob?{link}",
                }
                results.append(job_data)
        return results


extract_indeed_jobs('python')
