--dbext:profile=sqlite

drop table if exists place;
create table place (
    id      int            auto_increment,
    url     varchar(20),
    name    varchar(40),
    img     varchar(60)
);

drop table if exists story;
create table story (
    id      int             auto_increment,
    p_id    int,
    content varchar(1000),
    avt     varchar(60)
);
