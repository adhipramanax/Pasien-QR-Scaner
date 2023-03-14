def return_qr_code_html(img_base64):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
</head>
<body>
    <h1 style='font-size: 5rem; text-align: center'>Scan Me</h1>
    <image style='width: 100%;' src="data:image/png;base64,{img_base64}" />
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
<body style='align-items: center; '>
    <h1 style='font-size: 5rem; text-align: center; margin: 0;'>Data Pasien</h1>
    <div style='background-color: #f2f2f2; display: flex; justify-content: center; flex-direction: column;'>
    <h1 style='font-size: 4rem; text-align: center; display: block; color: #000'>{data[0]["name"]}</h1>
    
    <div style='display: flex; justify-content: center; '>
    <image style='border-radius: 10%; align-items: center; text-align: center; width: 50vw' src="data:image/png;base64,{data[0]["photo"]}" />
    </div>
    
    <h1 style='font-size: 2.5rem; text-align: center; display: block; color: #555; border: 2px solid; padding: 10px; border-radius: 25px;'>drg. {data[0]["drg"]}</h1>
    
    <table>
    <tr style='font-size: 3rem; font-weight: bold;'>
        <td style='width: 40%;'>Jenis Piranti</td>
        <td style='width: 3px; padding: 0;'>:</td>
        <td >{data[0]["piranti"]}</td>
    </tr>
    <tr style='font-size: 3rem; font-weight: bold;'>
        <td style='width: 40%;'>Tanggal</td>
        <td style='width: 3px; padding: 0;'>:</td>
        <td >{data[0]["date"]}</td>
    </tr>
    <tr style='font-size: 3rem; font-weight: bold;'>
        <td style='width: 40%;'>Detail</td>
        <td style='width: 3px; padding: 0;'>:</td>
        <td >{data[0]["detail"]}</td>
    </tr>
    </table>

    </div>

    </div>
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
    <h1 style='font-size: 5rem; text-align: center'>Form Input Data Pasien</h1>

    <form style='background-color: #f2f2f2; padding: 20px; border-radius: 10px; width: 100%;' action="/generate" method="post" enctype="multipart/form-data">
    <label style='font-size: 3rem; display: block; color: #555' for="name">Nama pasien:</label>
    <input style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="name" name="name"><br><br>

    <label style='font-size: 3rem; display: block; color: #555' for="drg">Nama drg:</label>
    <input style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="drg" name="drg"><br><br>

    <label style='font-size: 3rem; display: block; color: #555' for="piranti">Jenis Piranti:</label>
    <input style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="piranti" name="piranti"><br><br>

    <label style='font-size: 3rem; display: block; color: #555' for="date">Tanggal pesan:</label>
    <input style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="text" id="date" name="date"><br><br>

    <label style='font-size: 3rem; display: block; color: #555' for="detail">Keterangan:</label>
    <textarea style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' id="detail" name="detail" rows="4" cols="50"></textarea><br><br>

    <label style='font-size: 3rem; display: block; color: #555' for="photo">Gambar:</label>
    <input style='font-size: 3rem; width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: none;' type="file" id="photo" name="photo"><br><br>

    <input style='font-size: 3rem; width: 100%; background-color: #007bff; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;' type="submit" value="Submit">
    </form>
</body>
</html>
"""
