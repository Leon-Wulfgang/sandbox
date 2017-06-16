#CREATE#
create table animals (
       name text,
       species text,
       birthdate date);
create table diet (
       species text,
       food text);
create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text);
create table ordernames (
       t_order text,
       name text);


#SELECT#
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


#WHERE#
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


#GROUP BY#
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


#INSERT#
insert into animals
  values('Test','opossum','2014-01-01')
  ;
insert into animals (name, species, birthday)
  values('Test','opossum','2014-01-01')
  ;


#JOIN#
select T.thing, S.stuff
  from T join S
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


#HAVING# focus on result while where focus on source
select food, count(1) as c
  from animals,diet
  where animals.species = diet.species
  group by food
  having c = 1
  ; # which animal only have one food


#UPDATE#
update posts
    set content = 'cheese'
    where content LIKE '%test%'
    ;


#DELETE#
DELETE FROM posts
    WHERE content LIKE 'cheese'
    ;