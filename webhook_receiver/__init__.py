from flask import Flask, abort, Response
import subprocess


app = Flask(__name__)
app.config.from_pyfile("/etc/webhook-receiver.settings.py", silent=True)
app.config.from_pyfile("webhook-receiver.settings.py", silent=True)
app.config.from_envvar("WEBHOOK_RECEIVER_SETTINGS", silent=True)

for project, command in app.config['COMMANDS'].items():
    app.logger.info('Loaded project %s (%s)', project, command)

@app.route("/hook/<project>", methods=["POST"])
def hook(project):
    if project not in app.config['COMMANDS']:
        app.logger.info('Unknown project %s' % project)
        return abort(404)
    rc = subprocess.call(app.config['COMMANDS'][project])
    return Response() if rc == 0 else abort(500)
