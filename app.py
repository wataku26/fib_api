from flask import Flask, request, jsonify

app = Flask(__name__)

# フィボナッチ数を計算する関数
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# フィボナッチAPIエンドポイント
@app.route('/fib', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n')
    if not n:
        return jsonify({"status": 400, "message": "Parameter 'n' is required."}), 400

    try:
        n = int(n)
        if n <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as e:
        return jsonify({"status": 400, "message": str(e)}), 400

    result = fibonacci(n)
    return jsonify({"result": result}), 200

# メイン関数
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
