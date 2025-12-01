# Knee Osteoarthritis Prediction System

A Flask-based web application that uses deep learning to predict the severity of knee osteoarthritis from X-ray images.

## Features

- Upload knee X-ray images for analysis
- Automatic classification into 5 severity levels:
  - Normal (Grade 0)
  - Doubtful (Grade 1)
  - Mild (Grade 2)
  - Moderate (Grade 3)
  - Severe (Grade 4)
- User-friendly web interface
- Real-time prediction results

## Requirements

- Python 3.8 (64-bit)
- Visual C++ Redistributable
- See `SOURCE CODE/Knee Osteoarthritis/requirements.txt` for Python dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Novel_Method to_Predict_Knee Osteoarthritis"
```

2. Install Visual C++ Redistributable (if not already installed):
   - Download from: https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0
   - Install: vc_redist.x64.exe

3. Create and activate virtual environment:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
python -m venv knee_oa_env
.\knee_oa_env\Scripts\Activate.ps1
```

4. Install dependencies:
```bash
pip install tensorflow==2.4.0
pip install keras==2.4.2
pip install Flask==2.0.1
pip install Werkzeug==2.2.2
pip install pillow==10.3.0
pip install protobuf==3.20.0
```

## Usage

1. Navigate to the project directory:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
```

2. Activate virtual environment:
```bash
.\knee_oa_env\Scripts\Activate.ps1
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Project Structure

```
├── SOURCE CODE/
│   └── Knee Osteoarthritis/
│       ├── app.py              # Main Flask application
│       ├── knee.h5             # Trained model (not included in repo)
│       ├── requirements.txt    # Python dependencies
│       ├── templates/          # HTML templates
│       ├── static/            # CSS, JS, images
│       ├── model/             # Training data and model
│       └── Test_samples/      # Sample test images
├── REVIEW DOCUMENTS/          # Project documentation
└── SRS/                       # Software Requirements Specification
```

## Note

- The trained model file (`knee.h5`) is not included in this repository due to its size
- You'll need to train the model or obtain it separately
- The application uses legacy Keras compatibility mode for model loading

## License

[Add your license information here]

## Authors

[Add author information here]

## Deployment

### Deploy to Render (Free Hosting)

1. **Sign up at Render**: Go to [render.com](https://render.com) and sign up with your GitHub account

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Knee_Osteoarthritis_Classification`
   - Configure:
     - **Name**: knee-osteoarthritis-classifier (or your choice)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn wsgi:app`
     - **Instance Type**: Free

3. **Deploy**: Click "Create Web Service" and wait for deployment (5-10 minutes)

4. **Get Your Live URL**: After deployment, you'll get a URL like: `https://knee-osteoarthritis-classifier.onrender.com`

### Deploy to Railway (Alternative)

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `Knee_Osteoarthritis_Classification`
5. Railway will auto-detect and deploy
6. Get your live URL from the deployment

### Deploy to Heroku (Alternative)

1. Install Heroku CLI and login: `heroku login`
2. Create new app: `heroku create knee-oa-classifier`
3. Push to Heroku: `git push heroku main`
4. Open app: `heroku open`

**Note**: Make sure the `knee.h5` model file is available in the repository or uploaded separately for predictions to work.
