CREATE TABLE Account (
    ANo INT,
    AName VARCHAR(30),
    Address VARCHAR(30)
);

INSERT INTO Account VALUES
(101, 'Nirja Singh', 'Bangalore'),
(102, 'Rohan Gupta', 'Chennai'),
(103, 'Ali Reza', 'Hyderabad'),
(104, 'Rishabh Jain', 'Chennai'),
(105, 'Simran Kaur', 'Chandigarh');

CREATE TABLE Transact (
    TRNo VARCHAR(5),
    ANo INT,
    Amount INT,
    Type VARCHAR(15),
    DOT DATE
);

INSERT INTO Transact VALUES
('T001', 101, 2500, 'Withdraw', '2017-12-21'),
('T002', 103, 3000, 'Deposit',  '2017-06-01'),
('T003', 102, 2000, 'Withdraw', '2017-05-12'),
('T004', 103, 1000, 'Deposit',  '2017-10-22'),
('T005', 102, 12000,'Deposit',  '2017-11-06');
