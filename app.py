from flask import Flask, request, redirect, render_template_string
from datetime import datetime

app = Flask(__name__)
messages = []

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>簡易留言板</title>
</head>
<body>
    <h1>簡易留言板</h1>
    <form method="post">
        <p>
            <label>暱稱：<input name="name" required></label>
        </p>
        <p>
            <label>留言：<br>
            <textarea name="msg" rows="4" cols="40" required></textarea></label>
        </p>
        <p><button type="submit">送出</button></p>
    </form>
    <hr>
    <h2>留言列表：</h2>
    {% for m in messages %}
        <p><strong>{{ m.name }}</strong> 說：</p>
        <blockquote>{{ m.msg }}</blockquote>
        <p style="font-size: 0.9em; color: gray;">{{ m.time }}</p>
        <hr>
    {% endfor %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        msg = request.form.get('msg', '').strip()
        if name and msg:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            messages.append({'name': name, 'msg': msg, 'time': timestamp})
        return redirect('/')
    return render_template_string(HTML_TEMPLATE, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
