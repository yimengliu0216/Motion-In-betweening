# Motion In-betweening

## Dependencies
- Python 3+ distribution
- PyTorch >= 1.4.0
- NumPy 
- PIL
- TensorboardX
- Pyyaml

## Dataset and model
Download dataset follow [this repo](https://github.com/ubisoft/ubisoft-laforge-animation-dataset). 
Download pretrained models at [this link](https://drive.google.com/drive/folders/1Esu4LhiXI1BH19EAitYD1LwDV_OGjoJ7?usp=sharing). 

## Data preparation
```
python flip_bvh.py
```

## Training
```
python train.py
```

## Testing
```
python test.py
```

## Acknowledgement
> Felix G. Harvey, Mike Yurick, Derek Nowrouzezahrai, and Christopher Pal. [Robust Motion In-betweening](https://dl.acm.org/doi/pdf/10.1145/3386569.3392480). *ACM Transactions on Graphics (TOG)*, 2020.
