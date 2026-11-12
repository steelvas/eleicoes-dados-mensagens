"""Simulação didática. Não acessa contatos nem envia mensagens."""

def avaliar_origem(origem, comprada):
    if comprada or origem == "clientes_de_empresa":
        return "BLOQUEAR: não importar essa base"
    return "PENDENTE: verificar finalidade, base legal e direitos dos titulares"


if __name__ == "__main__":
    print(avaliar_origem("clientes_de_empresa", False))
    assert avaliar_origem("clientes_de_empresa", False).startswith("BLOQUEAR")
    assert avaliar_origem("cadastro_proprio", False).startswith("PENDENTE")
