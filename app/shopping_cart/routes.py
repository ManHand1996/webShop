from app.shopping_cart import cart_blueprint


@cart_blueprint.route('/test', methods=['GET'])
def test():
    r = sf.h()
    return r