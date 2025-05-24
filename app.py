from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

SONG_FOLDER = os.path.join(os.getcwd(), 'songs')

@app.route('/songs')
def list_songs():
    files = [f for f in os.listdir(SONG_FOLDER) if f.endswith('.mp3')]
    return jsonify(files)

@app.route('/songs/<filename>')
def serve_song(filename):
    return send_from_directory(SONG_FOLDER, filename)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # tu HTML debe llamarse index.html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
