# python-scripts
🐍 Some pythonic scripts

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

### Usage
```bash
python scripts/broken_urls_detector.py https://agustin-chavez.github.io/ -verbose
```

## 2) Logs Analyzer

Log Analysis Tool filtering and counting the number of errors and warnings

### Usage
```bash
python scripts/logs_analyzer.py resources/today.logs
```

## 3) Web Changes Notifier

Monitors a website to detect changes at regular intervals, every 24 hours by default or every 20 seconds in debug mode

### Usage
```bash
python scripts/web_changes_notifier.py https://github.com/agustin-chavez -t 1
```
