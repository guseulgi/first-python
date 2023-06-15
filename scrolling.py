from extractors.wwr import extract_wwr_jobs
from extractors.indeed_teaching import extract_indeed_jobs

keyword = input('What do you want to search for?')
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr  # list 끼리 합치기
for job in jobs:
    print(job)
    print('////////////\n////////////')
