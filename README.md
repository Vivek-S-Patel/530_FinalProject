
# Patent Proxy

This website allows users to input a patent abstract and find the two most similar patents from a local database (patents.csv). The similarity is calculated using simple word overlap and vectorization with NumPy, ensuring the app stays lightweight and fast. It is built with Flask, fully containerized with Docker, and designed for easy testing and deployment. No external APIs or heavy libraries are used, making it practical and cost-effective.

## How to run

#### Git Clone Method:

step 1: git clone https://github.com/Vivek-S-Patel/530_FinalProject.git

step 2: cd your-project

step 3: pip install -r requirements.txt

step 4: python app.py

#### Docker Method:
step 1: Download repo as folder titled "proxy"

step 2: docker build -t proxy .

step 3: docker run -p 5000:5000 proxy
