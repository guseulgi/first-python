# 웹 스크롤러 구현
from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?&term='
search_term = 'python'

# HTML 긁어오기
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print('Cant request website')
else:
    # Beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section', class_='jobs')

    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)  # list 므로
        for post in job_posts:
            print(post)
            print('////')
