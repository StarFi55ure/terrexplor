/**
  Basic user and permissions tables

 */

-- initialize database extensions
create extension pgcrypto;
create extension "uuid-ossp";

create table tbluser (
    userid          uuid primary key default uuid_generate_v4(),
    email           text not null unique,
    username        text not null unique,
    firstname       text not null,
    lastname        text not null,
    password        text not null,

    datecreated     timestamptz default now(),
    active          boolean default true
);

create table tblrole (
    roleid          uuid primary key default uuid_generate_v4(),
    rolename        text not null,
    datecreated     timestamptz default now(),
    active          boolean default true
);

create table tbluser_roles (
    userid          uuid references tbluser(userid),
    roleid          uuid references tblrole(roleid),

    unique(userid, roleid)
);

create table tblpermission (
    permissionid    uuid primary key default uuid_generate_v4(),
    permissionname  text not null,
    description     text,

    datecreated     timestamptz default now(),
    active          boolean default true
);

create table tbluser_permissions (
    userid          uuid references tbluser(userid),
    permissionid    uuid references tblpermission(permissionid),

    unique(userid, permissionid)
);

create table tblrole_permissions (
    roleid          uuid references tblrole(roleid),
    permissionid    uuid references tblpermission(permissionid),

    unique (roleid, permissionid)
);

-- basic reference data
insert into tblpermission(permissionname) values('root');

insert into tblrole(rolename) values ('root');

insert into tblrole_permissions(roleid, permissionid)
values((select roleid from tblrole where rolename = 'root'),
       (select permissionid from tblpermission where permissionname = 'root'));

insert into tbluser(email, username, firstname, lastname, password)
values('', 'admin', 'Admin', 'User', 'admin');

insert into tbluser_roles(userid, roleid)
values((select userid from tbluser where username = 'admin'),
       (select roleid from tblrole where rolename = 'root'));
