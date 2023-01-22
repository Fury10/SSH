# SSH
SSH is a linux only menu that makes using the ssh command even easier with the option to save profiles and search for them.
I took inspiration from [`ssh-menu`](https://github.com/antonjah/ssh-menu) and added additional features such as generating private keys, searching for profiles,

# Installation

#### Requirements:
- You will need python3 installed as well as pip  
- At the moment only the bullet package is needed however more may be added at a later point

Either download all of the [`requirements`](https://raw.githubusercontent.com/Fury10/SSH/master/requirements.txt) and install them using `pip install -r requirements.txt` or for now just install the one package using `pip install bullet`

next download the [script](https://raw.githubusercontent.com/Fury10/SSH/master/SSH.py) using: `wget https://raw.githubusercontent.com/Fury10/SSH/master/SSH.py`

to run the script use the following: `python3 SSH.py` alternatively you can create an alias to run the script:
`echo 'alias ssh="python3 SSH.py"' >> ~/.bash_aliases`

# To Add
- Support for Windows (need to use [forked bullet module](https://github.com/bchao1/bullet/pull/79), unsure of how to easily install it using pip, etc.)  
- Autocreate directory .ssh if not already existed
- Autocreate config file if not already created in .ssh/config
- Clean/Optimise Code
- Publish Python Package on PyPI

