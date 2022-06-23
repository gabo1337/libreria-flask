from Flask import jsonify, Response

def response_json(mensaje: str,status: int = 200)-> Response:
    response = jsonify({
        "message":mensaje
    })

    response.status_code = status
    return response