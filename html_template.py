
def html(contenido):
    template_html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/style.css">
    <meta name="author" content="Daniela Mercado">
    <meta name="description" content="Aves de Chile">
    <meta name="keywords" content="aves, chile, blog">

    <!-- --------------- BOOTSTRAP --------------- -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- ---------------- FAVICON ---------------- -->
    <link rel="icon" href="https://aves.ninjas.cl/api/site/assets/files/3131/17082018025342blanquillo_pedro_valencia_web.200x0.jpg">

    <title>Aves de Chile</title>
</head>

<body style="background-color: #FFEEDB;">
    <div class="container">
        <h1 class="text-center mt-3" style="color: #4D342E;font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><u>Aves de Chile</u></h1>
        <br>
        <div class="row">
            {contenido}
        </div>
    </div>

        <!-- ------------- BOOTSTRAP JS -------------- -->

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
'''
    return template_html