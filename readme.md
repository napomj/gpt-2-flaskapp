
# Install Requirements

- Some additional requirements might be required

`pip install -r requirements.txt`

`pip install tensorflow`


# Fine tuning model.

- Inside of the gpt-2/src you can use the `encode.py` to train a text file.

__note: you first need to download one of the models__

`python encode.py <file_name>.txt training.npz`

- This trains the model. While training you may enter `ctrl + C` and it will automatically save the content inside of a folder called checkpoint. Then you will want to copy that folders contents into the model (or copy of) you trained from. Use this to generate your text.

`python train.py --dataset training.npz`
