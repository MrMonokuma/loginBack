/*Crear usuario*/
delimiter $$
create procedure crearUsuario (
    in _username varchar(50), 
    in _password varchar(200)
)
begin
insert into usuarios (username,contraseña) 
values(_username,sha(_password));
end $$