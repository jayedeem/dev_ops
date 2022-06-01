from flask import Blueprint, jsonify, abort, request
from requests import Response
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])
def index():
    user = User.query.all()
    result = []
    for u in user:
        result.append(u.serialize())
    return jsonify(result)


@bp.route('/<int:id>',  methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'username' and 'password' not in request.json:
        return abort(400)

    if len(request.json['username']) <= 3 or len(request.json['password']) <= 8:
        return abort(400)
    u = User(username=request.json['username'],
             password=scramble(request.json['password']))

    db.session.add(u)
    db.session.commit()

    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int) -> Response:
    u = User.query.get_or_404(id)

    if 'username' in request.json:
        if len(request.json['username']) <= 3:
            abort(400, description="Username length must be greater than 3 characters!")

        u.username = request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) <= 8:
            return abort(400)

        u.password = request.json['password']

    try:
        # db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/liked_tweets', methods=["GET"])
def like_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for u in u.liked_tweets:
        result.append(u.serialize())
    return jsonify(result)
