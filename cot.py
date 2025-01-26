
import streamlit as st
import datetime as dt
from datetime import datetime,timedelta
import pandas as pd

def cot():    
    st.subheader("Bloqueos Agendas COT")

    df = pd.read_csv("COT.csv",encoding='utf-8', parse_dates=['Fecha'])

    
    col3,col4 = st.columns([2, 1])
    with col3:
        with st.container(border=True):
            par_rango_fecha=st.date_input('Rango de Fechas',value= (datetime.now(),(datetime.now()+timedelta(1))),format='DD/MM/YYYY')

            #listado_medicos=df['Medico'].unique()
            #med=st.selectbox('Medico',listado_medicos)
            #df_filtrado_medico = df[df['Medico']== med]

            if len(par_rango_fecha)==2:     
                df_Fechas=df[(df['Fecha']>= str(par_rango_fecha[0])) &  (df['Fecha']<= str(par_rango_fecha[1]))]
                st.dataframe(df_Fechas,hide_index=True,use_container_width=800)
                st.metric('Total Huecos Bloquedos',value=int(df_Fechas["Bloqueos"].sum()))
            else:
                df_Fechas=df[df['Fecha']== str(datetime.now())]
                st.dataframe(df_Fechas,hide_index=True,use_container_width=800, column_config=
                             {"Fecha": st.column_config.DateColumn("Fecha del bloqueo",format="DD/MM/YYYY")})
                st.metric('Total Huecos Bloquedos',value=int(df_Fechas["Bloqueos"].sum()))
                 
    with col4:
        with st.container(border=True):
    
            st.subheader("Notificaciones")

            df['Fecha']= pd.to_datetime(df['Fecha'])
            fechaTarget = dt.date.today()+dt.timedelta (days = 7)

            df_filtrado=df[df['Fecha']<= str(fechaTarget)]
            
            st.text('Huecos bloquedos que se deben citar:')
            with st.container(border=True):
                st.dataframe(df_filtrado,hide_index=True)
            df_bloqueosbymedico=df.groupby(['Medico'])['Bloqueos'].sum()
            st.text('Número de bloqueos por médico:')
            with st.container(border=True):
                st.dataframe(df_bloqueosbymedico,hide_index=False)
