
# Install Requirements

- Some additional requirements might be required

`pip install -r requirements.txt`

`pip install tensorflow`


# Fine tuning model

- Preparing a text file to be trained is just a matter of compiling a large amount of text inside a .txt file.

- Inside of the gpt-2/src you can use the `encode.py` to train a text file.

__note: you first need to download one of the models by using the follow commands__
``` terminal
python3 download_model.py 124M
python3 download_model.py 355M
python3 download_model.py 774M
python3 download_model.py 1558M
```

`python encode.py <file_name>.txt training.npz`

- This trains the model. While training you may enter `ctrl + C` and it will automatically save the content inside of a folder called checkpoint. Then you will want to copy that folders contents into the model (or copy of) you trained from. Use this to generate your text.

`python train.py --dataset training.npz`

- Transfering files into the model file
    - A folder called `checkpoint` will get generated. Once training is complete, copy the contents of this folder into either the downloaded model folder or a copy of the downloaded model which you used to train the text file. 
    - This new folder with the checkpoint information and previous model information will be what is used for generating text.


# Flask App

- Ensure you have all the correct libraries installed.
    - Flask
    - Python

- To start the application run the following in the project terminal.
    - `flask run`

# Troubleshooting

- We found incompatabilities when trying to run the application on a macbook with the M1 chip.