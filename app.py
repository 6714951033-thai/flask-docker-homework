from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            # บันทึกข้อความลง log.txt
            with open("log.txt", "a", encoding="utf-8") as file:
                file.write(message + "\n")

    return f"""
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Web Server</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}

            .container {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                width: 500px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }}

            h1 {{
                text-align: center;
            }}

            label {{
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
            }}

            input {{
                width: 100%;
                box-sizing: border-box;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 16px;
            }}

            button {{
                width: 100%;
                margin-top: 15px;
                padding: 12px;
                border: none;
                border-radius: 8px;
                background: #2563eb;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            .result {{
                margin-top: 25px;
                padding: 15px;
                background: #eef6ff;
                border-radius: 8px;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Simple Web Server</h1>

            <form method="POST">

                <label for="message">กรอกข้อความ</label>

                <input
                    type="text"
                    id="message"
                    name="message"
                    placeholder="พิมพ์ข้อความที่นี่..."
                    required
                >

                <button type="submit">
                    ส่งข้อความ
                </button>

            </form>

            <div class="result">
                <strong>ข้อความที่ได้รับ:</strong>
                <p>{message}</p>
            </div>

        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)