# Active-Learning-HESOs
Active learning for High-Entropy-Spinel-Oxides Discovery

## Installation
```
mamba create --name alhesos python=3.10 -y
mamba activate alhesos
pip install typed-argument-parser tqdm pandas numpy sqlalchemy
```

## Database
Database Creation, data import and export.
   1. Create the database.
        ```
        python create.py
        ```
   2. Import experimental data.
        ```
        python import.py --input database/raw_data/purity_KS.csv --property purity --tag KS
        python import.py --input database/raw_data/purity_al_init.csv --property purity
        python import.py --input database/raw_data/T90_al_init.csv --property T90
        python import.py --input database/raw_data/al1.csv --property purity
        python import.py --input database/raw_data/al1.csv --property T90
        python import.py --input database/raw_data/al2.csv --property purity
        python import.py --input database/raw_data/al2.csv --property T90
        python import.py --input database/raw_data/al3.csv --property purity
        python import.py --input database/raw_data/al3.csv --property T90
        python import.py --input database/raw_data/al4.csv --property purity
        python import.py --input database/raw_data/al4.csv --property T90
        ```
   3. Optionally, you can export experimental data.
        ```
        python export.py --property purity
        ```
   4. Active Learning.
        ```
        python3 active_learning.py --n_samples 5
        ```
## Figures
See [notebook](https://github.com/Xiangyan93/Active-Learning-HESOs/tree/master/notebook).

## Citations <a name="citations"></a>
If you find the code useful in your research, please cite the paper:

[Active Learning Guided Discovery of High Entropy Oxides Featuring High H2-production](https://pubs.acs.org/doi/abs/10.1021/jacs.4c06272)
