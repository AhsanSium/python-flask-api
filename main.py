from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.example.com"
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200
    # we can send html to client
    # return (
    #     "<html> <title>Hello</title> <body style='color:blue;font-size:46px;'> Test Man </body></html>"
    # )


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    print(user_id)
    return jsonify({"message": "User Deleted"}), 201


@app.route("/")
def home():
    return "Home"


if __name__ == "__main__":
    app.run(debug=True)
