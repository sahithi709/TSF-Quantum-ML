TIME SERIES FORCASTING USING QUANTUM MACHINE LEARNING

Getting Started
Create and activate a new Conda environment with python 3.11.7

Install requirements. pip install -r requirements.txt

Download data. You can download the weather dataset from Autoformer. Create a seperate folder ./dataset and put the weather.csv file in the directory.

QuLTSF
Training: All the scripts are in the directory ./scripts/. For example, to train the QuLTSF model you can use
sh scripts/QuLTSF_seq_len_336.sh
It will start to train QuLTSF model with fixed sequence length 336 and varying prediction lengths.

Acknowledgement
We acknowledge the following github repos very much for the valuable code base and dataset:

https://github.com/cure-lab/LTSF-Linear

https://github.com/zhouhaoyi/Informer2020

https://github.com/thuml/Autoformer

https://github.com/MAZiqing/FEDformer

https://github.com/yuqinie98/PatchTST

https://github.com/Yitiann/MTST
