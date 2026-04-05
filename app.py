from flask import Flask
import os

# Fixed: Added double underscores to __name__
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<body style="background-color: #111; color: red; font-family: monospace;">
    <div class="container" style="text-align: center; margin-top: 50px;">
        <a href="https://github.com/nikhilsainiop" style="text-decoration: none; color: red;">
            <center>
                <br/><br/>
                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄<br/>
                ██░▄▄▄░█░▄▄▀█▄░▄██░▀██░█▄░▄██<br/>
                ██▄▄▄▀▀█░▀▀░██░███░█░█░██░███<br/>
                ██░▀▀▀░█░██░█▀░▀██░██▄░█▀░▀██<br/>
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀<br/>
                <br/><br/>
                <b>Powered By SAINI BOTS</b>
            </center>
        </a>
    </div>
    <br>
    <center>
        <footer style="color: white; margin-top: 50px;">
            <p>© 2026 Video Downloader. All rights reserved.</p>
        </footer>
    </center>
</body>
</html>
"""

# Fixed: Added double underscores and Port binding for Render
if __name__ == "__main__":
    # This part is CRITICAL for Render to detect your app
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
