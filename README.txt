This Python program uses Selenium to crawl tax information from the website masothue.com. It iterates through multiple pages of tax listings for Ho Chi Minh City, extracts specific tax details from each listing, and saves the data to a CSV file (data.csv). The program is designed to run with Firefox and includes configurations to run smoothly in a Docker container.

Features:
Web Scraping: Uses Selenium to navigate and extract data from web pages.
Multipage Crawling: Iterates through multiple pages to gather comprehensive data.
Data Extraction: Extracts specific tax information such as tax ID, address, and phone number.
CSV Output: Saves the extracted data to a CSV file for further analysis or processing.
Docker Compatibility: Configured to run in a Docker container with necessary options for Firefox.
Prerequisites:
Python 3.9+
Selenium
Firefox
Geckodriver
Instructions to Run the Code:
1. Install Dependencies:
Make sure you have Python and pip installed. Then, install the required Python packages and Firefox browser.

2. Download and Install Geckodriver:
Download the appropriate version of Geckodriver for your operating system from the Geckodriver releases page. Extract the downloaded file and place the geckodriver executable in a directory included in your system's PATH.

3. Create the Python Script:
Save the provided Python code into a file named main.py.

4. Run the Python Script:
Execute the script using Python.

5. Check the Output:
The extracted tax information will be saved in a file named data.csv in the same directory as the script.

Docker Instructions:
1. Create a Dockerfile:
Create a file named Dockerfile in the same directory as main.py with the following content:

2. Build the Docker Image:
Build the Docker image using the Dockerfile.

3. Run the Docker Container:
Run the Docker container using the built image.

4. Check the Output:
The extracted tax information will be saved in a file named data.csv inside the Docker container. To access this file, you may need to mount a volume or copy the file from the container to your host system.

Example Command to Mount Volume:
This command mounts the current directory to /app inside the container, allowing you to access the data.csv file on your host system.