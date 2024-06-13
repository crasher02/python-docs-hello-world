from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def hello():
    # Get the current date and time in Zurich
    tz_zurich = pytz.timezone('Europe/Zurich')
    zurich_time = datetime.now(tz_zurich)
    
    # Format the date and time as a string
    zurich_time_str = zurich_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Return the message with the current date and time
    return f"Hello, Hackerman! This is your Pre-Production Environment. Current date and time in Zurich: {zurich_time_str}"

if __name__ == "__main__":
    app.run(debug=True)
