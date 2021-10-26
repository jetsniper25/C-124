from flask import Flask, jsonify,request

app=Flask(__name__)
@app.route("/")
def helloworld():
    return "hello world"

tasks=[
    {
        "id":1,
        "title":u"buy groceries",
        "description":u"Milk, Cheese, Fruit, Salt, Sugar",
        "done":False
    },
    {
        "id":2,
        "title":u"learn python",
        "description":u"Need to go through the basics of python",
        "done":False
    }
]

@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added succesfully"
    })
    
@app.route("/getdata")
def gettask():
    return jsonify({
        "data":tasks
    })


if __name__=="__main__":
    app.run(debug=True)
