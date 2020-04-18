from chalice import Chalice

app = Chalice(app_name='WalkthroughAPI')


@app.route('/')
def index():
    return {'hello': 'world'}

@all.route('/auth')
def auth():
    return {"token":"blahblah"}

@app.route('/create-game',methods=['POST'])
def create_game():
    return {'hello': 'world'}

@app.route('/create-section',methods=['POST'])
def create_section():
    return {'hello': 'world'}

@app.route('/create-trick',methods=['POST'])
def create_trick():
    return {'hello': 'world'}
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
