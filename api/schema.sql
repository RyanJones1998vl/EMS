DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS salary;
DROP TABLE IF EXISTS leave_application;
DROP TABLE IF EXISTS customer_expression;
DROP TABLE IF EXISTS expression_summary;

CREATE TABLE employee (
  employee_id TEXT PRIMARY KEY,
  email TEXT NOT NULL,
  full_name TEXT NOT NULL,
  password TEXT NOT NULL,
  role TEXT NOT NULL, 
  gender TEXT NOT NULL,
  dob TEXT,
  contact TEXT,
  start_day TEXT,
  address_1 TEXT,
  address_2 TEXT,
  id_card TEXT NOT NULL
);
INSERT INTO employee(employee_id, email, full_name, password, role, gender, id_card, contact, start_day)
VALUES ("nhp1998", "nhp1998@gmail.com", "Ngo Hoang Phuc", "nhp1998", "Admin", "Male", "1", "", "");

INSERT INTO employee(employee_id, email, full_name, password, role, gender, id_card, contact, start_day)
VALUES ("nva1996", "nva@gmail.com", "Nguyen Van A", "nva1996", "Employee", "Male", "2", "", "");

INSERT INTO employee(employee_id, email, full_name, password, role, gender, id_card, contact, start_day)
VALUES ("tvb1999", "tvb@gmail.com", "Tran Van B", "tvb1999", "Employee", "Female", "3", "", "");

INSERT INTO employee(employee_id, email, full_name, password, role, gender, id_card, contact, start_day)
VALUES ("htc1997", "htc@gmail.com", "Ha Thi C", "htc1997", "Employee", "Male", "23", "", "");

CREATE TABLE salary (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT,
  salary INTEGER NOT NULL,
  bank TEXT,
  account TEXT,
  account_holder TEXT,
  tax_number TEXT,
  FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);
INSERT INTO salary(employee_id, salary, bank, account, account_holder, tax_number)
VALUES ("htc1997", 10000000, "Agribank", "BankAccount", "Ha Thi C", "11111");
INSERT INTO salary(employee_id, salary, bank, account, account_holder, tax_number)
VALUES ("nva1996", 12000000, "Sacombank", "BankAccount", "Nguyen Van A", "123123");
INSERT INTO salary(employee_id, salary, bank, account, account_holder, tax_number)
VALUES ("tvb1999", 9000000, "Sacombank", "BankAccount", "Tran Van B", "000000");

CREATE TABLE leave_application (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT NOT NULL,
  leave_type TEXT NOT NULL,
  day_from TEXT NOT NULL,
  day_to TEXT,
  reason TEXT,
  status TEXT,
  FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);
INSERT INTO leave_application(employee_id, leave_type, day_from, day_to, reason, status)
VALUES ("htc1997", "Sick Leave", "12/17/2021", "", "", "Approved");

CREATE TABLE customer_expression (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT,
  emotion_1 TEXT NOT NULL,
  prob_emotion_1 REAL NOT NULL,
  emotion_2 TEXT NOT NULL,
  prob_emotion_2 REAL NOT NULL,
  emotion_3 TEXT NOT NULL,
  prob_emotion_3 REAL NOT NULL,
  time TEXT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

CREATE TABLE expression (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT,
  date TEXT NOT NULL,
  prob_emotion_1 REAL NOT NULL,
  prob_emotion_2 REAL NOT NULL,
  prob_emotion_3 REAL NOT NULL,
  prob_emotion_4 REAL NOT NULL,
  prob_emotion_5 REAL NOT NULL,
  prob_emotion_6 REAL NOT NULL,

  FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);
CREATE TABLE rspt (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  rspt TEXT NOT NULL

);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("htc1997", "10/30/2021", 0.65, 0.15, 0.01, 0.09, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("htc1997", "10/30/2021", 0.55, 0.25, 0.01, 0.09, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("htc1997", "10/30/2021", 0.45, 0.25, 0.11, 0.09, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("htc1997", "10/30/2021", 0.35, 0.25, 0.11, 0.19, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("htc1997", "10/30/2021", 0.25, 0.25, 0.11, 0.19, 0.15, 0.05);

INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("tvb1999", "10/31/2021", 0.68, 0.15, 0.01, 0.06, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("tvb1999", "10/31/2021", 0.58, 0.25, 0.01, 0.06, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("tvb1999", "10/31/2021", 0.48, 0.25, 0.11, 0.06, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("tvb1999", "10/31/2021", 0.38, 0.25, 0.11, 0.16, 0.05, 0.05);
INSERT INTO expression(employee_id, date, prob_emotion_1, prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6)
VALUES ("tvb1999", "10/31/2021", 0.28, 0.25, 0.11, 0.16, 0.15, 0.05);