# # What is RDBMS?
# #RDBMS stands for Relational Database Management System.
# # RDBMS is the basis for SQL, and for all modern database systems like MS SQL Server, IBM DB2, Oracle, MySQL,
# # and Microsoft Access.
#
# A Relational database management system (RDBMS) is a database management system (DBMS) that is based on
# the relational model as introduced by E. F.



# What is a table?
# The data in an RDBMS is stored in database objects which are called as tables.
# This table is basically a collection of related data entries and it consists of numerous columns and rows.



# What is a field?
# Every table is broken up into smaller entities called fields.
# The fields in the CUSTOMERS table consist of ID, NAME, AGE, ADDRESS and SALARY.
# A field is a column in a table that is designed to maintain specific information about every record in the table.



# What is a Record or a Row?
# A record is also called as a row of data is each individual entry that exists in a table.
# For example, there are 7 records in the above CUSTOMERS table. Following is a single row of data or record in the CUSTOMERS table −
#
# +----+----------+-----+-----------+----------+
# |  1 | Ramesh   |  32 | Ahmedabad |  2000.00 |
# +----+----------+-----+-----------+----------+



# What is a column?
# A column is a vertical entity in a table that contains all information associated with a specific field in a table.
#
# For example, a column in the CUSTOMERS table is ADDRESS, which represents location description and would be as shown below −
#
# +-----------+
# | ADDRESS   |
# +-----------+
# | Ahmedabad |
# | Delhi     |
# | Kota      |
# | Mumbai    |
# | Bhopal    |
# | MP        |
# | Indore    |
# +----+------+
# What is a NULL value?
# A NULL value in a table is a value in a field that appears to be blank, which means a field with a NULL value is a field with no value.
#
# It is very important to understand that a NULL value is different than a zero value or a field that contains spaces. A field with a NULL value is the one that has been left blank during a record creation.
#
# SQL Constraints
# Constraints are the rules enforced on data columns on a table. These are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the database.
#
# Constraints can either be column level or table level. Column level constraints are applied only to one column whereas, table level constraints are applied to the entire table.
#
# Following are some of the most commonly used constraints available in SQL −
#
# NOT NULL Constraint − Ensures that a column cannot have a NULL value.
#
# DEFAULT Constraint − Provides a default value for a column when none is specified.
#
# UNIQUE Constraint − Ensures that all the values in a column are different.
#
# PRIMARY Key − Uniquely identifies each row/record in a database table.
#
# FOREIGN Key − Uniquely identifies a row/record in any another database table.
#
# CHECK Constraint − The CHECK constraint ensures that all values in a column satisfy certain conditions.
#
# INDEX − Used to create and retrieve data from the database very quickly.
#
# Data Integrity
# The following categories of data integrity exist with each RDBMS −
#
# Entity Integrity − There are no duplicate rows in a table.
#
# Domain Integrity − Enforces valid entries for a given column by restricting the type, the format, or the range of values.
#
# Referential integrity − Rows cannot be deleted, which are used by other records.
#
# User-Defined Integrity − Enforces some specific business rules that do not fall into entity, domain or referential integrity.
#
# Database Normalization
# Database normalization is the process of efficiently organizing data in a database. There are two reasons of this normalization process −
#
# Eliminating redundant data, for example, storing the same data in more than one table.
#
# Ensuring data dependencies make sense.
#
# Both these reasons are worthy goals as they reduce the amount of space a database consumes and ensures that data is logically stored. Normalization consists of a series of guidelines that help guide you in creating a good database structure.
#
# Normalization guidelines are divided into normal forms; think of a form as the format or the way a database structure is laid out. The aim of normal forms is to organize the database structure, so that it complies with the rules of first normal form, then second normal form and finally the third normal form.
#
# It is your choice to take it further and go to the fourth normal form, fifth normal form and so on, but in general, the third normal form is more than enough.
#
# First Normal Form (1NF)
# Second Normal Form (2NF)
# Third Normal Form (3NF)



