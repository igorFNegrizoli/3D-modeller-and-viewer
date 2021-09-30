# 3D-modeller-and-viewer
## Descrição/Description  
Software feito como trabalho final da disciplina de computação gráfica. Permite vizualizar na tela objetos cilindricos em projeção perspectiva ou paralela e executa operações de escala, translação e rotação sobre eles. Os objetos podem ter diferentes atributos de superfície e a luz ambiente e a fonte de luz pontual podem ter seus atributos alterados. O algoritmo de sombreamento usado é o [sombreamento constante](https://en.wikipedia.org/wiki/Shading#Flat_shading). O pipeline de vizualização é simplificado, portando alguns bugs na vizualização paralela podem acontecer. O objeto é armazenado em memória de acordo com a [estrutura half-edge](https://cs184.eecs.berkeley.edu/sp19/article/15/the-half-edge-data-structure) que é implementada pela [biblioteca opemMesh](https://www.graphics.rwth-aachen.de/software/openmesh/).
  
This software was made as a final assignment for the Computer Graphics class. It allows the user visualize on the scree cylindric objects in perspective or parallel projection and applies scale, translation and rotation operations on them. The objects can have attributes related to the ambient light and the spot light and have it changed by the user. The shading algorithm used is the [flat shading](https://en.wikipedia.org/wiki/Shading#Flat_shading). The visualization pipeline is simplified, because of it some bugs on the parallel visualization can happen. The object is stored in memory according to the [half-edge structure](https://cs184.eecs.berkeley.edu/sp19/article/15/the-half-edge-data-structure) which is implemented by the [openMesh library](https://www.graphics.rwth-aachen.de/software/openmesh/).

## Autores/Authors
[Amanda Israel Graeff Borges](https://github.com/AmandaIsrael)  
[Igor França Negrizoli](https://github.com/igorFNegrizoli)  
[Leonardo Vanzin](https://github.com/EnergyFall266) 
 
## Instalação/Installation 
[Siga estas instruções para instalar o sistema gerenciador de pacotes conda   
Follow these instructions to install conda package management system](https://docs.conda.io/projects/conda/en/latest/user-guide/install/#regular-installation)

Com o conda instalado / with conda installed:  
```
conda create --name cg_py37 python=3.7
conda activate cg_py37
conda install -c anaconda tk
conda install -c conda-forge openmesh
conda install -c conda-forge openmesh-python
python3 GUI.py
```
## Instruções/Instructions
O botão "Novo mundo" atualiza os parâmetros de mundo
O botão "Novo objeto" insere um objeto com os parâmetros de objeto especificados
O botão "Att. luz" atualiza os parâmetros relacionados à luz ambiente e à luz pontual caso nenhum objeto esteja selecionado e atualiza os atributos de reflexão (Ka, Kd, Ks e n) do objeto caso algum objeto esteja selecionado
O botão "Limpar cena" remove todos os objetos da cena

Após selecionar um polígono com o cursor do mouse:
Q e A, W e S, E e D para aplicar transformações de translação nos objetos nos eixos x y e z respectivamente
R e F, T e G, Y e H para aplicar transformações de escala nos objetos nos eixos x y e z respectivamente
U e J, I e K, o e L para aplicar transformações de rotação nos objetos nos eixos x y e z respectivamente

## Capturas de tela/Printscreens
 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/90/Overview1.png" /><br>
  <span><i>Cena exemplo em projeção perspectiva / Example scene in perspective projection</i></span>
</p>

 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Overview2.png" /><br>
  <span><i>Cena exemplo em projeção paralela / Example scene in parallel projection</i></span>
</p>

 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Menu1.png" /><br>
  <span><i>Parâmetros de mundo disponíveis / Available word parameters</i></span>
</p>

 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d2/Menu2.png" /><br>
  <span><i>Parâmetros disponíveis para a criação do objeto / Object creation available parameters</i></span>
</p>

 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/45/Menu3.png" /><br>
  <span><i>Parâmetros de sombreamento de objeto disponíveis / Object shading available parameters</i></span>
</p>

