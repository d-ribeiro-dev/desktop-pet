
<div align="center">

# 🤖 Desktop Pet

### Pequeno no tamanho, grande nas possibilidades.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-8B9DC3?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![Version](https://img.shields.io/badge/Versão-0.1-C8A2C8)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-F4C2C2)
![Offline](https://img.shields.io/badge/Offline-100%25-A8D5BA)

*Um pequeno companheiro virtual para grandes jornadas de aprendizado.*

</div>

---

# 📖 Diário de Desenvolvimento

## Parte 01 — Da ideia ao primeiro protótipo

| 📌 Informação | Detalhes |
|---|---|
| 📅 Início | 24 de novembro de 2026 |
| 🚧 Status | Em desenvolvimento |
| 🏷️ Versão | 0.1 — Prova de conceito |
| 🎯 Natureza | Projeto autoral, experimental e educacional |

---

## 💡 1. Como surgiu a ideia

Durante meus estudos de programação e minhas pesquisas sobre sistemas embarcados, investiguei repositórios relacionados a projetos tecnológicos, buscando compreender como dispositivos com recursos computacionais limitados conseguem executar animações e comportamentos interativos.

O que despertou minha atenção foi a possibilidade de produzir personagens animados utilizando códigos compactos, sem depender necessariamente de grandes quantidades de imagens, GIFs ou recursos gráficos externos.

A partir dessa observação, comecei a questionar:

> **Se uma pequena placa ESP32 consegue executar um personagem animado em sua própria tela, por que não utilizar esse mesmo princípio para desenvolver um companheiro virtual para computadores?**

Minha intenção era desenvolver uma aplicação em Python que fosse leve, interativa e capaz de funcionar em uma pequena área da tela, sem comprometer o desempenho do computador.

---

## 🎯 2. A proposta inicial

Imaginei um personagem que permanecesse na área de trabalho enquanto utilizo normalmente o computador.

Mais do que uma animação decorativa, ele deveria apresentar comportamentos próprios, reagir às minhas interações e, futuramente, auxiliar nas atividades do cotidiano.

As primeiras funcionalidades idealizadas foram:

- 👀 Piscar, respirar e movimentar os olhos.
- 🖱️ Acompanhar o cursor do mouse.
- 💤 Dormir durante períodos de inatividade.
- ⏱️ Auxiliar em sessões de concentração
- 🤖 Possibilitar uma futura integração com o Eme, meu projeto de assistente pessoal.

---

## 🔍 3. Investigação e viabilidade técnica

Para avaliar a viabilidade da proposta, compartilhei com a inteligência artificial a ideia e detalhes estudados durante minhas pesquisas.

O objetivo era compreender a engenharia utilizada para produzir animações em dispositivos de baixo consumo e investigar como esses conceitos poderiam ser aplicados em um ambiente desktop.

Foram consideradas diferentes tecnologias:

| Tecnologia | Ambiente |
|---|---|
| C++ | Win32 |
| Python | PySide6 |
| Python | Tkinter |

A escolha inicial foi **Python com Tkinter**, considerando a simplicidade, a facilidade de manutenção, a possibilidade de reduzir dependências externas e minha própria trajetória de aprendizado em Python.

O projeto passou a adotar uma implementação própria, com desenhos geométricos gerados por código e uma lógica de funcionamento voltada ao ambiente desktop.

---

## 🛠️ 4. Desenvolvimento do primeiro protótipo — v0.1

A primeira versão foi desenvolvida como uma prova de conceito.

O personagem escolhido foi um pequeno robô com formas arredondadas, corpo compacto, rosto digital expressivo e uma antena.

A proposta visual buscou transmitir simpatia e simplicidade, mantendo uma estrutura que pudesse ser animada programaticamente.

### ✨ Funcionalidades implementadas

- [x] Janela independente de 240 × 240 pixels.
- [x] Fundo transparente no Windows.
- [x] Possibilidade de movimentação pela área de trabalho.
- [x] Animação de respiração.
- [x] Movimento dos olhos.
- [x] Acompanhamento do cursor.
- [x] Comportamento de sono por inatividade do mouse.
- [x] Temporizador Pomodoro.
- [x] Menu de interação.

### 📂 Estrutura do projeto

A estrutura inicial foi organizada em quatro arquivos:

| Arquivo | Responsabilidade |
|---|---|
| `pet.py` | Interface gráfica e animações |
| `model.py` | Lógica do temporizador |
| `test_model.py` | Testes automatizados |
| `README.md` | Documentação inicial |

### ▶️ Como executar

É necessário ter o Python instalado com suporte ao Tkinter.

Abra o terminal na pasta do projeto e execute:

```bash
python pet.py
```

### 🎮 Controles

| Interação | Ação |
|---|---|
| Botão esquerdo + arrastar | Movimentar o robô |
| Botão direito | Abrir o menu |
| Tecla Esc | Encerrar a aplicação |

### 🧪 Testes

Para executar os testes automatizados:

```bash
python -m unittest test_model.py -v
```

A validação do desempenho e do consumo de recursos permanece como parte do processo de desenvolvimento.

---

### 📋 Resultados dos testes — 24/11/2026

Antes de concluir a primeira versão, realizei testes
funcionais, automatizados e de desempenho para verificar
o comportamento do protótipo em condições reais de uso.

| Validação | Resultado |
|---|---|
| Testes funcionais manuais | ✅ 12/12 aprovados |
| Testes automatizados | ✅ 3/3 aprovados |
| Verificação de sintaxe | ✅ Sem erros |
| Funcionamento offline | ✅ Validado |
| Ciclo completo do Pomodoro | ✅ Validado |
| Execução durante 30 minutos | ✅ Concluída |

### 💻 Ambiente de testes

- **Sistema operacional:** Windows 10
- **Processador:** Intel Core i5-3330
- **Memória RAM:** 8 GB
- **Armazenamento:** SSD

### 📊 Avaliação de desempenho

Para avaliar o impacto do Desktop Pet no computador,
realizei medições utilizando o Gerenciador de Tarefas
do Windows, antes e durante a execução do aplicativo.

| Cenário | CPU total | CPU do Pet | RAM do Pet |
|---|---:|---:|---:|
| Sem o Desktop Pet | 1–2% | — | — |
| Pet acordado | 3–4% | 0% | 44,2 MB |
| Pet dormindo | 2% | 0% | 44,2 MB |
| Pomodoro ativo | 3% | 0% | 44,2 MB |

> As medições representam leituras pontuais realizadas
> durante os testes, não médias de consumo contínuo.

### 🍃 Eficiência e consumo de recursos

Um dos objetivos iniciais era desenvolver uma aplicação
capaz de funcionar com baixo consumo de recursos.

- 🎯 Meta inicial de memória: abaixo de 50 MB.
- ✅ Consumo observado: 44,2 MB.
- ⚡ Uso de energia classificado como muito baixo.
- 🌐 Funcionamento com o Wi-Fi desconectado.
- 📦 Sem necessidade de bibliotecas externas.
- 🎨 Animações produzidas diretamente por código.

Durante o modo de sono, a frequência nominal de
atualização das animações é reduzida de aproximadamente
25 para 10 quadros por segundo, buscando diminuir
a necessidade de processamento.

### 🏁 Conclusão da primeira versão

Os resultados obtidos foram satisfatórios para o
objetivo desta primeira prova de conceito.

A validação permitiu demonstrar que é possível criar
um pequeno companheiro virtual interativo utilizando
Python e Tkinter, sem depender de imagens externas,
GIFs ou conexão com a internet para seu funcionamento.

Por se tratar de uma versão experimental, análises
mais aprofundadas de desempenho, estabilidade e
gerenciamento de memória ficam para etapas futuras.

**Status da v0.1: concluída e validada dentro do escopo proposto.**

---


## 🌱 5. Evolução da ideia durante o desenvolvimento

Ao observar o primeiro protótipo, percebi que o personagem poderia oferecer possibilidades muito mais interessantes do que simplesmente permanecer animado na tela.

Surgiram novas ideias relacionadas à personalidade, à interação e à capacidade de reagir aos acontecimentos do computador.

Mas isso fica para a próxima atualização... 👀

---

<div align="center">

### 🚧 Uma pequena ideia em constante evolução.

Este projeto faz parte da minha jornada de aprendizado,
pesquisa e experimentação tecnológica.

**Continua...**

♡ Desenvolvido com curiosidade, dedicação e criatividade.

</div>

---

### 🔒 Direitos autorais

Copyright © 2026 — Dinara Ribeiro.

Todos os direitos reservados.

Este repositório público tem finalidade de apresentação,
documentação e demonstração do projeto.

A reprodução, modificação, redistribuição ou exploração
comercial do código não é autorizada sem consentimento
prévio da titular, ressalvadas as permissões legais
e os termos aplicáveis do GitHub.
