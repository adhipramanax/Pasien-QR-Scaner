def return_qr_code_html(img_base64):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
</head>
<body>
    <image src="data:image/png;base64,{img_base64}" />
</body>
</html>
"""


def return_error_html(message):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
    style="text-align:center"
</head>
<body class="center">
    <h1>{str(message)}</h1>
</body>
</html>
"""


def return_users_html(data):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
    <style>
        .center {{
            text-align: center;
        }}
    </style>
        
</head>
<body class="center">
    <h1>Name: {data[0]["name"]}</h1>
    <h1>Detail: {data[0]["detail"]}</h1>
    <image src="data:image/png;base64,{data[0]["photo"]}" />
</body>
</html>
"""


def return_input_users_html():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
    <style>
        .center {{
            text-align: center;
        }}
    </style>
</head>
<body style='background-color:#E6E6FA'>
    <h1 style='text-align: center'>Form Input Data</h1>
    <form action="/generate" method="post" enctype="multipart/form-data">
    <label style='text-align: center' for="name">Nama:</label>
    <input style='text-align: center' type="text" id="name" name="name"><br><br>

    <label for="detail">Keterangan:</label>
    <textarea id="detail" name="detail" rows="4" cols="50"></textarea><br><br>

    <label for="photo">Gambar:</label>
    <input type="file" id="photo" name="photo"><br><br>

    <input type="submit" value="Submit">
    </form>
</body>
</html>
"""
