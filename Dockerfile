# Verwende das offizielle Python-Basisimage
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Projektinhalt in das Arbeitsverzeichnis
COPY . .

# Setze die Umgebungsvariable für Flask
ENV FLASK_APP=app.py

# Exponiere den Port, auf dem die Anwendung läuft
EXPOSE 5000

# Starte die Flask-Anwendung
CMD ["flask", "run", "--host=0.0.0.0"]
