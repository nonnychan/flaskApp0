from app import app
 
 
@app.route('/')
def home():
    return "Nonny says 'Hello world!'"
