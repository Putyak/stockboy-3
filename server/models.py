from datetime import date
from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Alias(db.Model):
    Product_SKU = db.Column(db.String(), primary_key=True)
    Alias = db.Column(db.String(), nullable=False)
    Date = db.Column(db.Date(), nullable=False)
    Owner = db.Column(db.String(), nullable=False)
    products = db.relationship(
        'Products', back_populates="SKU_del", cascade='all, delete, delete-orphan')


class Products(db.Model):
    SKU = db.Column(db.String(), db.ForeignKey(
        "alias.Product_SKU", ondelete='cascade'), nullable=False)
    SKU_del = db.relationship('Alias', foreign_keys=[SKU])
    Product_ID = db.Column(db.String(), primary_key=True)
    Name = db.Column(db.String(), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    Owner = db.Column(db.String(), nullable=False)
    invetories = db.relationship(
        'Invetory', back_populates="inv_del", cascade='all, delete, delete-orphan')
    op1s = db.relationship(
        'Orders_Products', back_populates="op1_del", cascade='all, delete, delete-orphan')


class Invetory(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.String(), db.ForeignKey(
        'products.Product_ID', ondelete="cascade"), nullable=False)
    inv_del = db.relationship('Products', foreign_keys=[Product_ID])
    Stock = db.Column(db.String(), nullable=False)
    Available = db.Column(db.String(), nullable=False)


class Warehouses(db.Model):
    Warehouse_ID = db.Column(db.String(), primary_key=True)
    Origin_Address = db.Column(db.String(), nullable=False)
    Return_Address = db.Column(db.String(), nullable=False)
    Origin_Phone = db.Column(db.String(), unique=True, nullable=False)
    Return_Phone = db.Column(db.String(), unique=True, nullable=False)
    Origin_Name = db.Column(db.String(), nullable=False)
    Return_Name = db.Column(db.String(), nullable=False)
    orders = db.relationship(
        'Orders', back_populates="ord_del", cascade='all, delete, delete-orphan')
    ship1s = db.relationship(
        'Shipments', back_populates="shi1_del", cascade='all, delete, delete-orphan')


class Orders(db.Model):
    Order_ID = db.Column(db.String(), primary_key=True)
    Date = db.Column(db.Date(), nullable=False)
    Order_key = db.Column(db.String(), nullable=False)
    Order_Number = db.Column(db.Integer, nullable=False, unique=True)
    Order_Total = db.Column(db.Integer, nullable=False)
    Owner = db.Column(db.String(), nullable=False)
    Customer_Notes = db.Column(db.String(), nullable=False)
    Shipping = db.Column(db.String(), nullable=False)
    Customer_ID = db.Column(db.String(), unique=True, nullable=False)
    Status = db.Column(db.String(), nullable=False)
    Store_ID = db.Column(db.Integer, nullable=False)
    Warehouse_ID = db.Column(db.String(), db.ForeignKey(
        'warehouses.Warehouse_ID', ondelete="cascade"), nullable=False)
    ord_del = db.relationship('Warehouses', foreign_keys=[Warehouse_ID])
    Number_of_Products = db.Column(db.Integer, nullable=False)
    ships = db.relationship(
        'Shipments', back_populates="shi_del", cascade='all, delete, delete-orphan')
    ops = db.relationship(
        'Orders_Products', back_populates="op_del", cascade='all, delete, delete-orphan')
    ffs = db.relationship('Fulfillments', back_populates="ff_del",
                          cascade='all, delete, delete-orphan')
    ff1s = db.relationship(
        'Fulfillments', back_populates="ff1_del", cascade='all, delete, delete-orphan')
    ff2s = db.relationship(
        'Fulfillments', back_populates="ff2_del", cascade='all, delete, delete-orphan')
    cust_dels = db.relationship(
        'Customers', back_populates="cust_del", cascade='all, delete, delete-orphan')
    st_dels = db.relationship(
        'Stores', back_populates="st_del", cascade='all, delete, delete-orphan')


class Shipments(db.Model):
    Shipment_ID = db.Column(db.String(), primary_key=True)
    Order_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Order_ID', ondelete="cascade"), nullable=False)
    shi_del = db.relationship('Orders', foreign_keys=[Order_ID])
    Created_Date = db.Column(db.Date(), nullable=False)
    Shipping_Date = db.Column(db.Date(), nullable=False)
    Tracking_Number = db.Column(db.Integer, nullable=False)
    Carrier_Code = db.Column(db.Integer, nullable=False)
    Service_Code = db.Column(db.Integer, nullable=False)
    Package_Code = db.Column(db.Integer, nullable=False)
    Warehouse_ID = db.Column(db.String(), db.ForeignKey(
        'warehouses.Warehouse_ID', ondelete="cascade"), nullable=False)
    shi1_del = db.relationship('Warehouses', foreign_keys=[Warehouse_ID])


class Orders_Products(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.String(), db.ForeignKey(
        'products.Product_ID', ondelete="cascade"), nullable=False)
    op1_del = db.relationship('Products', foreign_keys=[Product_ID])
    Order_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Order_ID', ondelete="cascade"), nullable=False)
    op_del = db.relationship('Orders', foreign_keys=[Order_ID])


class Fulfillments(db.Model):
    Fulfillment_ID = db.Column(db.Integer, primary_key=True)
    Order_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Order_ID', ondelete="cascade"), nullable=False)
    ff_del = db.relationship('Orders', foreign_keys=[Order_ID])
    Customer_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Customer_ID', ondelete="cascade"), nullable=False)
    ff1_del = db.relationship('Orders', foreign_keys=[Customer_ID])
    Order_Number = db.Column(db.String(), db.ForeignKey(
        'orders.Order_Number', ondelete="cascade"), nullable=False)
    ff2_del = db.relationship('Orders', foreign_keys=[Order_Number])

    User_ID = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(), nullable=False)


class Customers(db.Model):
    Customer_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Customer_ID', ondelete="cascade"), primary_key=True)
    cust_del = db.relationship('Orders', foreign_keys=[Customer_ID])
    Name = db.Column(db.String(), nullable=False)
    Address = db.Column(db.String(), nullable=False)
    Email = db.Column(db.String(), nullable=False)


class Stores(db.Model):
    Store_ID = db.Column(db.String(), db.ForeignKey(
        'orders.Store_ID', ondelete="cascade"), primary_key=True)
    st_del = db.relationship('Orders', foreign_keys=[Store_ID])
    Store_Name = db.Column(db.String(), nullable=False)
    Owner = db.Column(db.String(), nullable=False)
    Marketplace_Name = db.Column(db.String(), nullable=False)
    Active = db.Column(db.String(), nullable=False)
    Accpunt_Name = db.Column(db.String(), nullable=False)
