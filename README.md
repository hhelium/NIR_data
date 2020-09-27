# MagicHand: Context-Aware Dexterous Grasping Using an Anthropomorphic Robotic Hand

This paper contains a NIR dataset and related pre-processing method for our [paper](https://ieeexplore.ieee.org/document/9196538). If you find this code useful in your research, please consider citing:

    @inproceedings{li2020magichand,
      title={MagicHand: Context-Aware Dexterous Grasping Using an Anthropomorphic Robotic Hand},
      author={Li, Hui and Tan, Jindong and He, Hongsheng},
      booktitle={2020 IEEE International Conference on Robotics and Automation (ICRA)},
      pages={9895--9901},
      year={2020},
      organization={IEEE}
    }

This code was tested on an Ubuntu 16.04 system.

### NIR dataset
The dataset contains 15936 near-infrared spectra of six types of materials including ceramic, stainless steel, wood, cardboard, plastic and glass. A total of 54 different daily used objects were selected. This material/objectselection pattern would expand the universality of our datasets. For each object 10 sample were selected for data collection and for each sample about 30 nir spectra was gather using SciO sensor depending on the size of the sample. To  sum  up, there were six materials, 54 objects, 540 samples and 15936 scans in this dataset. In addition, python codes for several preprocesing method are also included.


### Application and Usage
Near-infrared spectroscopy (NIRS) is a low-cost, simple, fast and nondestructive technique to analyze the spectrum of materials on a molecular level. NIRS is increasingly becoming one of the most efficient analytical tools in chemistry composition and material recognition.  

Originally, NIRS is mainly used in food industry to differentiate fruits or plants, analyze chemical composition or test food quality. Recently, this technique is also used to detect falsified medicines, classify gasoline, recognize colonic tissues and human-computer interface. 

As a non-destructive, non-invasive, chemical-free and rapid way to identify various materials, NIRS has great potential for aiding robot to interact with environments. In this paper, we utilized this technique to recognize characsterics of target object and generate proper grasping strategies based on these characsterics.  
