

def cards(arg1, arg2, arg3):
    contenido = ''
    for i, j, k in zip(arg1, arg2, arg3):
        contenido += f'''

    <div class="col-12 col-md-3 mb-5">
        <div class="card shadow-sm">
        <div class="card-body text-light text-center p-2 rounded-top" style="background-color: #AC7E72;">
            <h5 class="card-title text-center">{i}</h5>
            <p class="card-text text-center">{j}</p>
        </div>
        <img src="{k}" class="card-img-bottom w-100 d-block" style="min-height: 19rem;" alt="{i} / {j}">
        </div>    
    </div>
        

    '''
    return contenido