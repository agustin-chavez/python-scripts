# python-scripts
🐍 Some useful python scripts

Create and activate an environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## 1) Broken Urls Detector

It makes asynchronous HTTP requests for each <a> tag on a site based on its URL and checks the status of each of these hyperlinks.

### Ejemplo de uso
```bash
python3 broken_urls_detector.py https://www.google.com -verbose
```

