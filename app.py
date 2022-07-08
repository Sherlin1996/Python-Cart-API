from flask import Flask
from flask_restful import Api
from options import product,edit,Login
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.extension import FlaskApiSpec
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "secret_key"
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})
docs = FlaskApiSpec(app)

api.add_resource(product, '/product')
docs.register(product)
api.add_resource(edit, '/product/<string:name>')
docs.register(edit)
api.add_resource(Login, '/Login')
docs.register(Login)

if __name__ == '__main__':
    JWTManager().init_app(app)
    app.run(debug=True)








