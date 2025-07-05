from flask import Flask, render_template
import numpy as np
import os

app = Flask(__name__)

# Load the .npy array named 'pred.npy'
npy_path = os.path.join('data', 'pred.npy')
array_data = np.load(npy_path)

@app.route('/')
def index():
    # Show a preview (adjust as needed)
    preview = array_data[:10] if array_data.ndim == 1 else array_data[:5, :5]
    return render_template('index.html', data=preview.tolist())

if __name__ == '__main__':
    app.run(debug=True)
