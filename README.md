# 3D-modeller-and-viewer
## Descrição/Description  
Software feito como trabalho final da disciplina de computação gráfica. Permite vizualizar na tela objetos cilindricos em projeção perspectiva ou paralela e executa operações de escala, translação e rotação sobre eles. Os objetos podem ter diferentes atributos de superfície e a luz ambiente e a fonte de luz pontual podem ter seus atributos alterados. O pipeline de vizualização é simplificado, portando alguns bugs na vizualização paralela podem acontecer. O objeto é armazenado em memória de acordo com a [estrutura half-edge](https://cs184.eecs.berkeley.edu/sp19/article/15/the-half-edge-data-structure) que é implementada pela [biblioteca opemMesh](https://www.graphics.rwth-aachen.de/software/openmesh/).
  
This software was made as a final assignment for the Computer Graphics class. It allows the user visualize on the scree cylindric objects in perspective or parallel projection and applies scale, translation and rotation operations on them. The objects can have attributes related to the ambient light and the spot light and have it changed by the user. The visualization pipeline is simplified, because of it some bugs on the parallel visualization can happen. The object is stored in memory according to the [half-edge structure](https://cs184.eecs.berkeley.edu/sp19/article/15/the-half-edge-data-structure) which is implemented by the [openMesh library](https://www.graphics.rwth-aachen.de/software/openmesh/).

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
```
## Capturas de tela/Printscreens
To-do
