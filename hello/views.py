from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Create your views here.

@csrf_exempt
def webhook(request):
    # --- Verificación del Webhook ---
    if request.method == "GET":
        # Extrae el verify_token y otros parámetros de la petición de Meta
        verify_token = os.environ.get("WHATSAPP_VERIFY_TOKEN")
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        # Comprueba si el modo y el token son correctos
        if mode == "subscribe" and token == verify_token:
            # Responde con el challenge para verificar el webhook
            print("WEBHOOK_VERIFIED")
            return HttpResponse(challenge, status=200)
        else:
            # Si no coincide, responde con un error
            return HttpResponse("error", status=403)

    # --- Recepción de Mensajes ---
    if request.method == "POST":
        # Procesa el cuerpo de la petición (los datos del mensaje)
        data = json.loads(request.body)
        print("Received webhook data: ", json.dumps(data, indent=2))
        
        # Aquí es donde, en el futuro, pondremos la lógica de Gemini.
        # Por ahora, simplemente confirmamos que recibimos el mensaje.
        
        # Devuelve una respuesta 200 para que WhatsApp sepa que lo recibimos bien.
        return HttpResponse("success", status=200)

    # Si no es GET o POST, responde con un error
    return HttpResponse("Unsupported method", status=405)
