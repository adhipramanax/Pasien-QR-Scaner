def return_qr_code_html(img_base64):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body class="p-4">
    <h1 style="font-size: 5rem" class="text-center fw-bold ">Scan Me</h1>
    <image style="height: 600px; object-fit: cover;" class="rounded mx-auto d-block" src="data:image/png;base64,{img_base64}" />
</body>
</html>
"""


def return_error_html(message):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Input Data</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body class="p-4">
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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>     
</head>
<body style="font-size: 3rem" class="p-4">
    <div class="text-center">
        <div class="my-5">
            <h1 style="font-size: 5rem" class="text-center fw-bold ">Intan</h1>
            <h1 style="font-size: 5rem" class="text-center fw-bold ">Dental Laboratory</h1>
        </div>
        <div class="d-flex justify-content-between">
            <p class="fw-bold p-0 m-0">Nomor: {data[0]["num"]}</p>
            <p class="fw-bold p-0 m-0">Tgl Kirim: {data[0]["order"]}</p>
        </div>
    </div>
    <div class="d-flex justify-content-center align-items-center flex-column my-5">
        <image style="height: 500px; object-fit: cover;" class=" rounded mx-auto d-block" src="data:image/png;base64,{data[0]["photo"]}" />
    </div>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th class="col-5" scope="col"></th>
                    <th class="col-1" scope="col"></th>
                    <th class="" scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Nama Pasien</td>
                    <td>:</td>
                    <td>{data[0]["name"]}</td>
                </tr>
                <tr>
                    <td>Nama Dokter Gigi</td>
                    <td>:</td>
                    <td>{data[0]["drg"]}</td>
                </tr>
                <tr>
                    <td>Jenis Pekerjaan</td>
                    <td>:</td>
                    <td>{data[0]["job"]}</td>
                </tr>
                <tr>
                    <td>Tanggal Selesai</td>
                    <td>:</td>
                    <td>{data[0]["send"]}</td>
                </tr>
                <tr>
                    <td>Alamat Laboratorium</td>
                    <td>:</td>
                    <td>{data[0]["lab"]}</td>
                </tr>
                <tr>
                    <td>No Hp</td>
                    <td>:</td>
                    <td>{data[0]["hp"]}</td>
                </tr>
            </tbody>
        </table>
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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body class="fs-1" class="p-4">
    <form style='background-color: #f2f2f2; padding: 20px; border-radius: 10px; width: 100%;' action="/generate" method="post" enctype="multipart/form-data">

    <div class="my-5">
        <h1 style="font-size: 5rem" class="text-center fw-bold ">Intan</h1>
        <h1 style="font-size: 5rem" class="text-center fw-bold ">Dental Laboratory</h1>
    </div>

    <div class="mb-3">
        <label for="num" class="form-label">Nomor:</label>
        <input class="form-control fs-1" type="number" id="num" name="num" />
    </div>

    <div class="mb-3">
        <label for="name" class="form-label">Nama Pasien:</label>
        <input class="form-control fs-1" type="text" id="name" name="name" />
    </div>

    <div class="mb-3">
        <label for="drg" class="form-label">Nama Dokter Gigi:</label>
        <input class="form-control fs-1" type="text" id="drg" name="drg" />
    </div>

    <div class="mb-3">
        <label for="job" class="form-label">Jenis Pekerjaan:</label>
        <input class="form-control fs-1" type="text" id="job" name="job" />
    </div>
    
    <div class="mb-3">
        <label for="order" class="form-label">Tanggal Pembuatan:</label>
        <input class="form-control fs-1" type="date" id="order" name="order" />
    </div>

    <div class="mb-3">
        <label for="send" class="form-label">Tanggal Kirim:</label>
        <input class="form-control fs-1" type="date" id="send" name="send" />
    </div>

    <div class="mb-3">
        <label for="lab" class="form-label">Alamat Laboratorium:</label>
        <input class="form-control fs-1" type="text" id="lab" name="lab" />
    </div>

    <div class="mb-3">
        <label for="hp" class="form-label">No Hp:</label>
        <input class="form-control fs-1" type="text" id="hp" name="hp" />
    </div>

    <div class="mb-3">
        <label for="photo" class="form-label">Gambar</label>
        <input class="form-control fs-1" type="file" id="photo" name="photo">
    </div>

    <input class="btn btn-primary w-100 fs-1 mt-5" type="submit" value="Submit" />
    </form>
</body>
</html>
"""
