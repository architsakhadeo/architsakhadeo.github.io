
from flask import Flask, request, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
	return str(random.randint(1,106))

if __name__ == "__main__":
	app.run()
