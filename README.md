GUVI Web Application Automation Testing
📌 Project Overview
This project automates the testing of the GUVI EdTech Platform web application using Selenium with Python.
The goal is to validate critical UI functionalities, navigation flows, login/logout features, and accessibility of key elements across multiple browsers.

🎯 Objectives
Automate functional testing of GUVI’s web application.

Validate positive and negative scenarios for login and navigation.

Ensure cross‑browser compatibility (Chrome, Firefox, Edge, Safari).

Generate structured test execution reports.

📚 Scope
URL validation and page title checks.

Visibility and clickability of Login and Sign‑Up buttons.

Navigation to Sign‑Up and Login pages.

Login with valid and invalid credentials.

Verification of menu items (Courses, LIVE Classes, Practice).

Presence of Dobby Guvi Assistant chatbot.

Logout functionality.

🛠 Tech Stack
Language: Python

Framework: Selenium + PyTest

Design Pattern: Page Object Model (POM)

Reporting: PyTest HTML / Allure Reports

📂 Project Structure
Code
guvi_automation/
│
├── pages/              # Page Object classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── signup_page.py
│
├── tests/              # Test cases
│   ├── test_home.py
│   ├── test_login.py
│   └── test_signup.py
│
├── utils/              # Utilities
│   ├── driver_factory.py
│   └── logger.py
│
├── reports/            # Generated reports (upload to Google Drive)
│
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── conftest.py         # PyTest configuration
⚙️ Setup Instructions
Clone the repository:

bash
git clone https://github.com/<your-username>/guvi_automation.git
cd guvi_automation
Install dependencies:

bash
pip install -r requirements.txt
Ensure browser drivers are installed (e.g., ChromeDriver, GeckoDriver).

▶️ Running Tests
Execute all test cases:

bash
pytest --html=reports/report.html --self-contained-html
Run a specific test file:

bash
pytest tests/test_login.py
📑 Test Cases Implemented
Test Case	Scenario	Expected Result
TC1	Verify URL validity	Page loads successfully
TC2	Verify page title	Title matches expected
TC3	Login button visibility & clickability	Navigates to login page
TC4	Sign‑Up button visibility & clickability	Redirects to register page
TC5	Navigation via Sign‑Up	URL loads correctly
TC6	Login with valid credentials	Redirects to dashboard
TC7	Login with invalid credentials	Error message displayed
TC8	Menu items presence	Courses, LIVE Classes, Practice visible
TC9	Dobby Assistant presence	Widget displayed
TC10	Logout functionality	User logged out successfully
