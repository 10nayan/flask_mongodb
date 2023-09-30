from flask import jsonify, request
from . import api_bp
from models import User

@api_bp.route("/create_user", methods = ["POST"])
def create_user():
    user = User(username = request.json.get('username'), email = request.json.get('email'))
    try:
        saved_user = user.save()
        return saved_user.to_json()
    except Exception as e:
        return {"message":type(e).__name__}, 400
    
@api_bp.route("/get_all", methods = ["GET"])
def get_all_user():
    try:
        users = User.objects.all()
        return users.to_json()
    except Exception as e:
        return {"message":type(e).__name__}, 400
    
@api_bp.route("/get_user/<username>", methods = ["GET"])
def get_user(username):
    try:
        user = User.objects(username = username)
        return user.to_json()
    except Exception as e:
        return {"message":type(e).__name__}, 400
    
@api_bp.route("/update_user/<string:username_to_update>", methods = ["PATCH"])
def update_user(username_to_update):
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        user = User.objects(username = username_to_update)
        if username:
            user.update_one(set__username = username)
        if email:
            user.update_one(set__email = email)
        return user.to_json()
    except Exception as e:
        return {"message":type(e).__name__}, 400
    
@api_bp.route('/delete_user/<string:username>', methods=['DELETE'])
def delete_user(username):
    try:
        user_to_delete = User.objects(username = username).first()
        if user_to_delete:
            user_to_delete.delete()
            users = User.objects.all()
            return users.to_json()
        else:
            return {"message": "User not found"}, 404
    except Exception as e:
        return {"message": str(e)}, 500