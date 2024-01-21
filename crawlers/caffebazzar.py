

from bs4 import BeautifulSoup
import requests

site = 'https://careers.cafebazaar.ir/#/jobs'

from playwright.sync_api import sync_playwright

def get_job_details(browser, job_url):
    # Open a new page in a new context for each job detail
    context = browser.new_context()
    page = context.new_page()
    # print(job_url)
    page.goto(job_url)
    job_details = {}

    # Wait for the main job title to load as an indicator that the page has loaded
    # page.wait_for_selector('div.Layout d-flex fd-col bc-gray1')

    # Extract job details
    # job_details['location'] = page.query_selector('div.JobItem__header span.fc-gray7.fs-md').inner_text()
    # job_details['department'] = page.query_selector('div.JobItem__header span.fc-gray7.fs-md:nth-child(3)').inner_text()
    # job_details['employment_type'] = page.query_selector('div.JobItem__header span.fc-gray7.fs-md:nth-child(5)').inner_text()
    # job_details['title'] = page.query_selector('div.JobItem__header h1.fs-3xl.fw-md').inner_text()
    
    # Job Description
    job_description_elements = page.query_selector_all('div.JobItem__description p')
    job_details['description'] = ' '.join([elem.inner_text() for elem in job_description_elements if elem.inner_text().strip()])

    # Requirements
    job_requirements_elements = page.query_selector_all('div.JobItem__description:nth-child(2) ul li')
    job_details['requirements'] = ' '.join([elem.inner_text() for elem in job_requirements_elements if elem.inner_text().strip()])

    # Benefits
    job_benefits_elements = page.query_selector_all('div.JobItem__description:nth-child(3) ul li')
    job_details['benefits'] = ' '.join([elem.inner_text() for elem in job_benefits_elements if elem.inner_text().strip()])

    # Application Link
    apply_link = page.query_selector('a.JobItem__MainResumeButton')
    job_details['apply_link'] = apply_link.get_attribute('href') if apply_link else None


    detail_text =  job_details['description'] + '\n' + job_details['requirements'] + '\n' + job_details['benefits'] + '\n'
    context.close()
    return detail_text


def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(site) 
    # page.wait_for_selector('div.mrl-auto mrr-auto')
    job_selector = 'div[data-v-b362b9ae] > a'
    page.wait_for_selector(job_selector)
    job_elements = page.query_selector_all(job_selector)
    job_listings = []

    for job_element in job_elements:
        title = job_element.query_selector('div.fs-lg.fc-gray9.mrb-sm').text_content()
        department_and_location = job_element.query_selector_all('div.fs-sm.fw-lo.fc-gray7.f-grow')
        department = department_and_location[0].text_content() if len(department_and_location) > 0 else None
        location = department_and_location[1].text_content() if len(department_and_location) > 1 else None
        url = job_element.get_attribute('href')
        
        full_url = '/'.join(site.split('/')[:-1]) + url.strip()[1:] 
        
        detail_text = get_job_details(browser, full_url) 
        print(detail_text)
        job_listings.append({
            'title': title.strip() if title else None,
            'department': department.strip() if department else None,
            'location': location.strip() if location else None,
            'url': full_url if full_url else None
        })

    return job_listings

with sync_playwright() as playwright:
    job_details = run(playwright)
    for job in job_details:
        print(job)
