mport sys
import os
import os.path

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib_dir = os.path.join(root_dir, "eggs")
for filename in os.listdir(lib_dir):
        sys.path.append(os.path.join(lib_dir, filename))

        from flask import Flask
        from flaskext.mongoalchemy import MongoAlchemy

        app = Flask(__name__)
        app.config['MONGOALCHEMY_DATABASE'] = 'library'
        app.debug = True
        db = MongoAlchemy(app)

        import fiTracker.views
