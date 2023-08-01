1) LOCAL

python3 -m venv venv
bash
source venv/bin/activate
pip list
pip install -r requirements.txt
pip list


6. Make a copy of the example environment variables file:

cp .env.example .env


7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

OPENAI_API_KEY=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

8. Run the app:

bash
source venv/bin/activate
pip list
flask run


You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).


-----------------------
CLOUD

copia i file:

README.txt
app.py
requirements.txt


