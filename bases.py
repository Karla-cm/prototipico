
import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Curso: Prevención del Ciberfraude y Phishing", layout="wide")

# Menú lateral
menu = st.sidebar.radio("📋Navega por el curso", [
    "🏠Inicio",
    "🧩Módulo 1: ¿Qué es el ciberfraude?",
    "🧩Módulo 2: ¿Qué es el phishing?",
    "🧩Módulo 3: ¿Por qué los adultos mayores son vulnerables? (Factores tecnológicos, sociales y psicológicos).",
    "🧩Módulo 4: Señales de alerta",
    "🧩Módulo 5: Casos reales y estadísticas",
    "🧩Módulo 6: Buenas prácticas",
    "🧩Evaluación final"
])

# Contenido por módulo
if menu == "🏠Inicio":
    st.title("🔐Curso: Prevención del Ciberfraude y Phishing🔐")
    st.markdown("""
    🧠Bienvenido al curso interactivo sobre cómo protegerte del ciberfraude y el phishing🧠.

   📌En la era digital, los adultos mayores se han convertido en un grupo especialmente vulnerable ante el creciente fenómeno del fraude a través de dispositivos móviles. Este problema no solo representa un desafío tecnológico, sino también social, psicológico y ético, ya que afecta directamente su seguridad económica, su confianza en las herramientas digitales y su bienestar emocional. En muchos casos, esta población carece de las habilidades necesarias para identificar y evitar estafas en línea. 
   El fraude digital contra la tercera edad no puede abordarse desde una sola perspectiva. Por un lado, existe un componente tecnológico: los delincuentes aprovechan la falta de familiaridad de los adultos mayores con aplicaciones, mensajes de phishing o enlaces maliciosos. Por otro, hay un factor social: muchos ancianos viven solos o tienen redes de apoyo limitadas, lo que los hace más susceptibles a engaños. Además, el impacto psicológico es significativo, ya que, tras ser víctimas de fraude, pueden desarrollar desconfianza hacia la tecnología o incluso aislarse por miedo a nuevos ataques.
   
   🔍En este curso aprenderás a:

    ✅ Reconocer señales de alerta en correos, mensajes y sitios web.

    ❌ Evitar caer en fraudes comunes en redes sociales.

    🔒 Proteger tu información personal en línea.

   📋 Usa el menú lateral para navegar por los módulos.

    """)

elif menu == "🧩Módulo 1: ¿Qué es el ciberfraude?":
    st.header("🧩Módulo 1: ¿Qué es el ciberfraude?👨‍💻 / 👩‍💻")
    st.markdown("""
    El ciberfraude es un tipo de delito cometido a través de Internet o medios digitales, donde los ciberdelincuentes utilizan técnicas engañosas para obtener beneficios económicos, robar información personal o financiera, o causar daños a las víctimas.
    Modalidade comunes :

    ⚠️Phishing: Suplantación de identidad de instituciones financieras o empresas para robar datos bancarios mediante correos o mensajes falsos.

    ⚠️Smishing: Uso de mensajes SMS con enlaces fraudulentos que dirigen a páginas falsas.

    ⚠️Pharming: Redirección a sitios web falsos para capturar información confidencial.

    ⚠️Vishing: Llamadas telefónicas simulando ser empleados de bancos para obtener datos.

    ⚠️Malware: Software malicioso (como ransomware) que infecta dispositivos para extorsionar o robar información.

    ⚠️Ofertas engañosas: Promociones falsas en redes sociales o tiendas en línea que buscan estafar con pagos anticipados.
    
    """)

elif menu =="🧩Módulo 2: ¿Qué es el phishing?":
    st.header("🧩Módulo 2: ¿Qué es el phishing?")
    st.markdown("""
    🖥️El phishing es un tipo de ciberfraude que busca engañar a las personas para que revelen información personal, como contraseñas o datos bancarios. Los atacantes se hacen pasar por entidades de confianza (bancos, empresas, instituciones públicas) a través de correos electrónicos, mensajes de texto, llamadas telefónicas o sitios web falsos
    
    📲caracteristicas del phishing
    
    📟Suplantación de identidad:
    
    Los ciberdelincuentes imitan marcas legítimas (ej. Amazon, PayPal, bancos) usando logos y diseños similares para parecer auténticos.
    
    👩‍💻Tácticas de urgencia o miedo:

    Mensajes alarmantes como "¡Tu cuenta será bloqueada!" o "¡Actúa ahora!" para manipular emocionalmente a la víctima 
    
    🌐Enlaces o archivos maliciosos:

     Incluyen links a páginas falsas que imitan sitios reales (ej. una copia de la web de BBVA) o adjuntos infectados con malware
    
    📱Tipos comunes de phishing

     📤Phishing masivo: Correos genéricos enviados a miles de personas, esperando que algunos caigan 18.

     👫Spear phishing: Ataques personalizados con información específica de la víctima (ej. nombre, cargo laboral) .

     📞Smishing y vishing: Usan SMS o llamadas telefónicas para robar datos .

     📶 Whaling: Dirigido a ejecutivos de alto nivel para fraudes financieros .

     🛜Pharming: Redirige a sitios falsos incluso si la víctima escribe la URL correcta .

     """)

