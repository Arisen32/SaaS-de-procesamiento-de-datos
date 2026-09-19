from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile
from .serializers import UploadedFileSerializer # Lo crearemos en un momento o usaremos validación directa
from .tasks import procesar_archivo_pesado

class UploadFileView(APIView):
    def post(self, request, *format):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"error": "No se proporcionó ningún archivo."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Guardar el registro en la base de datos
        uploaded_file = UploadedFile.objects.create(
            file=file_obj,
            status='pending',
            progress=0
        )
        
        # Disparar la tarea asíncrona en Celery pasándole el ID del registro
        procesar_archivo_pesado.delay(uploaded_file.id)
        
        return Response({
            "message": "Archivo subido correctamente. Procesamiento iniciado en segundo plano.",
            "file_id": uploaded_file.id,
            "status": uploaded_file.status
        }, status=status.HTTP_201_CREATED)