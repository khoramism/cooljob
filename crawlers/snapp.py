from bs4 import BeautifulSoup
import requests

site = 'https://career.snapp.ir/'

def get_snapp_list():
    resp = requests.get(site)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    job_list = []
    for job in soup.find_all('a', class_='col-md-6'):
        title = job.find('h5', class_='title').text.strip()
        department = job.find('div', class_='department').text.strip()
        location = job.find('li', class_='location').text.strip()
        url = site[:-1] + job.get('href')
        job_detail = get_detail(url)

        job_dict = {
            'title': title,
            'team': department,
            'location': location,
            'url': url, 
            'detail' : job_detail,
            'company' : 'snapp'
        }
        job_list.append(job_dict)
    return job_list

def get_detail(url: str):
    class_content = 'col-md-9 content'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup.find('div', attrs={'class' : class_content}).text