elif menu =="🧩Módulo 3: ¿Por qué los adultos mayores son vulnerables? (Factores tecnológicos, sociales y psicológicos":
    st.header("🧩Módulo 3: ¿Por qué los adultos mayores son vulnerables? (Factores tecnológicos, sociales y psicológicos.")
    st.markdown("""
    Aprende a identificar posibles señales de phishing:
    - Enlaces extraños o mal escritos
    - Correos urgentes que piden información confidencial
    - Ofertas que parecen demasiado buenas para ser verdad
    """)

elif menu == "Módulo 4: Casos reales y estadísticas":
    st.header("📊 Módulo 4: Casos reales y estadísticas")
    st.markdown("Aquí incluirás gráficas interactivas sobre fraudes detectados en tu base de datos. (Las agregamos en el siguiente paso)")

elif menu == "Módulo 4: Casos reales y estadísticas":
    import pandas as pd
    import plotly.express as px

    st.header("📊 Módulo 4: Casos reales y estadísticas")

    # Cargar datos
    df = pd.read_excel("filtered_data.xlsx")
    df["fecha_hecho"] = pd.to_datetime(df["fecha_hecho"], errors='coerce')
    df["hora_hecho"] = pd.to_datetime(df["hora_hecho"], format="%H:%M:%S", errors='coerce').dt.hour
    df["anio"] = df["fecha_hecho"].dt.year
    df["mes"] = df["fecha_hecho"].dt.month

    # Gráfica 1: Denuncias por alcaldía
    alcaldias = df["alcaldia_hecho"].value_counts().reset_index()
    alcaldias.columns = ["Alcaldía", "Cantidad"]
    fig1 = px.bar(alcaldias, x="Cantidad", y="Alcaldía", orientation="h", title="Denuncias por Alcaldía")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfica 2: Denuncias por mes y año
    mensual = df.groupby(["anio", "mes"]).size().reset_index(name="Cantidad")
    mensual["Fecha"] = pd.to_datetime(mensual["anio"].astype(str) + "-" + mensual["mes"].astype(str))
    fig2 = px.line(mensual, x="Fecha", y="Cantidad", title="Denuncias por Mes")
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfica 3: Denuncias por horario
    horario = df["hora_hecho"].value_counts().sort_index().reset_index()
    horario.columns = ["Hora", "Cantidad"]
    fig3 = px.bar(horario, x="Hora", y="Cantidad", title="Denuncias por Hora del Día")
    st.plotly_chart(fig3, use_container_width=True)

    # Gráfica 4: Top 10 colonias con más fraudes
    colonias = df["colonia_hecho"].value_counts().head(10).reset_index()
    colonias.columns = ["Colonia", "Cantidad"]
    fig4 = px.bar(colonias, x="Cantidad", y="Colonia", orientation="h", title="Top 10 Colonias con más Denuncias")
    st.plotly_chart(fig4, use_container_width=True)

    # Gráfica 5: Tipo de delito
    delitos = df["delito"].value_counts().reset_index()
    delitos.columns = ["Delito", "Cantidad"]
    fig5 = px.pie(delitos.head(10), values="Cantidad", names="Delito", title="Tipos de Delito más Comunes")
    st.plotly_chart(fig5, use_container_width=True)

elif menu == "Módulo 5: Buenas prácticas":
    st.header("🔒 Módulo 5: Buenas prácticas")
    st.markdown("""
    Algunas recomendaciones clave:
    - Usa contraseñas seguras y únicas
    - Verifica enlaces antes de hacer clic
    - Activa la autenticación de dos factores
    - Nunca compartas información sensible por mensaje o email
    """)

elif menu == "Evaluación final":
    st.header("📝 Evaluación final")
    st.markdown("Próximamente: incluir un pequeño cuestionario para validar lo aprendido.")
