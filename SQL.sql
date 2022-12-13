drop database if exists Cliente;
create database Cliente;
Use Cliente;

select * from Clientes;


create table Clientes (
cliente_id int auto_increment primary key,
cpf        char(11)              not null,
nome       varchar(60)           not null,
idade      varchar(3)            not null,
logradouro varchar(100)          not null,
numero     varchar(8)            not null,
bairro     varchar(30)           not null,
estado     char(2)               not null,
ddd        varchar(3)            not null,
telefone   varchar(9)            not null,
email      varchar(40)           not null
);