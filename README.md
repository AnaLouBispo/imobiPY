# Sistema de Orçamento de Aluguel - Imobiliária R.M

## Descrição

Este projeto foi desenvolvido em Python com o objetivo de automatizar a geração de orçamentos de aluguel para uma imobiliária.

O sistema permite calcular o valor mensal do aluguel de apartamentos, casas e estúdios, aplicando regras específicas para cada tipo de imóvel, além de calcular o parcelamento do contrato imobiliário e gerar um arquivo CSV com as parcelas do orçamento.

## Funcionalidades

* Cadastro de orçamento para apartamentos, casas e estúdios.
* Cálculo automático do valor do aluguel.
* Acréscimo para imóveis com 2 quartos.
* Acréscimo de garagem para apartamentos e casas.
* Controle de vagas para estúdios.
* Desconto de 5% para apartamentos sem crianças.
* Parcelamento do contrato imobiliário em até 5 vezes.
* Geração de arquivo CSV com as 12 parcelas do orçamento.

## Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Biblioteca CSV

## Estrutura do Projeto

```text
orcamento-imobiliaria-rm/
│
├── orcamento_imobiliaria.py
├── parcelas.csv
├── README.md
└── Fluxograma.pdf
```

## Classes Utilizadas

### Imovel

Classe base do sistema.

### Apartamento

Responsável pelo cálculo do aluguel de apartamentos.

### Casa

Responsável pelo cálculo do aluguel de casas.

### Estudio

Responsável pelo cálculo do aluguel de estúdios.

## Como Executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python orcamento_imobiliaria.py
```

3. Preencha os dados solicitados pelo sistema.
4. O orçamento será exibido na tela.
5. Um arquivo chamado `parcelas.csv` será gerado automaticamente.

## Objetivo Acadêmico

Este projeto foi desenvolvido para a disciplina de Algoritmos, Técnicas e Introdução à Orientação a Objetos, com o objetivo de aplicar conceitos de lógica de programação, orientação a objetos, entrada e saída de dados e manipulação de arquivos.

## Autor

Ana Beatriz
