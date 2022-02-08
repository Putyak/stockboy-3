Stockboy Refactoring

#Install pipenv (if not already installed)
pip install pipenv

#Install npm (if not already installed)
brew install node

#Install npx (if not already installed)
npm install npx

#Boot server
cd server
pipenv shell

#install requirements
pipenv install -r requirements.txt

python app.py

#Install dependencies
pipenv install <package-name>

#update requirements file
pipenv lock -r > requirements.txt


#Boot client
cd client
npm install
npm run dev

