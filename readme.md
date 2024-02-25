# Projeto Final do Bootcamp do LAMIA

## [English Version](README_EN.md)

## LAMIA

O LAMIA, situado no campus da UTFPR em Santa Helena, é um centro de pesquisa dedicado à aplicação de Ciência de Dados e Visão Computacional na indústria. Ele desenvolve tecnologia e conhecimento acadêmico para o setor, contando com uma equipe de colaboradores espalhados por todo o país.

![LAMIA logo](/images/lamia.png)

## Bootcamp e jornada

Ao ingressar no laboratório, faz necessária passar por um bootcamp de treinamento e elaborar um projeto final que evidencie suas habilidades e contribuições. Durante esse processo, os participantes são considerados iniciantes e possuem um prazo para finalizar o treinamento. O laboratório abrange várias áreas, e escolhi focar em Aprendizado de Máquina.

## Desafio escolhido

Para meu projeto final, escolhi o seguiunte desafio: 
- Fazer uma compração entre três famosos modelos convolucionais disponíveis atualmente. 
    - Os modelos devem fazer a classificação de Covid-19 e Pneumonia a partir de uma imagem de raio-x.

Os modelos escolhidos foram:
- ResNet50
- VGG16
- InceptionV3

Todos disponíves para utilização na biblioteca tensorflow.

## Base de dados

A realização do treinamento e validação dos modelos teve como base uma mescla dos seguintes datasets:

- Covid-19 Image Dataset. 
    - Disponível em: https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset

- COVIDx CXR-4. 
    - Disponível em: https://www.kaggle.com/datasets/andyczhao/covidx-cxr2

- Chest X-Ray Images (Pneumonia) with new class. 
    - Disponível em: https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-clas

Resultando em `9423` imagens para o treinamento e `2353` imagens para a validação. 

# Resultados

Estou contente em informar que consegui resultados consistentes. 
Para uma melhor consistência entre as comparações, analisar apenas a precisão e e perda dos modelos não seria suficiente.
Por isso, resultados detalhados então disponibilizados no arquivo `testing-models.ipynb`. No mesmo, é possível analisar a precisão de cada modelo em cada caso. 

Esses resultados estabelecem um fundamento promissor para futuros aprimoramentos e aplicações. Portanto, pretendo continuar desenvolvendo minhas competências em Aprendizado de Máquina no LAMIA.