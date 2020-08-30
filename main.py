from flask import Flask, request
app = Flask(__name__)


@app.route('/scanner', methods=['POST'])
def scan_sudoku():
    image = request.files['image']
    print(image)
    return {
        "sudoku": []
    }
