Inside text generator install a env

then install flask inside the env

`pip install -r requirements.txt`

`pip install tensorflow`


fine tuning model.

- Need training file
`python3 encode.py train.txt training.npz`

`python3 train.py --dataset training.npz`


test model
`python3 interactive_conditional_samples.py --top_k 40`