# 🏏 Cricket Auction Application

This is a web-based Cricket Auction application that allows users to bid for players and manage their team budgets.

## 🔧 Features
- Player listing with base price
- Real-time bidding
- Team budget management
- Admin panel for auction control

## 🛠 Tech Stack
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite / PostgreSQL

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/THPavellpu/Cricket-Auction-Application.git

# Go into the project directory
cd Cricket-Auction-Application

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
