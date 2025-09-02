import streamlit as st
import pandas as pd
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

st.title("Encuesta de Satisfacción CRB")

# Formulario
nombre = st.text_input("Nombre")
correo = st.text_input("Correo")
satisfaccion = st.slider("Nivel de Satisfacción", 1, 5, 3)
comentarios = st.text_area("Comentarios")

if st.button("Enviar"):
    # Guardar respuestas
    df = pd.DataFrame([[nombre, correo, satisfaccion, comentarios]],
                      columns=["Nombre", "Correo", "Satisfacción", "Comentarios"])
    if os.path.exists("respuestas_encuesta.csv"):
        df.to_csv("respuestas_encuesta.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("respuestas_encuesta.csv", index=False)
    
    # Enviar correo
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = correo
        msg["Subject"] = "Resumen Encuesta Satisfacción CRB"
        body = f"Gracias {nombre} por completar la encuesta.\nNivel de satisfacción: {satisfaccion}\nComentarios: {comentarios}"
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, correo, msg.as_string())
        
        st.success("¡Encuesta enviada y correo enviado correctamente!")
    except Exception as e:
        st.error(f"Error al enviar correo: {e}")
