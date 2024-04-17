
-- create
CREATE TABLE STAN (
  №_показания INTEGER PRIMARY KEY,
  Дата_и_время TEXT NOT NULL,
  Частота_вибрации INTEGER NOT NULL
  потребляемая_мощность INTEGER NOT NULL,
  температуры INTEGER NOT NULL,
  номер_станка INTEGER NOT NULL,
);

-- insert
INSERT INTO STAN VALUES (0001, '14.02.2024 12:00', 60,500, 50,1);
INSERT INTO STAN VALUES (0002, '14.02.2024 15:00', 80,700, 55,1);
INSERT INTO STAN VALUES (0003, '15.02.2024 11:00', 40,200, 34,2);
INSERT INTO STAN VALUES (0004, '15.02.2024 15:00', 120,900, 80,2);


-- fetch 
SELECT * FROM EMPLOYEE 