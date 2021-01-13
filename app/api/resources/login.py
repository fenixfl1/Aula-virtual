from flask_restful import Resource


class Login(Resource):
    
    def get():
        return {"message": "Hello!!!"}