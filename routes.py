from config import app
from controller_functions import index, create_dojo, create_ninja



app.add_url_rule("/", view_func=index)
app.add_url_rule("/create_dojo", view_func=create_dojo, methods=["POST"])
app.add_url_rule("/create_ninja", view_func=create_ninja, methods=["POST"])



