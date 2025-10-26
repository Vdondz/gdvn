from flask import Flask, render_template_string, request, flash

app = Flask(__name__)
app.secret_key = 'gia-dinh-viet-key'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
    <style>
        body { font-family: sans-serif; background: #0f172a; color: white; text-align: center; padding-top: 15vh; }
        .btn-light { background: white; color: #0f172a; font-weight: bold; border-radius: 12px; }
        h1 { font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; }
    </style>
</head>
<body data-aos="fade-up">
    <h1>Gia Đình Việt</h1>
    <p data-aos="fade-up" data-aos-delay="200">Website Flask demo trên Vercel</p>
    <a href="https://vercel.com" target="_blank" class="btn btn-light mt-3">Powered by Vercel</a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
    <script>AOS.init();</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, title="Gia Đình Việt")

# ⚠️ Không chạy app.run() trên Vercel
# if __name__ == '__main__':
#     app.run(debug=True)
