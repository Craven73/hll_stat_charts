from flask import Flask

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG'] = True

# Import views (route handlers)
from app import routes