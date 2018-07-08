import sys, os

if sys.version_info[0]<3:       # require python3
 raise Exception("Python3 required! Current (wrong) version: '%s'" %
 sys.version_info)

# To include the application's path in the Python search path
sys.path.insert(0,"/var/www/homeLEDController")

# Activate virtual env
 #activate_env=os.path.expanduser("/var/www/homeLEDController/venv/bin/activate_this.py")
 #execfile(activate_env, dict(__file__=activate_env))


# Construct a Flask instance "app" via package mypack's __init__.py
from app import app as application
