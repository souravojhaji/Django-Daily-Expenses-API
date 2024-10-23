# Daily Expenses Sharing Application

## Setup Instructions

1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Run the server: `python manage.py runserver`
5. API endpoints:
    - `/user/`: Create a new user
    - `/expense/`: Add an expense
    - `/user/<id>/expenses/`: Retrieve user expenses
    - `/download_balance_sheet/<id>/`: Download balance sheet
