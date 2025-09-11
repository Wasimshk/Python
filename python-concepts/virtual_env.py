"""
install virtual environment
    pip install virtualenv

create virtual env
    python -m venv {venv name} e.g python -m venv myenv1
        this will create and add a folder named myenv1 at the current working directory

activate virtual environment
    .\myenv1\Scripts\Activate.ps1
        after running the command it will activate the env and we can now see the '(myenv1)' written at left side of the command line

install other packages
    pip install requests
        it will now only installed in virtual env

check all the installed packages
    pip list

install specific version
    pip install requests==2.32.5

upgrade a package
    pip install --upgrade requests
        updated the package to latest version available

delete a package
    pip uninstall requests

show the packages with version number
    pip freeze
        shows the packages in the following form ->> requests==2.32.5

create a requirement.txt with all the required packages
    pip freeze > requirements.txt
        '>' basically a command line to add the output from earlier command to the specific file.

install packages from requirements.txt
    pip install -r requirements.txt

deactivate the virtual env
    deactivate


"""