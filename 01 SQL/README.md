# Download the `mysql-installer-community`  If you don't have
- ### [Click 🔗](https://dev.mysql.com/downloads/installer/)


## Steps 
- ### Click the
- ### Select the latest version
- ### Select oprating system
- ### accoudaing to your System 
- ### Click to Download




---
---
---
---
## 1) Create  database 
- ##     syntax---> create database database_name;
- ##     eg musharraf (database) 

  ```
  create database musharraf;
  ```

## 2) to see all databae 
```
show databases;
```

## 3) select that database eg:- musharraf
- ##     syntax----> use datatbase_name;
- ## eg---> use musharraf;
```
use musharraf;
```

## 4) create table 
- ##     syntax---> create table table_name(column1 datatype, column2 datatype,----------n number of columns);
- ##    eg :-  create table  dept(DEPTNO INT(2) NOT NULL PRIMARY KEY, NMAME VARCHAR(14), LOC VARCHAR(13));
```
create table  dept(DEPTNO INT(2) NOT NULL PRIMARY KEY, NMAME VARCHAR(14), LOC VARCHAR(13));
```

 
## check table
- ###  syntax--> select * from dept;
```
select * from dept;
```
      
     

## 5)  insert value :- there is an two way to inster values in a table 

###   1) secure lilke  
- ###    syntax --->insert into table table_name(colum1,column2,-------n number of columns)values(value1,value2,-------n number of values)

###       2) unsecure          
- ###    syntax ---> insert into table_name values(value1,value2,value2,-----n numbe rof values)

## if yo want to insert many row at a time then 
- ###    syntax --->  insert into dept(DEPTNO,DNAME,LOC)values(10,"ACCOUNTING","NEW YOURK"),(20 ,"RESEARCH","DALLAS"),(30,"SALES","CHICHGO"),(40,"OPERATIONS","BOSTON");



## 6) update 
- ###    syntax ---> update table_name set  column1=value, column2=value, column3=value--------------n number of columns=n number on values;
- ###    eg :-
```
         update dept set Name="kali" where deptno=10;
```


## 7) delet :-  is used to delete row from the table  but ther space is not free that is containing by7 the table 
- ###    syntax ---> delet from table_name where condition;
- ###   e.g-->
```
delete from student where  id=04;
```


## truncate :- this use to free space and delet table row parmanently


## 8) drop :- is used to delete the table row togeher with the table definition so the relationship of that table with other  table will no londer be vaild.
- ####    syntax ---> drop table table_name;
- ###    e.g-->  
```
Drop table student;
```
 
## 9) Delete/ drop columns -----> use alter( it also use to add as well as delet columns) 
- ###    syntax ---> Alter table table_name  drop column column_name;
- ###     e.g--> 
```
alter table student drop column Name;
```
