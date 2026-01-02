create database practl;
use practl;

CREATE TABLE Item (
    ICode VARCHAR(5),
    IName VARCHAR(30),
    Price INT,
    Color VARCHAR(15),
    VCode VARCHAR(5)
);

INSERT INTO Item VALUES
('S001', 'Mobile Phones', 30000, 'Silver', 'P01'),
('S002', 'Refrigerator', 20000, 'Cherry', 'P02'),
('S003', 'TV', 45000, 'Black', 'P03'),
('S004', 'Washing Machine', 12000, 'White', 'P04'),
('S005', 'Air Conditioner', 50000, 'White', 'P05');

CREATE TABLE Vendor (
    VCode VARCHAR(5),
    VName VARCHAR(20)
);

INSERT INTO Vendor VALUES
('P01', 'Rahul'),
('P02', 'Mukesh'),
('P03', 'Rohan'),
('P04', 'Kapil');

## 1
select ICode, IName, VName
from Item, Vendor
where Item.VCode = Vendor.VCode and IName = "Refrigerator";

## 2
select IName, ICode, VName, Price
from Item, Vendor
where Item.VCode = Vendor.Vcode and Price > 23000;

## 3
select IName from Item
where IName like "%r";

## 4
select * from Item
order by VCode;

## 5
select VName, IName
from Item, Vendor
where Item.VCode = Vendor.VCode and Vendor.VCode = "P04";

## 6
select Color, count(Color)
from Item
group by Color;

## 7
select * from Item
where Price < 30000;

## 8
select * from Item
order by Price;
