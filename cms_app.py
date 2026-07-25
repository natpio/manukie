import streamlit as st
import pandas as pd

# Ustawienia strony
st.set_page_config(page_title="CMS Manufaktura", page_icon="🥩", layout="wide")

st.title("🥩 Panel Zarządzania - Manufaktura Kiełbas")
st.markdown("Edytuj asortyment, zmieniaj ceny i zarządzaj dostępnością produktów na stronie głównej.")

# Tutaj docelowo zepniesz się z Google Sheets API (np. biblioteką gspread lub st.connection)
# Na potrzeby startu interfejsu ładujemy przykładowe dane:
@st.cache_data
def load_data():
    return pd.DataFrame({
        "ID": ["prod_001", "prod_002", "set_001"],
        "Kategoria": ["Menu", "Menu", "Zestawy"],
        "Nazwa": ["Kiełbasa Tradycyjna", "Kiełbasa Czosnkowa", "Grill Box Premium"],
        "Opis": ["100% mięsa wieprzowego...", "Zdecydowany aromat czosnku...", "Zestaw bestsellerów..."],
        "Cena": [29.90, 32.90, 109.00],
        "Dostępny": [True, True, True]
    })

df = load_data()

st.subheader("Baza Produktów")

# Interaktywny edytor tabeli (nowość w Streamlit, idealna do CMS)
edited_df = st.data_editor(
    df, 
    num_rows="dynamic", # Pozwala na dodawanie nowych wierszy z poziomu interfejsu
    use_container_width=True,
    column_config={
        "Cena": st.column_config.NumberColumn(
            "Cena (zł)",
            help="Cena brutto w PLN",
            min_value=0.0,
            format="%.2f zł"
        ),
        "Dostępny": st.column_config.CheckboxColumn(
            "Widoczny na stronie?",
            help="Odznacz, aby ukryć produkt w sklepie",
            default=True,
        )
    }
)

# Przycisk zapisu (docelowo wyśle dane z powrotem do Google Sheets)
if st.button("💾 Zapisz zmiany w Arkuszu"):
    # Tutaj wpadnie logika zapisu gspread / API
    st.success("Zmiany zostały pomyślnie zapisane! Sklep zaktualizuje się automatycznie.")
