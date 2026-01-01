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
