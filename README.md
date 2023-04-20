# Into the Logisticverse: Improving Efficiency in Transportation Networks using Python

## PyCon US 2023 Talk Code Examples

### Virtual Environment Setup

You will need python installed on your machine. Version 3.8 and up are preferred however version 3.6 to 3.7 are acceptable.

Setup a virtual environment by running the following command in the root of the repo directory:

```shell
$ python3 -m venv .venv
```

Once created activate your virtual environment by running the following command:

**Bash**

```shell
$ source .venv/bin/activate
```

**Windows (Powershell)**
```powershell
$ .venv/Scripts/activate
```

### Installing Dependencies

Each example from the talk is in its own folder and each folder has its own requirements.txt which can be used to install the dependencies needed to run the example python code.

> **NOTE:.** Make sure you have your virtual environment activated

**Installing dependencies for a single example**

```shell
(.venv) $ python3 -m pip install -r finding-the-right-order/requirements.txt
```

**Installing dependencies for all examples**

```shell
(.venv) $ python3 -m pip install \
    -r finding-the-right-order/requirements.txt \
    -r improving-connectivity/requirements.txt \
    -r match-powers-to-loads/requirements.txt
```

### Run the main.py file found in each example's folder.