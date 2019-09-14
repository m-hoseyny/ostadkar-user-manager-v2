from . import user_routes
from .models import User
# from flask_login import login_user, login_required, header_loader
from flask import request, Response
import json
import datetime


def convert_datetime(time_object):
    if isinstance(time_object, (datetime.date, datetime.datetime)):
        return str(time_object)


def json_response(res, status):
    return Response(
        response=json.dumps(res, default=convert_datetime),
        status=status,
        mimetype='application/json'
    )


@user_routes.route('', methods=['POST'])
def create():
    data = request.get_json()
    if User.get_user(email=data.get('email')) or User.get_user(username=data.get('username')):
        return Response(
            {'error': 'UserExist'},
            status=400
        )
    user = User.create(data)
    return json_response({'status': 'ok', 'user_id': user.id}, 200)


@user_routes.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(User.to_dict, users))

    return json_response(users, 200)


@user_routes.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return json_response(user.to_dict(), 200)
    return json_response({'error': 'UserDoesntExist'}, 400)


@user_routes.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.delete()
        return json_response({'message': 'user ({}) deleted'.format(user_id)}, 200)
    return json_response({'error': 'UserDoesntExist'}, 400)


@user_routes.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.get_json()
    if user:
        user = user.update(data)
        print(user)
        return json_response(user.to_dict(), 200)
    return json_response({'error': 'UserDoesntExist'}, 400)
