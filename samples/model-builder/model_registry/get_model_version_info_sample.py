# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_model_registry_get_model_version_info_sample]

from google.cloud import aiplatform


def get_model_version_info_sample(
    model_id: str, version_id: str, project: str, location: str
):
    """
    Get model version info.
    Args:
        model_id: The ID of the model.
        version_id: The version ID of the model version.
        project: The project name.
        location: The location name.
    Returns:
        VersionInfo resource.
    """

    # Initialize the client.
    aiplatform.init(project=project, location=location)

    # Initialize the Model Registry resource with the ID 'model_id'.The parent_name of create method can be also
    # 'projects/<your-project-id>/locations/<your-region>/models/<your-model-id>'
    model_registry = aiplatform.models.ModelRegistry(model=model_id)

    # Get model version info with the version 'version_id'.
    model_version_info = model_registry.get_version_info(version=version_id)

    return model_version_info


# [END aiplatform_model_registry_get_model_version_info_sample]
