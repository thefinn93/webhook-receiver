# Webhook Receiver

Very simple tool that runs a pre-defined command when an HTTP POST is sent to it. Intended to do things like `git pull`
in response to a GitHub webhook.


## Installation
```
pip install git+https://github.com/thefinn93/webhook-receiver
```

to install the latest version. Maybe I'll put it in pypi some day.

Next, you'll probably want to install something to serve it with, rather than the flask built in web server.
`gunicorn` is what I use:

```
pip install gunicorn
```

Finally, run gunicorn to start the server:

```
gunicorn -b 0.0.0.0 webhook_receiver:app
```

Obviously you'll probably want it running as a daemon and probably managed by your init system, take a look at
`webhook-receiver.service` in this directory for a sample systemd unit file, although you will likely need to modify it
to your liking.

## Configuration
Configuration is done via a python file. Place it in `/etc/webhook-receiver.settings.py` or specify the path to it in an
environment variable called `WEBHOOK_RECEIVER_SETTINGS`. It should define a variable, `COMMANDS`, as a dictionary. Each
key represents the path that will be requested (`/hook/<key>`), and each value is the command to run when it is. For
example:

```python
COMMANDS = {
    "myrepo": ["git", "-C", "/usr/local/src/myrepo", "pull"]
}
```

Then instruct the webhook sender (eg GitHub) to request `http://<your server>/hooks/myrepo`. Configuration is read once
at startup, so you'll need to restart the server if you change the config.
