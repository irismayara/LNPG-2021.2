dicionario = {}
palavras = {}
texto = ""

while true do
    entrada = io.read()

    if(entrada == "-1") then  
        texto = string.lower(texto)

        for palavra in string.gmatch(texto, "%a+") do
            table.insert(palavras, palavra)
        end

        table.sort(palavras)

        palavra = ""
        qtd = 0

        for i, value in pairs(palavras) do
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
    else
        texto = texto .. " " .. entrada
    end 
end