--RDB DESIGN--
    -- 1.multiple kinds of one item_id turnInto multiple rows of same item_id
    -- 2.key/item_id is topic of row, rest of row describe key/item_id
    -- 3.non-key columns do not descripbe non-key columns, they only describe the key/item_id column
    -- 4.columns should not imply non-existing relations
    -- http://www.bkent.net/Doc/simple5.htm

--CREATE--
create table quest (
    quest_id serial primary key, -- serial is incremental in Postgresql
    quest_name text,
    description text,
    create_datetime date
    );
create table task (
    task_id serial primary key ,
    quest_id integer references quest(quest_id), -- ForeignKey <integer> check quest_id exist in quest, a task is part of a quest
    race_id text references task_type(task_type_id), -- FK to task type
    task_name text,
    description text
    );
create table task_type (
    task_type_id text primary key,  -- repeatable, onetime, optional, etc
    description text
    );
create table postal_places (
    postal_code text,
    country text,
    place_name text,
    primary key(place_name, species) -- multiple PK
    );

--SELECT--
select name from animals
  where (not species = 'gorilla')
  and (not name = 'Max')
  ;
select name from animals
  where not( species = 'gorilla' or name = 'Max')
  ;
select name from animals
  where ( species != 'gorilla')
  and ( name != 'Max')
  ;
select name from animals
  where (species = 'llama')
  and (birthdate >= '1995-01-01' )
  and (birthdate <= '1998-12-31')
  ;


--WHERE--
select max(name) from animals
  ; # Zoe
select * from animals
  limit 10
  ;
select * from animals
  where species = 'orangutan'
  order by birthdate
  ;
select name from animals
  where species = 'orangutan'
  order by birthdate desc
  ;
select name, birthdate from animals
  order by name
  limit 10 offset 20
  ;


--GROUP BY--
select species, min(birthdate) from animals
  group by species
  ; # min(birthday) for each species
select name, count(*) as num from animals
  group by name
  order by num desc
  limit 5
  ; # top 5 frequent animal names and count
select species, count(1) as c
  from animals
  group by species
  order by c desc
  ; # all species sort by count


--INSERT--
insert into animals
  values('Test','opossum','2014-01-01')
  ;
insert into animals (name, species, birthday)
  values('Test','opossum','2014-01-01')
  ;


--JOIN--
select products.name, products.sku, count(sales.sku) as num -- count only in sales
    from products left join sales -- left (outer) join 2nd common: every row in products table, even the ones not in sales table
    on products.sku = sales.sku
    group by products.sku;
select t1.id t2.id
    from building as t1, building as t2 -- self join
    where t1.room = t2.room
    and t1.id < t2.id -- de-dup
    ;
select T.thing, S.stuff
  from T join S -- (inner) join, most common
  on T.target = S.match
  ;
select T.thing, S.stuff
  from T,S
  where T.target = S.match
  ;
select name
  from animals,diet
  where animals.species = diet.species
  and food = 'fish'
  ;


--HAVING-- focus on result while where focus on source
select food, count(1) as c
  from animals,diet
  where animals.species = diet.species
  group by food
  having c = 1
  ; # which animal only have one food


--UPDATE--
update posts
    set content = 'cheese'
    where content LIKE '%test%'
    ;


--DELETE--
DELETE FROM posts
    WHERE content LIKE 'cheese'
    ;


--SUBQUERY--
select avg(bigscore) -- avg score of highest scores from each team
    from
    (
    select max(score) as bigscore
        from mooseball
        group by team
    ) as maxes -- name required even not used
    ;
select name, weight
    from player, -- joined with 1x1 subq result, apply av to each row
        (
        select avg(weight) as av -- calculate av to be used by outer query
            from players
        )as subq -- not used name
    where weight < av -- compare to av calculated from subq
    ;


--VIEW-- rows in sub-views of larger source tables can be updated/deleted
create view course_size as
    select course_id, count(*) as c
    from enrollment
    group by course_id
    ;