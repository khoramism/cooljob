from playwright.sync_api import sync_playwright
from digikala import run_digikala
from tapsi import run_tapsi
from snapp import get_snapp_list
from models.elastic_model import insert_data 

all_job_data = []

all_job_data.append(get_snapp_list())

with sync_playwright() as playwright:
    all_job_data.append(run_digikala(playwright))
    all_job_data.append(run_tapsi(playwright))

for job_companies in all_job_data:
    for job in job_companies:
        print(job)
        insert_data(index_name='cooljob', job_data=job)