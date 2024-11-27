Objective:Create an API that allows users to upload images and receive descriptions in various tones (e.g., formal, humorous, and critical).

Setup Instructions

1)Clone the repository:
git clone <repository-url>
cd <repository-folder>

2)Set up a virtual environment:
python3 -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

3)Install the dependencies:
pip install -r requirements.txt

4)Configure the .env file with your API keys:
GPT_API_KEY=<Your GPT/LLM API Key>
DEBUG=True

5)Run the server:
python manage.py runserver

Access the application at http://127.0.0.1:8000.
