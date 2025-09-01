import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# -------------------
# CONFIGURACIÓN INICIAL
# -------------------
st.set_page_config(page_title="Encuesta de Satisfacción", page_icon="🧪", layout="centered")

st.image("logo_crb.png", width=200)  # Logo CRB (debes subirlo al repo)
st.title("Encuesta de Satisfacción – Toma de Muestras")
st.write("Tu opinión es muy importante para mejorar nuestro servicio. Responde estas 3 preguntas en menos de 2 minutos.")

# -------------------
# FORMULARIO
# -------------------
expectativas = st.text_area("1. ¿Cuáles son tus expectativas de una toma de muestra?")
cumplimiento = st.radio("2. ¿Fueron cumplidas tus expectativas en esta atención?", ["Sí", "Parcialmente", "No"])
mejoras = st.text_area("3. ¿Qué esperas de la toma de muestra para cumplir mejor tus expectativas y satisfacción?")

if st.button("Enviar respuesta"):
    # Guardar en CSV
    nueva_respuesta = {
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Expectativas": expectativas,
        "Cumplimiento": cumplimiento,
        "Mejoras": mejoras
    }

    try:
        df = pd.read_csv("respuestas_encuesta.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Fecha", "Expectativas", "Cumplimiento", "Mejoras"])

    df = pd.concat([df, pd.DataFrame([nueva_respuesta])], ignore_index=True)
    df.to_csv("respuestas_encuesta.csv", index=False)

    # Enviar por correo (opcional: configura SMTP)
    try:
        msg = MIMEText(f"""
        Nueva respuesta recibida:
        Expectativas: {expectativas}
        Cumplimiento: {cumplimiento}
        Mejoras: {mejoras}
        """)
        msg["Subject"] = "Nueva respuesta – Encuesta de Satisfacción"
        msg["From"] = "tu_correo@gmail.com"
        msg["To"] = "destinatario@crb.cl"

        # Configuración SMTP (ejemplo Gmail)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("tu_correo@gmail.com", "tu_password_app")
            server.send_message(msg)
    except Exception as e:
        st.warning("⚠️ No se pudo enviar el correo (configura SMTP).")

    st.success("✅ ¡Gracias por tu opinión! Tu respuesta ha sido registrada.")
