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

- Python 3.10 (64-bit)
- Visual C++ Redistributable (for Windows)
- See `SOURCE CODE/Knee Osteoarthritis/requirements_deploy.txt` for Python dependencies

## Local Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Knee_Osteoarthritis_Classification
```

2. Install Visual C++ Redistributable (if not already installed, Windows only):
   - Download from: https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0
   - Install: vc_redist.x64.exe

3. Create and activate virtual environment:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Linux/Mac:
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements_deploy.txt
```

5. Add your trained model:
   - Place your trained `knee.h5` model file in the `SOURCE CODE/Knee Osteoarthritis/` directory

## Usage (Local)

1. Navigate to the project directory:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
```

2. Activate virtual environment:
```bash
# On Windows:
.\venv\Scripts\Activate.ps1
# On Linux/Mac:
source venv/bin/activate
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Deployment

### Deploy to Render

1. Fork this repository to your GitHub account
2. Go to [Render](https://render.com) and create a new account or sign in
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - **Root Directory**: `SOURCE CODE/Knee Osteoarthritis`
   - **Build Command**: `pip install -r requirements_deploy.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Add your `knee.h5` model file to the repository (or use external storage)
7. Click "Create Web Service"

### Deploy to Heroku

1. Install Heroku CLI and login
2. Navigate to the source code directory:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
```
3. Create a new Heroku app:
```bash
heroku create your-app-name
```
4. Deploy:
```bash
git subtree push --prefix "SOURCE CODE/Knee Osteoarthritis" heroku main
```

### Deploy to Railway

1. Go to [Railway](https://railway.app) and create an account
2. Click "New Project" and select "Deploy from GitHub repo"
3. Connect your repository
4. Set the root directory to `SOURCE CODE/Knee Osteoarthritis`
5. Railway will automatically detect the Procfile and deploy

### Deploy with Docker

1. Navigate to the source code directory:
```bash
cd "SOURCE CODE/Knee Osteoarthritis"
```

2. Build the Docker image:
```bash
docker build -t knee-osteoarthritis-app .
```

3. Run the container:
```bash
docker run -p 5000:5000 knee-osteoarthritis-app
```

4. Access the application at `http://localhost:5000`

## Project Structure

```
├── SOURCE CODE/
│   └── Knee Osteoarthritis/
│       ├── app.py                  # Main Flask application
│       ├── knee.h5                 # Trained model (required for deployment)
│       ├── requirements_deploy.txt # Python dependencies for deployment
│       ├── Procfile                # Heroku/Railway deployment config
│       ├── render.yaml             # Render deployment config
│       ├── runtime.txt             # Python version specification
│       ├── templates/              # HTML templates
│       ├── static/                 # CSS, JS, images
│       ├── model/                  # Training data and model training code
│       └── Test_samples/           # Sample test images
├── SRS/                            # Software Requirements Specification
└── README.md                       # This file
```

## Important Notes

- **Model File**: The trained model file (`knee.h5`) is required for the application to function. You'll need to:
  - Train the model using the Jupyter notebook in `model/Untitled.ipynb`, OR
  - Obtain a pre-trained model and place it in the `SOURCE CODE/Knee Osteoarthritis/` directory

- **Model Training**: The model uses VGG16 transfer learning architecture and achieves ~95% accuracy on the validation dataset

- The application uses TensorFlow with legacy Keras compatibility mode for model loading
