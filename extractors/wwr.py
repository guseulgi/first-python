from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(search_term):
    base_url = 'https://weworkremotely.com/remote-jobs/search?&term='

    # HTML 긁어오기
    response = get(f"{base_url}{search_term}")
    if response.status_code != 200:
        print('Cant request website')
    else:
        results = []
        # Beautifulsoup
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_='jobs')

        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)  # find_all 은 list 를 리턴
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, location = anchor.find_all(
                    'span', class_='company')
                title = anchor.find('span', class_='title')
                job_data = {
                    'position': title.string.replace(',', ' '),
                    'company': company.string.replace(',', ' '),
                    'location': location.string.replace(',', ' '),
                    'link': f"http://weworkremotely.com{link}",
                }
                results.append(job_data)
    return results
