# python-scripts
🐍 Some useful python scripts

Create and activate an environment 3.7 or higher:

```bash
python --version
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 1) Broken Urls Detector

It makes HTTP requests for each <a> tag on a site based on its URL and checks the status of each of these hyperlinks.

### Ejemplo de uso
```bash
python scripts/broken_urls_detector.py https://agustin-chavez.github.io/ -verbose
```

## 2) Logs Analyzer

Log Analysis Tool filtering and counting the number of errors and warnings

### Ejemplo de uso

```bash
python scripts/logs_analyzer.py resources/today.logs
```
