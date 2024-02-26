# Projeto Final do Bootcamp do LAMIA

## [English Version](readme_en.md)

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

Estou satisfeito em compartilhar que obtive resultados consistentes. No entanto, para uma análise mais abrangente das comparações, simplesmente observar a precisão e o número de perda dos modelos não seria suficiente. Por isso, forneci resultados detalhados no arquivo `testing-models.ipynb`. Neste documento, é possível examinar as métricas de desempenho de cada modelo no conjunto de dados de teste. Vale ressaltar que o conjunto de dados de teste foi compilado com imagens reais obtidas do Google Imagens e de vários sites de medicina. Além disso, para uma análise das métricas de desempenho de cada modelo no conjunto de dados de validação, os gráficos correspondentes podem ser encontrados nos arquivos de cada modelo respectivo.

Esses resultados estabelecem um fundamento promissor para futuros aprimoramentos e aplicações. Portanto, pretendo continuar desenvolvendo minhas competências em Aprendizado de Máquina no LAMIA.