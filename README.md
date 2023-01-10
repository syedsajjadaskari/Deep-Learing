
# deep Classfier project

## Deep Learing 

## Workflows

1. update config.yaml
2. update secrets.yaml [ Optional]
3. update params.yaml
4. update the entity
5. update the configuraton manager in src config
6. update the componenets
7. update the pipeline
8. Test run pipeline stage
9. Run tox for testin your package
10. update the dvc.yaml
11. run "dvc repro"for runnin all the stage



STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab
'''
MLFLOW_TRACKING_URI=https://dagshub.com/syedsajjadaskari/Deep-Learing.mlflow
MLFLOW_TRACKING_USERNAME=syedsajjadaskari
MLFLOW_TRACKING_PASSWORD=<> \

'''
step 2: install mlflow

step 3: set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model

