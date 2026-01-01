CREATE TABLE Doctors (
    DocID INT,
    DocName VARCHAR(30),
    Department VARCHAR(20),
    NoofOpdDays INT
);

INSERT INTO Doctors VALUES
(101, 'J K Mishra', 'Ortho', 3),
(102, 'Mahesh Tripathi', 'ENT', 4),
(103, 'Ravi Kumar', 'Neuro', 5),
(104, 'Mukesh Jain', 'Physio', 3);

CREATE TABLE Patients (
    PatNo INT,
    PatName VARCHAR(30),
    Department VARCHAR(20),
    DocID INT
);

INSERT INTO Patients VALUES
(1, 'Payal', 'ENT', 102),
(2, 'Naveen', 'Ortho', 101),
(3, 'Rakesh', 'Neuro', 103),
(4, 'Atul', 'Physio', 104);
