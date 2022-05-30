dado = {1,2,3,4,5,6}
tabuleiro = {}

ultima_casa = tonumber(io.read())

casa = 1
jogadas = 0

while casa ~= ultima_casa do
    for i in ipairs(dado) do
        casa = casa + i 
        jogadas = jogadas + 1
        if(casa > ultima_casa) then
            casa = casa - ultima_casa
        end
        if(i == 6 or casa == ultima_casa)then
            break
        end
    end
end
print(jogadas)