import os
import sys

# Add the application directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'SOURCE CODE', 'Knee Osteoarthritis'))

# Change to the application directory
os.chdir(os.path.join(os.path.dirname(__file__), 'SOURCE CODE', 'Knee Osteoarthritis'))

# Import the Flask app
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
