# Eleições: a base de clientes pode virar lista de campanha?

Uma loja possui telefones de clientes. Alguém propõe entregar a lista a uma campanha.

```python
origem = "clientes_da_loja"

if origem == "clientes_da_loja":
    print("BLOQUEAR a importação")
else:
    print("Examinar origem, finalidade e base legal")
```

1. **Código:** a origem da lista aciona um bloqueio. O programa não afirma que qualquer outra lista seja lícita.
2. **Resultado:** ter acesso aos números para vender produtos não autoriza usá-los para propaganda eleitoral.
3. **Regra:** pessoas jurídicas não podem utilizar, doar ou ceder dados pessoais de clientes em favor de candidaturas ou partidos. A venda de cadastros e bancos de dados pessoais também é proibida.
4. **O que fazer:** antes de importar contatos, identificar quem os coletou, para quê, com qual fundamento e quem terá acesso. Mensagens de campanha precisam identificar o remetente e oferecer descadastramento, a ser atendido em até 48 horas.

**Papel do advogado:** impedir que a facilidade técnica de copiar uma planilha seja confundida com autorização jurídica para reutilizá-la.

Fonte: [Resolução TSE nº 23.610/2019, arts. 31 e 33, com alterações posteriores](https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019).

## Executar o exemplo

Com Python 3 instalado, rode `python exemplo.py`. O arquivo usa apenas dados fictícios e inclui verificações simples com `assert`. Ele não substitui a análise jurídica nem executa ações externas.


*Exemplo didático com dados fictícios. A análise real depende da origem, finalidade e operação concreta.*
