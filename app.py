from flask import Flask, render_template
from controllers.books_controller import books_blueprint
app = Flask(__name__)

# TODO: import books blueprint here
app.register_blueprint(books_blueprint)
# TODO: register books blueprint here
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
