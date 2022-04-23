import time
from bs4 import BeautifulSoup
import requests


def find_jobs():
    html_text = requests.get('https://topdev.vn/viec-lam-it/python-kt34').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='box-job')
    for index, job in enumerate(jobs):
        company_name = job.find('p', class_='job-location fl mb-1').text.replace(' ', '')
        position = job.find('h3').text.replace(' ', '')
        more_info = job.h3.a['href']
        with open(f'data/{index}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Tên công ty: {company_name.strip()}")
            f.write(f"Vị trí: {position.strip()}")
            f.write(f"Xem thêm: https://topdev.vn{more_info}")
        print(f'File save: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Watting {time_wait} seconds...')
        time.sleep(time_wait * 1)
