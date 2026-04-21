from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Simple HTML template stored as a string
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<body style="text-align: center; margin-top: 50px;">
    <h2>Login</h2>
    <form action="/auth" method="post">
        <input type="text" name="u" placeholder="Username" required><br><br>
        <input type="password" name="p" placeholder="Password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    # Shows the login page when you access the LB IP
    return render_template_string(HTML_PAGE)

@app.route('/auth', methods=['POST'])
def auth():
    # Accepts ANY username/password and redirects to /login path
    return redirect('/login')

@app.route('/login')
def success():
    return "<h1>Success</h1><p>You have been redirected to the /login path.</p>"

if __name__ == '__main__':
    # Runs on port 80 (Standard HTTP)
    app.run(host='0.0.0.0', port=80)
