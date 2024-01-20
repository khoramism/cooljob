FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script to the container
COPY . /app

# Install dependencies
RUN pip install playwright
RUN playwright install chromium
RUN playwright install-deps
# Run the script
CMD ["python", "/app/crawlers/digikala.py"]
