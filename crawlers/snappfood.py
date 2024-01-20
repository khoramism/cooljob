from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://careers.snappfood.ir') 

    page.wait_for_selector('.job-box', timeout=60000) 
    while True:
        if page.is_visible('#show-more button'):
            page.click('#show-more button')
            page.wait_for_load_state('networkidle')
        else:
            break

    job_listings = page.query_selector_all('.job-box')
    job_details_list = []

    for job in job_listings:
        title = job.query_selector('.job-box-des-title').text_content().strip()
        location = job.query_selector('.job-box-des-info-name').nth(1).text_content().strip()  # Assuming second info-name is location
        department = job.query_selector('.job-box-des-info-name').nth(0).text_content().strip()  # Assuming first info-name is department
        url = job.get_attribute('href')

        job_details = {
            'title': title,
            'location': location,
            'department': department,
            'url': url
        }
        job_details_list.append(job_details)

    browser.close()
    return job_details_list

with sync_playwright() as playwright:
    job_details = run(playwright)
    for job in job_details:
        print(job)
