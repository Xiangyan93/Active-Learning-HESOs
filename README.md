# Active-Learning-HESOs
Active learning for High-Entropy-Spinel-Oxides Discovery

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
        ```
   3. Optionally, you can export experimental data.
        ```
        python export.py --property purity
        ```
   4. Active Learning.
        ```
        python3 active_learning.py --n_samples 5
        ```
## Machine Learning
See [notebook](https://github.com/Xiangyan93/Active-Learning-HESOs/tree/master/notebook).
