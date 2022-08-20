# TIR (TAXA INTERNA DE RETORNO)

TIR é a fórmula utilizada para encontrar a taxa de retorno de acordo com o fluxo de caixa
de uma carteira dado seus investimentos realizados e parcelas recebidas ou a receber.

No Python utilizamos a biblioteca `numpy_financial` onde encontra-se o método IRR, para obtermos o valor da TIR com esse método é necessário passar um array contendo os valores de investimentos (como um débito) e os valores das parcelas (como um crédito).
Esse array deve estar nas seguintes condições:
 - Todo valor de investimento deve entrar como um valor negativo;
 - Todo valor de parcela deve entrar como um valor positivo;
 - O fluxo de caixa deve estar ordenado por data da movimentação, quando investimento pela data de criação `created_at` e quando parcela pela data de vencimento `due_date`;
 - O fluxo de caixa deve ser dia a dia da carteira, iniciando na data do primeiro investimento e finalizando no recebimento da última parcela;
 - Dias que não tem recebimento nem investimento devem ficar com valor 0.0;
 - Em dias que existirem mais de uma movimentação os valores devem ser somados;

Referência:
https://warren.com.br/magazine/taxa-interna-de-retorno-tir/

Como Intalar: 
Utilizando: Python 3.9.2
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install numpy-financial

No Terminal bash rodar: 
Python main.py


