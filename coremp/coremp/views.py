from django.shortcuts import render, get_object_or_404
from .models import Plan  # Asegúrate de importar tu modelo Plan

# Otras vistas que ya tengas...

def pago(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    
    if request.method == 'POST':
        # Aquí procesarías el formulario cuando se envía
        nombre_facturacion = request.POST.get('nombre_facturacion')
        direccion_facturacion = request.POST.get('direccion_facturacion')
        metodo_pago = request.POST.get('metodo_pago')
        
        # Aquí puedes añadir lógica para procesar el pago
        # Por ejemplo, guardar la información en la base de datos
        # o redirigir a una página de confirmación
        
        # Por ahora, simplemente renderizamos la misma página
        return render(request, 'pago_confirmado.html', {
            'plan': plan,
            'nombre': nombre_facturacion
        })
    
    # Si es una solicitud GET, simplemente mostramos el formulario
    return render(request, 'pago.html', {'plan': plan})


<!-- pago_confirmado.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Pago Confirmado - Coremp</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
        .container { max-width: 800px; margin: 50px auto; padding: 20px; text-align: center; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #0078d4; }
        a { color: #0078d4; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Pago Procesado con Éxito!</h1>
        <p>Gracias, <strong>{{ nombre }}</strong>, por tu compra.</p>
        <p>Has adquirido el plan: <strong>{{ plan.nombre }}</strong></p>
        <p>Precio mensual: ${{ plan.precio_mensual }}</p>
        <p>Te hemos enviado un correo electrónico con los detalles de tu compra.</p>
        
        <p><a href="{% url 'publico_registrado' %}">Volver a la página principal</a></p>
    </div>
</body>
</html>
