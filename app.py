import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from numpy.linalg import norm

# Load patent data from CSV
patents_df = pd.read_csv('patents.csv')

# Function to calculate cosine similarity
def cosine_similarity(text1, text2):
    vector1 = text1.split()
    vector2 = text2.split()
    words = list(set(vector1 + vector2))
    
    vector1_count = np.array([vector1.count(word) for word in words])
    vector2_count = np.array([vector2.count(word) for word in words])
    
    dot_product = np.dot(vector1_count, vector2_count)
    return dot_product / (norm(vector1_count) * norm(vector2_count))

# Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    abstract = request.form['abstract']
    patents_df['similarity'] = patents_df['abstract'].apply(lambda x: cosine_similarity(abstract, x))
    
    # Sort patents based on similarity
    sorted_patents = patents_df.sort_values(by='similarity', ascending=False).head(2)
    
    return render_template('results.html', patents=sorted_patents)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)