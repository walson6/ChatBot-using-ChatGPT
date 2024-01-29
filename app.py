from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai

app = Flask(__name__)

def configure():
    load_dotenv()

openai.api_key = os.getenv('secret_key')

def generate_response(prompt):
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return render_template('index.html', user_input=user_input, bot_response=response)

if __name__ == "__main__":
    app.run(debug=True)