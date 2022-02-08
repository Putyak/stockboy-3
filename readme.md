Stockboy Refactoring

# Install Package Management

## Install pipenv (if not already installed)
pip install pipenv

## Install npm (if not already installed)
brew install node

## Install npx (if not already installed)
npm install npx

# Boot server
## Navigate to server folder
cd server
## Activeate pipenv
pipenv shell

## installing requirements
pipenv install -r requirements.txt

## Run server
python app.py

### How to Install Python dependencies
pipenv install <package-name>

### How to update requirements file
pipenv lock -r > requirements.txt

# Booting the client (for the first time)
cd client
npm install
npm run dev

