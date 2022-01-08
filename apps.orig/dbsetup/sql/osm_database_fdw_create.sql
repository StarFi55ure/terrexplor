
create server if not exists {{ database }}
    foreign data wrapper postgres_fdw options (host 'localhost', dbname '{{database}}', port '5432');

create user mapping if not exists for terrexplor 
    server {{ database }} options (user 'terrexplor', password 'terrexplor');

create schema if not exists {{database}};

import foreign schema public 
    from server {{ database }}
    into {{ database }};

