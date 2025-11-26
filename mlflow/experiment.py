import mlflow
import random

if __name__ == "__main__":
    print("Starting MLFlow experiment...")
    
    # Start a new MLFlow run
    with mlflow.start_run():
        # Log a parameter
        param1 = random.randint(0, 100)
        mlflow.log_param("param1", param1)
        print(f"Logged param1: {param1}")

        # Log a metric
        metric1 = random.random()
        mlflow.log_metric("metric1", metric1)
        print(f"Logged metric1: {metric1}")

        # Log an artifact (dummy file)
        with open("output.txt", "w") as f:
            f.write("Hello MLFlow!")
        mlflow.log_artifact("output.txt")
        print("Logged artifact: output.txt")

    print("Experiment completed.")
