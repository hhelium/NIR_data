# MagicHand: Context-Aware Dexterous Grasping Using an Anthropomorphic Robotic Hand

This paper contains a NIR dataset and related pre-processing method. If you find this code useful in your research, please consider citing:

    @inproceedings{li2020magichand,
      title={MagicHand: Context-Aware Dexterous Grasping Using an Anthropomorphic Robotic Hand},
      author={Li, Hui and Tan, Jindong and He, Hongsheng},
      booktitle={2020 IEEE International Conference on Robotics and Automation (ICRA)},
      pages={9895--9901},
      year={2020},
      organization={IEEE}
    }
[[download paper](https://ieeexplore.ieee.org/document/9196538)]

    @inproceedings{rao2018learning,
      title={Learning robotic grasping strategy based on natural-language object descriptions},
      author={Rao, Achyutha Bharath and Krishnan, Krishna and He, Hongsheng},
      booktitle={2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
      pages={882--887},
      year={2018},
      organization={IEEE}
    }
[[download paper](https://ieeexplore.ieee.org/document/8593886)]



This code was tested on an Ubuntu 16.04 system.

### MagicHand Platform ####
The MagicHand platform integrates an AR10 anthropomorphic robotic hand, a Sawyer robotic arm, a SCiO sensor, and an Intel Realsense D435 depth camera.

<img src="./images/magichand.png" width="40%">
<img src="./images/header.pdf" width="40%">


### Task-Oriented Context-Aware Dexterous Grasping ####   

<img src="./images/wf.png" width="80%">

### NIR dataset
1. Contains 15936 near-infrared spectra of six types of materials including ceramic, stainless steel, wood, cardboard, plastic, and glass materials. 
2. 54 different daily used objects were selected. For each object, 10 sample were selected for data collection. For each sample, about 30 NIR spectra was collected using SciO sensor 

<img src="./images/data.png" width="50%">

### Context-Aware Task-Oriented Grasping
Grasp strategies can be decided by the perceived object features and task designations. 


### Application and Usage
Near-infrared spectroscopy (NIRS) is a low-cost, simple, fast and nondestructive technique to analyze the spectrum of materials on a molecular level. NIRS is increasingly becoming one of the most efficient analytical tools in chemistry composition and material recognition.  

Originally, NIRS is mainly used in food industry to differentiate fruits or plants, analyze chemical composition or test food quality. Recently, this technique is also used to detect falsified medicines, classify gasoline, recognize colonic tissues and human-computer interface. 

As a non-destructive, non-invasive, chemical-free and rapid way to identify various materials, NIRS has great potential for aiding robot to interact with environments. 
