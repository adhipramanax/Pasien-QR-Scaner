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
</head>
<body style='align-items: center;'>
    <h1 style='text-align: center;'>Data Pasien</h1>
    <h1 style='text-align: center; display: block; color: #555'>Nama pasien: {data[0]["name"]}</h1>
    <image style='align-items: center; text-align: center; width: 200px' src="data:image/png;base64,{data[0]["photo"]}" />
    <h1 style='text-align: center; display: block; color: #555'>Nama drg: {data[0]["drg"]}</h1>
    <h1 style='text-align: center; display: block; color: #555'>Jenis piranti: {data[0]["piranti"]}</h1>
    <h1 style='text-align: center; display: block; color: #555'>Tanggal: {data[0]["date"]}</h1>
    <h1 style='text-align: center; display: block; color: #555'>Detail: {data[0]["detail"]}</h1>
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

    <input style='width: 100%; background-color: #007bff; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;' type="submit" value="Submit">
    </form>
</body>
</html>
"""
