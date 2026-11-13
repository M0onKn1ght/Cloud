import os
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfiguracja folderu na zdjęcia
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tworzymy folder, jeśli nie istnieje
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Prosty szablon strony HTML wewnątrz kodu, żeby nie tworzyć osobnego pliku templates
HTML_TEMPLATE = '''
<!doctype html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Galeria Zdjęć w Dockerze</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 30px auto; padding: 0 20px; background: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        .upload-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
        .gallery { display: flex; flex-wrap: wrap; gap: 15px; justify-content: center; }
        .photo-card { background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); padding: 10px; width: 200px; text-align: center; }
        .photo-card img { width: 100%; height: 150px; object-fit: cover; border-radius: 4px; }
        input[type="file"] { margin-bottom: 10px; }
        button { background: #007bff; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Moja Galeria Zdjęć (Docker)</h1>
    
    <div class="upload-box">
        <h3>Dodaj nowe zdjęcie</h3>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="photo" accept="image/*" required><br>
            <button type="submit">Prześlij zdjęcie</button>
        </form>
    </div>

    <h3>Wszystkie zdjęcia:</h3>
    <div class="gallery">
        {% if photos %}
            {% for photo in photos %}
                <div class="photo-card">
                    <img src="{{ url_for('uploaded_file', filename=photo) }}" alt="Zdjęcie">
                    <p style="font-size: 12px; word-break: break-all;">{{ photo }}</p>
                </div>
            {% endfor %}
        {% else %}
            <p>Brak zdjęć w galerii. Wgraj pierwsze!</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return redirect(request.url)
        file = request.files['photo']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    
    # Pobieramy listę wgranych zdjęć
    photos = []
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        photos = os.listdir(app.config['UPLOAD_FOLDER'])
        
    return render_template_string(HTML_TEMPLATE, photos=photos)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)