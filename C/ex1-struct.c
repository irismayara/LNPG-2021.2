struct pessoa
{
    char nome[10];
    char cpf[10];
    int idade;
    float peso;
};

float calc_media(float soma_pesos){
    return soma_pesos/5;
}

int main(int argc, char const *argv[])
{
    struct pessoa p[5];
    float soma_pesos = 0.0f;
    for(int i = 0; i < 5; i++) {
        scanf("%s", p[i].nome);
        scanf("%s", p[i].cpf);
        scanf("%d", &p[i].idade);
        scanf("%f", &p[i].peso);
        soma_pesos += p[i].peso;
    }
    float media = calc_media(soma_pesos);

    for(int i = 0; i < 5; i++) {
        if(p[i].peso > media){
            printf(p[i].nome, p[i].cpf, "\n");
        }
    }

    return 0;
}