drop table if exists directory;
create table directory (
       id integer primary key autoincrement,
       email text not null,
       username text not null, 
       phone integer not null,
       picture BLOB not null

);

drop table if exists account_holder;
create table account_holder(
       id integer primary key autoincrement,
       email text not null,
       password text not null,
       username text not null,
       phone integer not null,
       picture BLOB not null
);
