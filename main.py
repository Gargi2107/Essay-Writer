from flask import Flask, jsonify, render_template, request
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 2048 * 2048  



@app.route('/')  # Route for the path '/'
def home():
    return render_template("index.html")

@app.route("/login")  # Route for the path '/login'
def login():
    return render_template("login.html")

@app.route("/signup")  # Route for the path '/signup'
def signup():
    return render_template("signup.html")

@app.route("/about")  # Route for the path '/about'
def about():
    return render_template("about.html")

@app.route("/services")  # Route for the path '/services'
def services():
    return render_template("services.html")

@app.route("/contact")  # Route for the path '/contact'
def contact():
    return render_template("contact.html")


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method=='POST':
        prompt=PromptTemplate.from_template("Generate an Essay on title {title}")
        llm=OpenAI(temperature=0.9)
        chain=LLMChain(llm=llm,prompt=prompt)
        prompt = request.json.get('prompt')
        output=chain.run(prompt)
        if(prompt):
            return output
    return "Please enter the subject!"

@app.route('/generateJoke', methods=['POST'])
def generateJoke():
    if request.method=='POST':
        prompt=PromptTemplate.from_template("Tell me a new good Joke. Never repeat the previous one")
        llm=OpenAI(temperature=0.9)
        chain=LLMChain(llm=llm,prompt=prompt)
        outputJoke=chain.invoke({})
        # print(outputJoke)
        return outputJoke
    return "Internal Service Error!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
