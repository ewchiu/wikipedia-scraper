from flask import Flask, request, jsonify
import wikipedia as wk

app = Flask(__name__)

# Wikipedia scraper by Eric Chiu
# If wiki search results in an exception being raised,
# null will be returned in the JSON object

@app.route("/wiki")
def scraper():
    search_term = request.args.get("search")

    try: 
        summary = wk.summary(search_term, sentences=2)
    except:
        response = {'info': None}
    else:
        response = {'info': summary}

    return jsonify(response)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)