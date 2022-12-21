### Create a virtual ENvirnments
echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
virtualenv venv
### Activate the virtual Envirmnet
echo [$(date)]: "activating the environment" 
.venv/bin/activate
echo [$(date)]: "installing the dev requirements" 
### Creating a new Folder for LabProgram
pip install -r requirements_dev.txt
echo [$(date)]: "END" 


