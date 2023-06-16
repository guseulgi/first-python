from extractors.wwr import extract_wwr_jobs
from extractors.indeed_teaching import extract_indeed_jobs
from extractors.file import save_to_file

keyword = input('What do you want to search for?')

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
save_to_file(keyword, indeed+wwr)
