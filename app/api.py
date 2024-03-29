from flask import request
from flask_appbuilder.api import BaseApi, ModelRestApi, expose, rison, safe
from flask_appbuilder.security.decorators import protect
from flask_appbuilder.models.sqla.interface import SQLAInterface


from . import appbuilder
from .models import Contact, ContactGroup, Gender, Product, Seller, Courier, Order, Cart


greeting_schema = {"type": "object", "properties": {"name": {"type": "string"}}}


class GroupModelApi(ModelRestApi):
    resource_name = 'group'
    datamodel = SQLAInterface(ContactGroup)
    allow_browser_login = True


appbuilder.add_api(GroupModelApi)


class ContactModelApi(ModelRestApi):
    resource_name = 'contact'
    datamodel = SQLAInterface(Contact)
    allow_browser_login = True


appbuilder.add_api(ContactModelApi)


class ProductModelApi(ModelRestApi):
    resource_name = 'product'
    datamodel = SQLAInterface(Product)
    allow_browser_login = True


appbuilder.add_api(ProductModelApi)


class SellerModelApi(ModelRestApi):
    resource_name = 'seller'
    datamodel = SQLAInterface(Seller)
    allow_browser_login = True


appbuilder.add_api(SellerModelApi)


class CourierModelApi(ModelRestApi):
    resource_name = 'courier'
    datamodel = SQLAInterface(Courier)
    allow_browser_login = True


appbuilder.add_api(CourierModelApi)


class OrderModelApi(ModelRestApi):
    resource_name = 'order'
    datamodel = SQLAInterface(Order)
    allow_browser_login = True


appbuilder.add_api(OrderModelApi)


class CartModelApi(ModelRestApi):
    resource_name = 'cart'
    datamodel = SQLAInterface(Cart)
    allow_browser_login = True


appbuilder.add_api(CartModelApi)


# class Client(BaseApi):
#
#     resource_name = "product"
#
#     @expose("/clients", methods=["GET"])
#     def get_client_list(self):
#         pass
#
#     @expose("/client/<int:id>", methods=["GET"])
#     def get_client(self):
#         pass
#
#
# appbuilder.add_api(Client)


class BotGetProducts(BaseApi):

    resource_name = "bot"
    apispec_parameter_schemas = {"greeting_schema": greeting_schema}

    @expose("/product/getList", methods=["GET"])
    def product_get_list(self):
        """Send a greeting
        ---
        get:
          responses:
            200:
              description: Greet the user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        return self.response(200, message="Hello")

    @expose("/product/getItem/<int:id>", methods=["GET"])
    def product_get_item_by_id(self):
        pass

    # @expose("/getList", methods=["POST", "GET"])
    # def greeting2(self):
    #     """Send a greeting
    #     ---
    #     get:
    #       responses:
    #         200:
    #           description: Greet the user
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #                 properties:
    #                   message:
    #                     type: string
    #     post:
    #       responses:
    #         201:
    #           description: Greet the user
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #                 properties:
    #                   message:
    #                     type: string
    #     """
    #     if request.method == "GET":
    #         return self.response(200, message="Hello (GET)")
    #     return self.response(201, message="Hello (POST)")
    #
    # @expose("/greeting3")
    # @rison()
    # def greeting3(self, **kwargs):
    #     if "name" in kwargs["rison"]:
    #         return self.response(
    #             200, message="Hello {}".format(kwargs["rison"]["name"])
    #         )
    #     return self.response_400(message="Please send your name")
    #
    # @expose("/greeting4")
    # @rison(greeting_schema)
    # def greeting4(self, **kwargs):
    #     """Get item from Model
    #     ---
    #     get:
    #       parameters:
    #       - $ref: '#/components/parameters/greeting_schema'
    #       responses:
    #         200:
    #           description: Greet the user
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #                 properties:
    #                   message:
    #                     type: string
    #     """
    #     return self.response(200, message="Hello {}".format(kwargs["rison"]["name"]))

    # @expose("/risonjson")
    # @rison()
    # def rison_json(self, **kwargs):
    #     """Say it's risonjson
    #     ---
    #     get:
    #       responses:
    #         200:
    #           description: Say it's private
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #     """
    #     return self.response(200, result=kwargs["rison"])

    # @expose("/private")
    # @protect()
    # def private(self):
    #     """Say it's private
    #     ---
    #     get:
    #       responses:
    #         200:
    #           description: Say it's private
    #           content:
    #             application/json:
    #               schema:
    #                 type: object
    #         401:
    #           $ref: '#/components/responses/401'
    #     """
    #     return self.response(200, message="This is private")
    #
    # @expose("/error")
    # @protect()
    # @safe
    # def error(self):
    #     """Error 500
    #     ---
    #     get:
    #       responses:
    #         500:
    #           $ref: '#/components/responses/500'
    #     """
    #     raise Exception


appbuilder.add_api(BotGetProducts)
