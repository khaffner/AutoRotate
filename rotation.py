import os
from flask import Flask

app = Flask(__name__)

# Simple secret, ok for home env.  
# User must know this string. Just put som gibberish.
secret = 'replaceme'

# display must be one of the displys listed by xrandr --listmonitors. eDP-1 for example in my case.
# orientation must be one of (normal,inverted,left,right).
@app.route(f'/{secret}/rotate/<display>/<orientation>')
def rotate(display,orientation):
    os.system(f'xrandr --output {display} --rotate {orientation}')
    return (orientation + '\n')

if __name__ == "__main__":
    app.run(host='0.0.0.0')