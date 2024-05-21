# Library Server API

This project implements a Python API backend service for managing users, groups, datasets, metadata, filelists, and integrating with external tools. It also provides functionalities for data cleaning and pre-processing.

## Files

- `schema.py`: Defines the data model for the project including classes for User, Group, EntDataset, EntRecording, and EntFilelist.
- `server_api.py`: Contains core logic for interacting with databases and handling data models. It includes functions for creating users, groups, datasets, metadata, filelists, querying and retrieval of data, integration with external tools, and data cleaning and pre-processing.
- `app.py`: Implements API endpoints using Flask. It exposes the functions from `server_api.py` as HTTP endpoints for clients to interact with.

## Usage

1. Ensure you have Python installed on your system.
2. Install Flask using `pip install Flask`.
3. Run the Flask application by executing `python app.py`.
4. Use HTTP client tools like cURL or Postman to interact with the exposed API endpoints.

## API Endpoints

- **User and Group Management**:
  - `POST /users`: Create a new user.
  - `POST /groups`: Create a new group.
  - `GET /users/<user_id>`: Retrieve user details.
  - `GET /groups/<group_id>`: Retrieve group details.
  - `POST /apply-access-restrictions`: Apply access restrictions for User and Group management.


- **Dataset Storage and Management**:
  - `POST /datasets`: Create a new dataset.
  - `POST /metadata`: Create metadata for a dataset.
  - `GET /datasets/<dataset_id>`: Retrieve dataset details.
  - `GET /metadata/<metadata_id>`: Retrieve metadata details.

- **Filelist Storage and Management**:
  - `POST /filelists`: Create a new filelist.
  - `GET /filelists/<filelist_id>`: Retrieve filelist details.

- **Integration Point for External Tools**:
  - `POST /annotation-tool-result`: Store annotation tool result.
  - `GET /annotation-data/<recording_id>`: Retrieve annotation data.

- **Data Cleaning and Pre-processing**:
  - `POST /data-cleaning`: Perform basic data cleaning.
  - `POST /quality-checks`: Perform quality checks on data.
