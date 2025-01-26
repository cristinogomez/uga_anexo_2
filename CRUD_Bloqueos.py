import streamlit as st
import datetime as dt
from datetime import datetime,timedelta
import pandas as pd

def crud_bloqueo():
    st.subheader("Bloqueos Agendas COT")

    df = pd.read_csv("COT.csv",encoding='utf-8', parse_dates=['Fecha'])

    df_mask = df["Bloqueos"] >0
    filtered_df = df[df_mask]
    listado_medicos=df['Medico'].unique()
    listado_agendas=df['Agenda'].unique()
    with st.form("my_form"):
            edited_df = st.data_editor(filtered_df,
                        width=800,
                        height=540,
                        column_config={
                                        "Fecha": st.column_config.DateColumn("Fecha del bloqueo",format="DD/MM/YYYY"),
                                        "Medico": st.column_config.SelectboxColumn("Facultativo", options=listado_medicos),
                                        "Agenda": st.column_config.SelectboxColumn("Agenda",options=listado_agendas),
                                        "Bloqueos":st.column_config.NumberColumn("Número de huecos bloqueados",
                                                                                                    min_value=0,
                                                                                                    max_value=7,
                                                                                                    default=2,
                                                                                                    step=1)},
                                            num_rows='dynamic',use_container_width=True)          
                
            boton_guardar=st.form_submit_button('Save')

            if boton_guardar:
                    df2 = pd.DataFrame(edited_df)
            
                    df2.to_csv('COT.csv',index=False)

                    mensaje=st.success('Los datos se han guardado corecctamente')

                    st.rerun



       