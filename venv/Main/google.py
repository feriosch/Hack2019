# TODO(developer): Uncomment and set the following variables
# project_id = 'PROJECT_ID_HERE'
# compute_region = 'COMPUTE_REGION_HERE'
# model_id = 'MODEL_ID_HERE'
# file_path = '/local/path/to/file'
# score_threshold = 'value from 0.0 to 0.5'

from google.cloud import automl_v1beta1 as automl
import csv

automl_client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = automl_client.model_path(
    project_id, compute_region, model_id
)

# Create client for prediction service.
prediction_client = automl.PredictionServiceClient()

# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# Initialize params
params = {}
if score_threshold:
    params = {"score_threshold": score_threshold}

with open(file_path, "rt") as csv_file:
    # Read each row of csv
    content = csv.reader(csv_file)
    for row in content:
        # Create payload
        values = []
        for column in row:
            values.append({'number_value': float(column)})
        payload = {
            'row': {'values': values}
        }

        # Query model
        response = prediction_client.predict(model_full_id, payload)
        print("Prediction results:")
        for result in response.payload:
            print("Predicted class name: {}".format(result.display_name))
            print("Predicted class score: {}".format(result.classification.score))
