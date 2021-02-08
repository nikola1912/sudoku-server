import boto3
from pathlib import Path


def scan_sudoku_test():
    sudoku_src = Path(__file__).parent / "assets/sudoku.png"
    with open(sudoku_src, 'rb') as image:
        data = image.read()

    client = boto3.client('rekognition')
    response = client.detect_text(Image={'Bytes': data})

    print(response)


if __name__ == '__main__':
    scan_sudoku_test()
