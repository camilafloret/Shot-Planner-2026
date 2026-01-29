# Steel Bulls Shot Planner 2026 - REBUILT™

O **Shot Planner 2026** é uma ferramenta de simulação física avançada adaptada para a equipe **Steel Bulls (FRC 9460)**. Ela permite analisar e planejar trajetórias de lançamento para o desafio da temporada 2026, ajudando a identificar as configurações ideais de velocidade, ângulo e posicionamento do robô.

## 🚀 Como Funciona

O sistema combina um motor de física em Python com uma interface interativa em tempo real para fornecer feedback instantâneo sobre a viabilidade de um arremesso.

### 🧠 O Motor de Física (`physics_engine.py`)

O simulador utiliza as equações cinemáticas de movimento de projéteis para prever a trajetória da "Cargo" (bola):

1.  **Trajetória Dinâmica:** Calcula a posição $(x, y)$ em função do tempo, considerando a gravidade constante ($9.81 m/s^2$).
2.  **Condição de Acerto (Make):** Um arremesso é considerado válido se, ao atingir a altura do alvo (`rim_height`), a coordenada $x$ estiver dentro dos limites do aro, levando em conta o raio da bola (`cargo_radius`). Além disso, a bola deve estar em trajetória descendente ($v_y < 0$).
3.  **Cálculo de Margem de Erro (Budget):**
    *   **Velocity Budget:** Determina a faixa de velocidade (mínima e máxima) que resultaria em acerto para o ângulo e posição atuais.
    *   **Position Budget:** Calcula a tolerância de posicionamento no campo (em metros) para a velocidade e ângulo configurados.
4.  **Heatmap de Probabilidade:** Gera um mapa de calor no campo baseado na "Área de Sucesso" no espaço de configuração. Zonas mais claras (amarelas) indicam locais onde é mais fácil acertar o alvo (maior tolerância a erros).

### 🖥️ Interface de Controle (`webapp/`)

*   **Painel de Trajetória (Esquerda):** Permite arrastar o robô (ponto branco) pelo campo. O rastro muda de cor (verde/vermelho) indicando sucesso ou erro.
*   **Configuração do Shooter (Polar Plot):** Um gráfico polar interativo onde o raio representa a **velocidade** e o ângulo representa a **inclinação do shooter**. A zona sombreada em vermelho mostra todas as combinações de (velocidade/ângulo) que resultam em ponto.
*   **Margem de Velocidade (Bottom Right):** Mostra graficamente quão "folgado" está o seu arremesso. Se o ponto branco estiver no centro da zona colorida, você tem a margem máxima para variações no motor.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3 + [Flask](https://flask.palletsprojects.com/)
-   **Processamento Matemático:** [NumPy](https://numpy.org/) e [SciPy](https://scipy.org/) (para integrações e otimizações)
-   **Frontend:** JavaScript (ES6+), HTML5, CSS3
-   **Gráficos:** [Plotly.js](https://plotly.com/javascript/) (para renderização de alta performance dos plots)
-   **Estilização:** CSS Premium com Glassmorphism e Tailwind CSS para estrutura responsiva.

## ⚙️ Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes)

### Passo a Passo

1.  **Instale as dependências:**
    ```bash
    pip install flask numpy scipy
    ```

2.  **Inicie o servidor:**
    ```bash
    python webapp/app.py
    ```

3.  **Acesse no navegador:**
    Abra `http://localhost:5000`

---

## 👥 Créditos

Este projeto foi desenvolvido por:
- **Skyehawk** - [GitHub](https://github.com/Skyehawk/)

Adapatado por:
- **Camila Floret** - [GitHub](https://github.com/camilafloret)
