import mlflow

def calculate(x,y):
    return x*y


if __name__ == '__main__':
    #starting the server of mlflow
    with mlflow.start_run():
        x,y=85,20
        z=calculate(x,y)
        #tracking the experiment with mlflow
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_metric("z",z)
        #print(f"the sum is:{z}")