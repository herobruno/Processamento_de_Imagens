# Detecção de Carros Vermelhos em Imagens

## Descrição

Este projeto aplica técnicas de processamento de imagens para detectar carros vermelhos em imagens de estacionamentos ou vias urbanas. A detecção é realizada com a conversão da imagem para o espaço de cores HSV e aplicação de máscaras específicas baseadas em tonalidades de cor. Operações morfológicas são então aplicadas para melhorar a segmentação, e contornos são extraídos para destacar e contar os objetos detectados. O sistema se mostrou eficaz na identificação de veículos vermelhos, mesmo em ambientes com condições de iluminação variadas.

## Objetivo

O objetivo deste projeto é desenvolver uma aplicação simples e eficiente de processamento de imagens, utilizando a biblioteca OpenCV, para identificar e contar carros vermelhos em imagens estáticas. A aplicação usa segmentação por cor, operações morfológicas e detecção de contornos para realizar essa tarefa.

## Tecnologias Utilizadas

- **OpenCV**: Biblioteca de visão computacional para processamento de imagens.
- **Python**: Linguagem de programação utilizada para implementar a solução.
- **NumPy** para manipulação eficiente de arrays e matrizes, o que facilitou o processo de criação das máscaras e manipulação das imagens.

## Funcionalidades

- **Conversão de Imagem para HSV**: A imagem é convertida do espaço de cores BGR para HSV para melhorar a segmentação por cor.
- **Segmentação por Cor**: Máscaras são aplicadas para isolar regiões vermelhas na imagem.
- **Operações Morfológicas**: A operação "close" é aplicada para unir regiões próximas, melhorando a segmentação dos carros.
- **Detecção de Contornos**: Contornos das regiões detectadas são extraídos para identificar e contar os veículos.
- **Agrupamento de Caixas Delimitadoras**: Caixas sobrepostas ou próximas são agrupadas para evitar múltiplas detecções do mesmo carro.
- **Contagem de Veículos**: O número total de veículos detectados é exibido na imagem e no terminal.

## Estrutura do Projeto

- `index.py`: Arquivo principal que executa o processamento de imagens.


## Como Executar

Para executar o projeto, basta rodar o script principal:

```bash
python index.py
```

## Metodologia

1. **Pré-processamento e Conversão de Cor**  
   A imagem é redimensionada para 800x600 pixels e convertida do espaço de cores BGR para HSV, pois o HSV oferece uma melhor separação das cores, facilitando a segmentação.

2. **Segmentação por Cor**  
   Foram definidas duas faixas de tonalidades vermelhas no espaço HSV. A soma das máscaras geradas por essas faixas permite uma segmentação mais robusta dos carros vermelhos.

3. **Operações Morfológicas**  
   Uma operação morfológica de fechamento (close) é aplicada com um kernel grande (25x25) para unir regiões próximas pertencentes ao mesmo veículo.

4. **Detecção de Contornos e Filtragem por Área**  
   Utilizando a função `findContours` do OpenCV, são detectadas as regiões contornadas. Somente os contornos com área entre 500 e 20.000 pixels são considerados válidos.

5. **Agrupamento de Caixas**  
   Para evitar múltiplas detecções de um mesmo veículo, caixas próximas ou sobrepostas são agrupadas.

6. **Marcação e Contagem**  
   As caixas finais são desenhadas na imagem, e a quantidade de veículos detectados é exibida tanto na imagem quanto no terminal.

## Resultados

A aplicação foi testada com imagens contendo veículos de diferentes tamanhos e tonalidades de vermelho. O sistema demonstrou bom desempenho na detecção de carros vermelhos, mesmo em ambientes com iluminação variável e ruído moderado.

A seguir, estão os resultados de algumas imagens testadas:

![image](https://github.com/user-attachments/assets/2445f8af-9056-4a7e-822a-73436888d6cb)

![image](https://github.com/user-attachments/assets/330f6758-51f3-4af7-b6c5-7942e74b4452)


A quantidade total de veículos detectados foi impressa no terminal, bem como sobreposta à imagem com a numeração individual de cada carro detectado.

## Conclusão

O projeto demonstrou a eficácia de técnicas simples de processamento de imagens, como segmentação por cor, operações morfológicas e detecção de contornos, para detectar veículos vermelhos. A abordagem foi eficiente mesmo em imagens com ruído moderado e variações de iluminação.

## Referências

1. **GONZALEZ, R. C.; WOODS, R. E.** Processamento de Imagens Digitais. 3. ed. Pearson, 2010.
2. **OpenCV Documentation**: [https://docs.opencv.org/](https://docs.opencv.org/)

