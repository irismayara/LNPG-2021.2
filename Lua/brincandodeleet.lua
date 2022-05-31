function isEmpty(string)
    if(string == "") then
        return true
    else
        return false
    end
end

function hasNumber(string)
    if(string.match(string, "%d")) then -- ola12 mundo
        return true
    else
        return false
    end
end

function codificar(string, codigo)
    substituicoes = 0
    
    for key, value in pairs(codigo) do
        string, sub = string.gsub(string, key, value)
        substituicoes = substituicoes + sub
    end

    return string.reverse(string), substituicoes    
end

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

string = io.read()
substituicoes = 0

if(isEmpty(string)) then
    print("Vazio.")
elseif(hasNumber(string)) then
    print("Numeros.")
else
    leet, substituicoes = codificar(string, codigo)
    print(leet)
end
    print(substituicoes)