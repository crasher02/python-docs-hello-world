from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Hackerman! This is your Pre-Production Environment"

from datetime import datetime
import pytz

def main():
    # Display "Hello World!"
    print("Hello World!")
    
    # Get the current date and time in Zurich
    tz_zurich = pytz.timezone('Europe/Zurich')
    zurich_time = datetime.now(tz_zurich)
    
    # Format the date and time as a string
    zurich_time_str = zurich_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Display the date and time
    print(f"Current date and time in Zurich: {zurich_time_str}")

if __name__ == "__main__":
    main()
