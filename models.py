import pydantic
from tortoise import Model, fields, List 
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from datetime import datetime,timezone



def get_current_utc_datetime():
    return datetime.now(timezone.utc)

class User(Model):
    id = fields.IntField(pk= True, index= True)
    username=fields.CharField(unique= True, null=False, max_length=20)
    email=fields.CharField(max_length=200, null=False, unique= True)
    password = fields.CharField(max_length=100, null=False, unique= True)
    is_verified= fields.BooleanField(default=  False)
    join_date = fields.DatetimeField(default=get_current_utc_datetime)


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    bussiness_name= fields.CharField(null =False, unique= True, max_length=20)
    city = fields. CharField(null= False, unique= True, default = "Unspecified", max_length=20)
    region= fields.CharField(max_length=100, null =False, default= "Unspecified")
    business_description =  fields.CharField(null= True, max_length=100)
    logo= fields.CharField(max_length=200, null= False, default = "default.jpg")
    owner=  fields.ForeignKeyField("models.User", related_name= "business")




class Product(Model):
    id = fields.IntField(pk= True, index= True)
    name=  fields. CharField(max_length= 100, null= False, index= True)
    category = fields. CharField(max_length=30, index= True)
    original_price=  fields.DecimalField(max_digits= 12, decimal_places=2)
    new_price = fields.DecimalField(max_digits=12, decimal_places=2)
    percentage_discount=  fields.IntField()
    offer_expiration_date = fields.DatetimeField(default= get_current_utc_datetime)
    product_image = fields.CharField(max_length=200, null= False, default= "Productdefault.jpg")
    business= fields. ForeignKeyField("models.Business", related_name= "products")


user_pydantic= pydantic_model_creator(User, name= "User", exclude = ("is_verfied", ))
user_pydanticIn=pydantic_model_creator(User, name = "UserIn", exclude_readonly = True,
                                       exclude= ("is_verified", "join_date"))
user_pydanticOut = pydantic_model_creator(User, name = "UserOut",exclude= ("password" ))

business_pydantic= pydantic_model_creator(Business, name = "Business")
business_pydanticIn= pydantic_model_creator(Business, name= "BusinessIn", exclude_readonly=True)

product_pydantic = pydantic_model_creator(Product, name= "Product")
product_pydanticIn = pydantic_model_creator(Product, name= "ProductIn", exclude= ("percentage_discount", "id"))