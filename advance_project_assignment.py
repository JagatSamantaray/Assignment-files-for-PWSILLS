# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 1. Web Scraping Route
@app.route('/scrape')
def scrape():
    url = 'https://example.com'  # Replace with the actual site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('h2')  # Example tag
    return render_template('scrape.html', data=data)

# 2. API Consumption Route
@app.route('/api_data')
def api_data():
    api_url = 'https://jsonplaceholder.typicode.com/posts'  # Example public API
    response = requests.get(api_url)
    data = response.json()
    return render_template('api_data.html', data=data)

# 3. OAuth2 Authentication (Simplified Example)
@app.route('/login')
def login():
    return redirect('https://accounts.google.com/o/oauth2/auth')  # Redirect to Google OAuth

@app.route('/callback')
def callback():
    # Handle OAuth2 callback
    return 'Logged in successfully!'

# 4. Recommendation System
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        preferences = request.form['preferences']
        recommendations = [f"Recommended item for {preferences}"]  # Placeholder
        return render_template('recommend.html', recommendations=recommendations)
    return render_template('recommend.html')

if __name__ == '__main__':
    app.run(debug=True)

