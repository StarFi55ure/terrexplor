/**
  Add basic asset tables and image tables.

 */


create table tbldatablock (
    datablockid     uuid primary key default uuid_generate_v4(),
    md5             text not null unique,
    size            bigint, -- bytes
    datecreated     timestamptz default now(),
    active          boolean default true
);

create table tblmediatype (
    mediatypeid     uuid primary key default uuid_generate_v4(),
    mediatypename   text not null,
    datecreated     timestamptz default now(),
    active          boolean default true
);

insert into tblmediatype(mediatypename) values('IMAGE');
insert into tblmediatype(mediatypename) values('VIDEO');
insert into tblmediatype(mediatypename) values('THUMB_IMAGE');
insert into tblmediatype(mediatypename) values('THUMB_VIDEO');

create table tblmedia (
    mediaid         uuid primary key default uuid_generate_v4(),
    name            text not null,
    description     text,
    filename        text not null,
    mimetype        text,
    datablockid     uuid references tbldatablock(datablockid),
    mediatypeid     uuid references tblmediatype(mediatypeid),
    createdby       uuid,

    datecreated     timestamptz default now(),
    active          boolean default true
);

create table tblmediameta (
    mediametaid     uuid primary key default uuid_generate_v4(),
    mediaid         uuid references tblmedia(mediaid),
    data            jsonb,

    datecreated     timestamptz default now(),
    active          boolean default true
);


-- create table tblasset (
--     assetid         uuid primary key default uuid_generate_v4(),
--     name            text not null,
--     description     text,
--     filename        text not null,
--     mimetype        text,
--     datablockid     uuid references tbldatablock(datablockid),
--
--     createdby       uuid, -- user that created the asset
--
--     datecreated     timestamptz default now(),
--     active          boolean default true
-- );
--
-- create table tblimagemeta (
--     imagemetaid     uuid primary key default uuid_generate_v4(),
--     exifdata        jsonb,
--
--     datecreated     timestamptz default now(),
--     active          boolean default true
-- )
