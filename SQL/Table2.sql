use practl;

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

select * from Doctors;
select * from Patients;

## 1
select PatNo, PatName, DocName
from Doctors, Patients
where Doctors.DocID = Patients.DocID;

## 2
select count(distinct Department) from Patients;

## 3 
select * from Doctors 
where NoofOpdDays > 3;

## 4
select DocId, Docname from Doctors
where Department = "ENT";

## 5
select Doctors.DocId, Doctors.DocName, Doctors.Department, Patients.PatName
from Doctors, Patients
where Doctors.DocId = Patients.DocId
and Doctors.DocId in (101,103);

## 6 
select * from Doctors
where DocName like "M%";

## 7 
select DocID, DocName from Doctors
where Department = "Ortho";

## 8
select * from Doctors
where NoofOpdDays < 3;
