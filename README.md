# digit_kohonen
Reconhecimento de dígitos numéricos usando rede neural de Kohonen

### Entrada
Os arquivos de entrada se encontram na pasta `digit_kohonen/input/`
|     Nome do Arquivo        | Descrição          | Instâncias |
|:--------------------------:|--------------------|------------|
| `optdigits-orig.tra.in`    | Training           | 1934       |
| `optdigits-orig.cv.in`     | Validation         | 946        |
| `optdigits-orig.wdep.in`   | Writer-dependent   | 943        |
| `optdigits-orig.windep.in` | Writer-independent | 1797       |

Como temos vários parâmetros que podem influenciar nos resultados, os mesmos são controlados dentro do código.
as variáveis de controle são:
```python
carregar_treino = "output/toda-entrada.tra.out"         # Arquivo de treino armazenado anteriormente
treinar         = "input/optdigits-orig.tra.in"         # Arquivo de entrada para treinar
teste_de_acerto = "input/optdigits-orig.tra.in"         # Arquivo de entrada para testar taxa de acerto
teste_de_treino = "input/optdigits-orig.cv.in"          # Arquivo de entrada gerar a grade de reconhecimento
n_iter          = 5                                     # Quantidade de iterações de treino

CARREGAR_TREINO                 = False                 # Flags de controle
TREINAR                         = True
ARMAZENAR                       = False
GERAR_GRADE_RECONHECIMENTO      = True
CALCULAR_TAXA_ACERTOS           = True
DESENHAR_GRADE_MESCLADA         = True
DESENHAR_GRADE_RECONHECIMENTO   = True
GERAR_LOG_RESULTADO             = True

GRID_SIZE_I                     = 8                 # Quantidade de linhas na grade de neurônios
GRID_SIZE_J                     = 8                 # Quantidade de colunas no arquivo de entrada

ALPHA_INICIAL                   = 0.1               # Valor inicial do alpha
DECRE_ALPHA                     = 0.00009           # Quantia do decremento alpha por época

SIGMA_INICIAL                   = 2                 # Valor inicial de sigma
DECRE_SIGMA                     = 0.0015            # Quantia do decremento de sigma por época
```
### Dependências
> Atenção, para o programa funcionar se faz necessários respeitar as dependências abaixo.
* Python3 instalado e atualizado
* biblioteca numpy instalada e atualizada
* biblioteca pillow instalada e atualizada
>Antes de executar o programa, verificar o arquivo `desenho.py`, quando utilizado o método `ImageFont.truetype`, como parâmetro precisa ter um endereço de fonte válido.
### Compilando e Executando
>Atenção: Os comandos para executar a implementação precisam ser feitos dentro do diretório `digit_kohonen/`.
Para Ubunto e distros que usam como padrão o python2:

    $ python3 Main.py
>ou

    $ make
>Para Arch Linux e distros que usam como padrão o python3:

    $ python Main.py
    
### Saídas:
> Como possibilidades de saída podemos salvar a grade de neurônios em arquivo, basta ter a flag ARMAZENAR ativada.
Também é possível gerar um arquivo de Log que guarda alguns parâmetros de controle e a taxa de acerto da rede.
E são geradas duas imagens: A mesclada mostrando dentro de cada neurônio uma lista de vitórias com o número respectivo da classe na qual foi vencedor, e uma imagem com cada neurônio representando uma classe, que o numero com qual teve mais vitórias.
Todas as saídas são encontradas no diretório `digit_kohonen/output/`