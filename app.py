from flask import Flask, Response, jsonify
from get_data import get_arots, get_products, get_units

app = Flask(__name__)

@app.route('/api/arots', methods=['GET'])
def api_get_arots():
    """
    API endpoint to retrieve Arot data in JSON format.
    Retrieves data from get_arots(), converts the Pandas DataFrame
    safely to JSON (handling timestamps, NaNs, and numpy datatypes),
    and returns the response.
    """
    try:
        df = get_arots()
        if df is None:
            return jsonify({
                "success": False,
                "error": "Failed to retrieve arot data from the upstream API"
            }), 500

        # Convert the pandas DataFrame to a JSON string.
        # orient='records' creates a JSON list of objects.
        # date_format='iso' converts timestamps to standard ISO format.
        json_data = df.to_json(orient='records', date_format='iso')

        return Response(json_data, mimetype='application/json')

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An unexpected error occurred: {str(e)}"
        }), 500


@app.route('/api/products', methods=['GET'])
def api_get_products():
    """
    API endpoint to retrieve Products data in JSON format.
    Retrieves data from get_products(), converts the Pandas DataFrame
    safely to JSON, and returns the response.
    """
    try:
        df = get_products()
        if df is None:
            return jsonify({
                "success": False,
                "error": "Failed to retrieve products data from the upstream API"
            }), 500

        json_data = df.to_json(orient='records', date_format='iso')
        return Response(json_data, mimetype='application/json')

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An unexpected error occurred: {str(e)}"
        }), 500


@app.route('/api/units', methods=['GET'])
def api_get_units():
    """
    API endpoint to retrieve Units data in JSON format.
    Retrieves data from get_units(), converts the Pandas DataFrame
    safely to JSON, and returns the response.
    """
    try:
        df = get_units()
        if df is None:
            return jsonify({
                "success": False,
                "error": "Failed to retrieve units data from the upstream API"
            }), 500

        json_data = df.to_json(orient='records', date_format='iso')
        return Response(json_data, mimetype='application/json')

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An unexpected error occurred: {str(e)}"
        }), 500


if __name__ == '__main__':
    # Run the server locally on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)

