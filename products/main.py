from flask import Blueprint
products = Blueprint('Products', __name__)

@products.route('/', methods=['GET'])
def index():
    return []
