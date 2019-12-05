from flask import Flask
from flask_cas_fix import CAS
import config
import os

dir = os.path.abspath('orangepages/templates')
app = Flask(__name__, template_folder=dir)
cas = CAS(app, '/cas')
app.config.from_object(config.Config)
app.config["IMAGE_UPLOADS"] = "./orangepages/static/uploads/"
app.config["IMAGE_UPLOADS_RELATIVE"] = "../static/uploads/"

# Import and register views.
from orangepages.views import general, post, search, user, error, test, friend
blueprints = [general, post, search, user, error, test, friend]
for bp in blueprints:
    app.register_blueprint(bp.page)
