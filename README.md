# TTM4115_KomSys_SemesterProsjekt

Run ```main.py``` using the following command

```python .\main.py```

# How to set up a venv environment (inside the project folder)
For reference: [docs.python](https://docs.python.org/3/library/venv.html)

1. Clone the project on your computer.
2. Navigate to the project.
3. Run the following command to create a new environment called "venv". It's going to create a folder for your environment inside the project folder. This is already added to the gitignore file, so it's not going to be pushed to a remote repo. Note that your venv environment will be based on your "python3" version.


```python3 -m venv ./venv```
Activate the enviroment using one of the following commands.

Posixs/unix (max and linux):

```source venv/bin/activate```

Windows cmd:

```C:\> venv\Scripts\activate.bat```

Windows powershell:

```PS C:\> venv\Scripts\Activate.ps1```

If sucessful, you should see you environment in your teminal, like this (mac):

```$ (venv) computername:TTM4115_Project username$ ```


Install required packages specified in the "requirements.txt" file using the following command.

```pip install -r requirements.txt```

If you install any additional packages that your teammates also will need, then add them to the "requirements.txt" file by using the following command.
```pip freeze > requirements.txt```
