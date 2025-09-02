# Encuesta Satisfacción CRB

## Instrucciones para ejecutar localmente
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Crea un archivo `.env` con tus credenciales de Gmail.
3. Ejecuta:
   ```bash
   streamlit run app.py
   ```

## Despliegue en Streamlit Cloud
1. Sube todos los archivos al repositorio.
2. En **Settings → Secrets**, agrega:
   ```
   SMTP_USER="muestrascrb@gmail.com"
   SMTP_PASS="yhyeuufweuxhhhie"
   ```
3. Despliega la app y abre la URL generada.
