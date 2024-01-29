
# CoolJob

## Iran Tech Job Market Explorer

### Introduction

Welcome to the Iran Tech Job Market Explorer - a comprehensive platform aimed at transforming the way job seekers explore opportunities in Iran's thriving tech sector. Combining the robustness of Go (Fiber) for API development and the agility of Python for web crawling, our platform aggregates job postings from top high-tech companies in Iran, indexing them into Elasticsearch. This fusion creates a centralized, searchable database for tech job opportunities.

### Technologies

- **Go (Fiber):** Efficient, scalable API development.
- **Python:** Advanced web crawling and data extraction.
- **Elasticsearch:** Robust search and analytics engine.
- **Docker:** Containerization of application components.
- **Swagger:** Detailed API documentation.
- **Vue.js & Vuetify:** Frontend development for a responsive and interactive user interface.


### Installation and Setup

1. Clone the repository:
   ```shell
   git clone https://github.com/khoramism/cooljob
   ```
2. Navigate to the project directory:
   ```shell
   cd cooljob
   ```
3. Execute the build script (requires Docker):
   ```shell
   ./build.sh
   ```

### API Documentation

Our API is thoroughly documented using Swagger. Here's a glimpse of what you can do:

- **Get Job Posts by Title:** `/v1/jobs/{title}`
  
  Fetches job postings based on the specified title. For detailed API usage, refer to our `swagger.yaml`.

### Usage

- **API Endpoints:** Interact with our API as per the documentation in `swagger.yaml`.
- **Crawlers:** Execute Python crawlers to fetch the latest job postings from sources like Tapsi, Snapp, and Digikala.
- **Elasticsearch:** Utilize Elasticsearch for querying and analyzing job data.

### Web Interface

Access our platform at [cooljob.ir](https://cooljob.ir) for a user-friendly experience, developed using Vue.js and Vuetify.

### Repositories

- Backend Repo: [khoramism/cooljob](https://github.com/khoramism/cooljob)
- Frontend Repo: [khoramism/cooljob_frontend](https://github.com/khoramism/cooljob_frontend)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

A special thanks to the Iranian tech community for their continuous support and invaluable feedback.
