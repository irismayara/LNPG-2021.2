dicionario = {}
texto = ""

while true do
    entrada = io.read()

    if(entrada ~= "-1") then 
        texto = texto .. " " .. entrada
    else
        texto = string.lower(texto)

        for p in string.gmatch(texto, "%a+") do -- ola12-mundo0de[
            table.insert(dicionario, p)
        end

        table.sort(dicionario)

        palavra = ""
        qtd = 0

        for i, value in ipairs(dicionario) do -- am am beer clash 
            if(value == palavra) then
                qtd = qtd + 1
            else
                if(palavra ~= "") then
                    print(palavra, qtd)
                end
                palavra = value
                qtd = 1
            end   
        end  
        print(palavra, qtd) 
        break
    end 
end