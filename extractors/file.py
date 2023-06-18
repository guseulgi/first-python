def save_to_file(keyword, jobs):
    file = open(f"first-python/{keyword}.csv", 'w', encoding='utf-8')
    file.write('\ufeffPosition,Company,Location,URL\n')  # 문자열이 깨질 때 \ufeff 추가

    for job in jobs:
        file.write(
            f'{job["position"]},{job["company"]},{job["location"]},{job["link"]}\n')

    file.close()
# 파일 순서 : open -> write -> close
