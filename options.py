from flask_restful import reqparse
import pymysql
from flask import jsonify
import util, model
from flask_apispec import doc, use_kwargs, MethodResource, marshal_with
from model import UserGetResponse, UseranotherResponse, \
    UserPostRequest, UserPatchRequest, LoginReqest
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta

def db_init():
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3307,
        db='api_class'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor

def get_access_token(account):
    token = create_access_token(
        identity={"account": account},
        expires_delta=timedelta(days=1)
    )
    return token

class product(MethodResource):
    @doc(description="GET products info", tags=['cart'])
    def get(self):
        db, cursor = db_init()
        
        sql1 = "SELECT * FROM api_class.cart;"
        cursor.execute(sql1)
        products = cursor.fetchall()
        
        sql2 = "SELECT sum(price*quantity) as total FROM api_class.cart;"
        cursor.execute(sql2)
        total = cursor.fetchall()
        
        re={"products":products,"total":total}
        db.close()
        return re
    
    @doc(description="Post products info", tags=['cart'])
    @use_kwargs(UserPostRequest,location="json")    #帶入已設定好資料型態的變數
    @jwt_required()
    @marshal_with(UseranotherResponse, code=200)   # 回傳值的資料型態

    def post(self,**kwargs):
        db, cursor = db_init()

        product = {
            'product': kwargs['product'],
            'price': kwargs['price'],
            'quantity': kwargs['quantity']
        }
        sql = """

        INSERT INTO `api_class`.`cart` (`product`,`price`,`quantity`)
        VALUES ('{}','{}','{}');

        """.format(
            product['product'], product['price'], product['quantity'])
            
        result = cursor.execute(sql)
        
        db.commit()
        db.close()

        if result == 1:
            return util.success()
                
        return util.failure()

class edit(MethodResource):
    @doc(description="Patch product info", tags=['cart'])
    @use_kwargs(UserPatchRequest,location="json")
    @jwt_required()
    @marshal_with(UseranotherResponse, code=200)

    def patch(self, name,**kwargs):
        db, cursor = db_init()
      
        product = {
            'product': kwargs.get('product'),
            'price': kwargs.get('price'),
            'quantity': kwargs.get('quantity')
        }

        query = []
  
        for key, value in product.items():
            if value is not None:
                query.append(f"{key} = '{value}'")
        query = ",".join(query)
   
        sql = """
            UPDATE api_class.cart
            SET {}
            WHERE product = '{}';
        """.format(query, name)

        result = cursor.execute(sql)
        
        db.commit()
        db.close()
        
        if result == 1:
            return util.success()
                
        return util.failure()

    @doc(description="Delete product info", tags=['cart'])
    @jwt_required()
    @marshal_with(UseranotherResponse, code=200)

    def delete(self, name):
        db, cursor = db_init()
        sql = f"DELETE FROM `api_class`.`cart` WHERE product = '{name}';"
        result = cursor.execute(sql)
        message = "success" if result == 1 else "failure"
        db.commit()
        db.close()

        if result == 1:
            return util.success()
                
        return util.failure()

    @doc(description="Get products info", tags=['cart'])
    @jwt_required()
    def get(self, name):
        db, cursor = db_init()

        sql1 = f"SELECT * FROM api_class.cart where product like '%{name}%';"
        cursor.execute(sql1)
        products = cursor.fetchall()

        
        sql2 = f"SELECT sum(price*quantity) as total FROM api_class.cart where product like '%{name}%';"
        cursor.execute(sql2)
        total = cursor.fetchall()
        
        re={"products":products,"total":total}
        db.close()
        return re


class Login(MethodResource):
    @doc(description='User Login', tags=['Login'])
    @use_kwargs(model.LoginReqest, location="json")    
    def post(self, **kwargs):
        db, cursor = db_init()
        account, password = kwargs["account"], kwargs["password"]
        sql = f"SELECT * FROM api_class.member WHERE account = '{account}' AND password = '{password}';" 
        cursor.execute(sql)
        user = cursor.fetchall()
        db.close()

        if user != ():
            token = get_access_token(account)
            data = {
                "message": f"Welcome back {user[0]['name']}",
                "token": token}
            return util.success(data)
        
        return util.failure({"message":"Account or password is wrong"})


        



