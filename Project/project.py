from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

def read_data_from_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/')
def index():
    data_from_scraped_data_csv = read_data_from_csv('scraped_data.csv')
    # Enumerate the data with index starting from 1
    enumerated_data = [(i + 1, row) for i, row in enumerate(data_from_scraped_data_csv[:10])]
    return render_template('index1.html', data=enumerated_data, search_results=[])

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    data_from_scraped_data_csv = read_data_from_csv('scraped_data.csv')
    filtered_data = [row for row in data_from_scraped_data_csv if any(keyword.lower() in str(value).lower() for value in row.values())]
    
    # Ensure search_results is always initialized as an empty list
    search_results = filtered_data if filtered_data else []

    return jsonify(search_results)


if __name__ == '__main__':
    app.run(debug=True)