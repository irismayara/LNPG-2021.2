ultima_casa = tonumber(io.read())

casa_atual = 1
jogadas = 0

while casa_atual ~= ultima_casa do
    for i = 1, 6 do
        casa_atual = casa_atual + i 
        jogadas = jogadas + 1
        if(casa_atual > ultima_casa) then
            casa_atual = casa_atual - ultima_casa
        end
        if(i == 6 or casa_atual == ultima_casa)then
            break
        end
    end
end
print(jogadas)