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
</head>
<body style='align-items: center; display: flex; justify-content: center; flex-direction: column; padding: 10px'>
    <h1 style='text-align: center'>Form Input Data Pasien</h1>

    <form style='background-color: #f2f2f2; padding: 20px; border-radius: 10px; width: 100%;' action="/generate" method="post" enctype="multipart/form-data">
    <label style='display: block; color: #555' for="name">Nama pasien:</label>
    <input style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="name" name="name"><br><br>

    <label style='display: block; color: #555' for="drg">Nama drg:</label>
    <input style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="drg" name="drg"><br><br>

    <label style='display: block; color: #555' for="piranti">Jenis Piranti:</label>
    <input style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="piranti" name="piranti"><br><br>

    <label style='display: block; color: #555' for="date">Tanggal pesan:</label>
    <input style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="date" name="date"><br><br>

    <label style='display: block; color: #555' for="detail">Keterangan:</label>
    <textarea style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' id="detail" name="detail" rows="4" cols="50"></textarea><br><br>

    <label style='display: block; color: #555' for="photo">Gambar:</label>
    <input style='width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="file" id="photo" name="photo"><br><br>

    <input type="submit" value="Submit">
    </form>
</body>
</html>
"""
