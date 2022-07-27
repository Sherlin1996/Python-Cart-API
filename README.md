# 購物車API

## /Login

### **post**

登入
. 送出: account、password
. 回傳: token
```
####登入成功
{
    "data": {
        "message": "Welcome back Bob",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODg5NDIwMCwianRpIjoiYzlhYzdlN2UtNTI4MC00YjQzLTkzNGItOWU5NzU3YWU5ZTZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJhY2NvdW50IjoiMTIzIn0sIm5iZiI6MTY1ODg5NDIwMCwiZXhwIjoxNjU4OTgwNjAwfQ.I2nZGqO73-U0zHMB5TzKBkBKGjrK5pIG4c5lK1Rbaxk"
    },
    "datatime": "Wed, 27 Jul 2022 11:56:40 GMT",
    "message": "success"
}
```
## /product
### **get**
搜尋所有產品
回傳:所有產品 價錢、數量、金額
```
{
    "products": [
        {
            "price": "30",
            "product": "banana",
            "quantity": "1000"
        },
        {
            "price": "30",
            "product": "pieapple",
            "quantity": "10"
        },
        {
            "price": "30",
            "product": "mango",
            "quantity": "40"
        },
        {
            "price": "30",
            "product": "apple",
            "quantity": "1000"
        },
        {
            "price": "30",
            "product": "apple",
            "quantity": "1000"
        }
    ],
    "total": [
        {
            "total": 91500.0
        }
    ]
}
```
### **post**
新增產品
* 送出:product、quality、price
* 回傳:成功訊息
```
{
    "message": "success"
}
```
### **patch**
更改產品資訊
* 路由參數 string:name
* 送出:product、quality、price
* 回傳:成功訊息
```
{
    "message": "success"
}
```
### **delete**
刪除產品
* 路由參數 string:name
* 送出:product、quality、price
* 回傳:成功訊息
```
{
    "message": "success"
}
```
### ***get***
模糊搜尋產品
* 路由參數 string:name
* 回傳: 所有符合的產品名稱、價錢、數量、總金額
```
{
    "products": [
        {
            "price": "30",
            "product": "banana",
            "quantity": "1000"
        },
        {
            "price": "30",
            "product": "mango",
            "quantity": "40"
        }
    ],
    "total": [
        {
            "total": 31200.0
        }
    ]
}
```
