from playwright.sync_api import sync_playwright
import json

def get_job_details(browser, job_url):
    # Open a new page in a new context for each job detail
    context = browser.new_context()
    page = context.new_page()
    page.goto(job_url)
    page.wait_for_selector('.elementor-section.elementor-top-section')

    # Extract the details from blocks 3 to 6 (index 2:6)
    detail_text = '\n'
    blocks = page.query_selector_all('.elementor-section.elementor-top-section')
    for block in blocks[2:6]:  # Adjust the indices as necessary
        detail_text += '\n' + str(block.text_content())

    # Close the context after extracting details
    context.close()
    return detail_text.strip()

def run_digikala(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://careers.digikala.com/positions/')
    page.wait_for_selector('div.careers-content')

    jobs = page.query_selector_all('a.career-item')
    page.wait_for_selector('a.career-item')
    
    all_jobs_data = []
    for job in jobs:
        try:
            job_data = {}
            job_data['title'] = job.query_selector('h4.title').text_content()
            job_data['team'] = job.query_selector('span.department').text_content()
            job_data['location'] = job.query_selector('div.location > span').text_content()
            job_data['url'] = job.get_attribute('href')
            job_data['detail'] = get_job_details(browser, job_data['url'])
            job_data['company'] = 'digikala'
            all_jobs_data.append(job_data)
    
        except Exception as e:
            print(f"Error processing job: {str(e)}")
    context.close()
    return all_jobs_data

