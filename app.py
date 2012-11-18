import os
from flask import (
    Flask,
    Response,
    session,
    redirect,
    abort,
    url_for,
    escape,
    request,
    render_template,
)

from model import *
from sqlalchemy.orm import create_session
session = create_session()


app = Flask(__name__)
app.secret_key = 'Zgb1krq^_@s&*)qz03^jcfl4w+tle660s$z1#mtemu5b(m=$fudn##@'

@app.route('/restaurant/')
def main():
    restaurant_id = request.args.get('restaurant_id')
    restaurant = session.query(Restaurant).get(restaurant_id)
    chef = restaurant.Chefs[0]
    print ["%s %s" % (c.first_name, c.last_name) for c in restaurant.Chefs]
    return render_template('index.html',
        restaurant=restaurant,
        chef=chef,

    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    # HEROKU LIVE
    #app.run(host='0.0.0.0', port=port)
    # UNCOMMENT FOR RUNNING LOCALLY
    app.run()
