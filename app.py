from flask import Flask, request, jsonify
import wikipedia as wk

app = Flask(__name__)

@app.route("/wiki")
def scraper():
    search_term = request.args.get("search")

    try: 
        wk.summary(search_term)
    except:
        response = {'info': None}
        return jsonify(response)
    else:
        summary = wk.summary(search_term, sentences=2)
        response = {'info': summary}
        return jsonify(response)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)