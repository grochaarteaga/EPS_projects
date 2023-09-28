import streamlit as st
import json
import xmltodict

def main():
    st.title("Merchant Loop from MID and MCC codes")

    uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Read and parse the JSON file
        json_data = uploaded_file.read()
        try:
            json_obj = json.loads(json_data)
        except json.JSONDecodeError as e:
            st.error(f"Error parsing JSON file: {e}")
            return

        # Convert JSON to XML
        xml_data = xmltodict.unparse(json_obj, pretty=True)

        # Display the XML data
        st.header("Merchant Loop file in XML:")
        st.code(xml_data, language="xml")

if __name__ == "__main__":
    main()
