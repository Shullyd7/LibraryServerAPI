from flask import Flask, request, jsonify
from server_api import *

app = Flask(__name__)

# API endpoints for creating entities

@app.route("/users", methods=["POST"])
def create_user_endpoint():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    if not (username and email):
        return jsonify({"error": "Username and email are required"}), 400
    user_id = create_user(username, email)
    return jsonify({"user_id": user_id}), 201

@app.route("/groups", methods=["POST"])
def create_group_endpoint():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Group name is required"}), 400
    group_id = create_group(name)
    return jsonify({"group_id": group_id}), 201

@app.route("/datasets", methods=["POST"])
def create_dataset_endpoint():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    created_by = data.get("created_by")
    if not (name and description and created_by):
        return jsonify({"error": "Name, description, and created_by are required"}), 400
    dataset_id = create_dataset(name, description, created_by)
    return jsonify({"dataset_id": dataset_id}), 201

@app.route("/metadata", methods=["POST"])
def create_metadata_endpoint():
    data = request.json
    dataset_id = data.get("dataset_id")
    name = data.get("name")
    description = data.get("description")
    created_by = data.get("created_by")
    if not (dataset_id and name and description and created_by):
        return jsonify({"error": "Dataset ID, name, description, and created_by are required"}), 400
    metadata_id = create_metadata(dataset_id, name, description, created_by)
    return jsonify({"metadata_id": metadata_id}), 201

@app.route("/filelists", methods=["POST"])
def create_filelist_endpoint():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    created_by = data.get("created_by")
    if not (name and description and created_by):
        return jsonify({"error": "Name, description, and created_by are required"}), 400
    filelist_id = create_filelist(name, description, created_by)
    return jsonify({"filelist_id": filelist_id}), 201

# API endpoint to apply access restrictions for User and Group management

@app.route("/apply-access-restrictions", methods=["POST"])
def apply_access_restrictions_endpoint():
    data = request.json
    user_id = data.get("user_id")
    group_id = data.get("group_id")
    restrictions = data.get("restrictions")
    if not (user_id and group_id and restrictions):
        return jsonify({"error": "User ID, group ID, and restrictions are required"}), 400

# API endpoints for querying and retrieval of data

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_endpoint(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.__dict__)

@app.route("/groups/<int:group_id>", methods=["GET"])
def get_group_endpoint(group_id):
    group = get_group(group_id)
    if not group:
        return jsonify({"error": "Group not found"}), 404
    return jsonify(group.__dict__)


# API endpoints for integration with external tools

@app.route("/annotation-tool-result", methods=["POST"])
def store_annotation_tool_result_endpoint():
    data = request.json
    result = store_annotation_tool_result(data)
    return jsonify({"message": result}), 200

@app.route("/annotation-data/<int:recording_id>", methods=["GET"])
def retrieve_annotation_data_endpoint(recording_id):
    annotations = retrieve_annotation_data(recording_id)
    return jsonify(annotations)

# API endpoints for data cleaning and pre-processing

@app.route("/data-cleaning", methods=["POST"])
def basic_data_cleaning_endpoint():
    data = request.json
    cleaned_data = basic_data_cleaning(data)
    return jsonify(cleaned_data)

@app.route("/quality-checks", methods=["POST"])
def quality_checks_endpoint():
    data = request.json
    result = quality_checks(data)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)