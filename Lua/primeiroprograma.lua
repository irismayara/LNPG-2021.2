--[==[
-- ENTRADA
n = io.read()
print(type(n)) -- string

n = tonumber(io.read())
print(type(n)) -- number

-- SAÍDA 
print("Olá, mundo!")

print 
    "Olá, mundo"
    em várias
    linhas!


print "Olá, mundo! Sem parênteses"

-- VARIAVEIS
nome = "Airton Sena" -- variavel global

local nome = "Airton Sena" -- variável local

print(Nome)

-- TABELAS
tabela = {}
tabela["p1"] = "Oi"

print(tabela["p1"])

print(type(tabela)) -- table


lista = {x="ola mundo", y="a", z="b"}
t = "ola mundo"

string, sub1 = string.gsub("stringa", "a", "@")

string, sub = string.gsub("stringa", "s", "5")

string = "marcelo"

codigo = {
    a = "@",
    A = "@",
    e = "3",
    E = "3",
    i = "1",
    I = "1",
    o = "0",
    O = "0",
    t = "7",
    T = "7",
    s = "5",
    S = "5"
}

string = "ola"

-- print(string)

nome = "Airton"
idade = 15
altura = 1.75

print("Meu nome eh " .. nome .. ", tenho " .. idade ..    " anos e " .. altura .. " de altura.")

print(string.format("Meu nome eh %s, tenho %d anos e %.2f de altura.", nome, idade, altura))


-- COMENTARIO DE LINHA

--[[
    COMENTARIO DE BLOCO
]]

a = 65
b = 48;
a = 65 b = 48
a = 65; b = 48


if(true) then
    -- do this
end

if(true) then
    -- do this
else
    -- do that
end

n = -1
if(n < 0) then
    n = 0
elseif(n > 100) then
    n = 100
else
    
end

-- imprimindo de 1 a 10
for i = 1, 10, 1 do
    print(i)
end

-- percorrendo tabela de índices numericos
t = {"PHP", "C", "Lua", "Java"}

for key, value in ipairs(t) do -- (1,t[1]), (2,t[2]), ...
    print(key, value)
end

-- percorrendo tabela
t = {nome = "Airton", idade = "15"}

for key, value in pairs(t) do
    print(key, value)
end

-- WHILE
-- imprimindo de 10 a 1
numero = 10
while (numero > 0) do
    print(numero)
    numero = numero - 1
end
]==]

-- REPEAT UNTIL

-- imprimindo números pares até 10
numero = 2
repeat
    print(numero)
    numero = numero + 2
until (numero > 10)