from flask import Flask, abort, response
import subprocess


app = Flask(__name__)
app.config.from_envvar("WEBHOOK_RECEIVER_SETTINGS", silent=True)
app.config.from_pyfile("/etc/webhook-receiver.settings.py", silent=True)
app.config.from_pyfile("webhook-receiver.settings.py", silent=True)


@app.route("/hook/<project>", methods=["POST"])
def hook(project):
    if project not in app.config['COMMANDS']:
        return abort(404)
    rc = subprocess.wait(app.config['COMMANDS'][project])
    return response.ok() if rc == 0 else abort(500)
