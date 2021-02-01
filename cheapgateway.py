from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/api/v1.0', methods=['POST'])
def home():
    return 'OK'

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5002)
