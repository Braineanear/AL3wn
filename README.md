# AL3wn Educational Platform Website.



## Running this project

### what to do everytime to open it

open the main folder that has the virtual environment and the project
activate the env with this command on

mac/linux:

```
source dj/bin/activate
```

windows:

```
dj\Scripts\activate
```

then go to the project folder

```
cd al3wn
```

Now you can run the project with this command

```
python manage.py runserver
```


### Starting

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv dj
```

That will create a new folder `dj` in your project directory. Next activate it with this command on

mac/linux:

```
source dj/bin/activate
```

windows:

```
dj\Scripts\activate
```
then go to the project folder

```
cd al3wn
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
