# The News Hub

## Overview
**The News Hub** is a news aggregator that allows users to segregate news based on newspapers such as CNN, Associated Press (AP), Times of India (TOI), Hindustan Times (HT), BBC, and The New York Times (NYT). It provides a simple interface to select a news source and displays all the latest headlines. The application also includes a light and dark theme for better user experience.

## Features
- **News Source Selection**: Users can select their preferred news source from available options.
- **Headline Display**: Fetches and displays the latest headlines based on the selected news source.
- **Theme Support**: Users can toggle between light and dark themes for a comfortable reading experience.

## Technologies Used
- **Flask**: Backend framework for handling requests and serving content.
- **Beautiful Soup**: Used for web scraping to extract news headlines.
- **Fake UserAgent**: Helps in bypassing restrictions by generating random user agents to prevent blocking by news websites.

## Installation & Setup

### Prerequisites
Ensure you have **Python 3.7+** installed.

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/The-News-Hub.git
   cd The-News-Hub
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Open your browser and navigate to:
   ```sh
   http://127.0.0.1:5000
   ```

## Usage
1. Select a news source from the available options.
2. The latest headlines from the selected source will be displayed.
3. Toggle between light and dark themes for better readability.


## Contributing
If you wish to contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Open a pull request.


