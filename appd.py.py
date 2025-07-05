# from flask import Flask, render_template
# import numpy as np
# import pandas as pd

# app = Flask(__name__)

# # Define column names (based on your weather dataset)
# COLUMNS = ["date", "p (mbar)", "T (degC)", "Tpot (K)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)",
#            "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m³)", "wv (m/s)", "max. wv (m/s)", "wd (deg)",
#            "rain (mm)", "raining (s)", "SWDR (W/m²)", "PAR (µmol/m²/s)", "max. PAR (µmol/m²/s)", "Tlog (degC)"]


# # Path to the .npy file (update this to your file path)
# NPY_FILE_PATH = "./results/weather_336_96_QuLTSF_custom_nq10_ftM_sl336_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy"

# @app.route("/")
# def display_npy():
#     try:
#         # Load the .npy file
#         data = np.load(NPY_FILE_PATH)

#         # Convert only the first sample (96 time steps) into a DataFrame
#         df = pd.DataFrame(data[0], columns=COLUMNS)

#         # Render as an HTML table
#         return render_template("table.html", tables=[df.to_html(classes="table table-bordered")], title="Weather Data")

#     except Exception as e:
#         return f"Error loading data: {e}"


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template
# import numpy as np
# import pandas as pd
# import os

# app = Flask(__name__, static_folder="static")

# # Define column names (based on your weather dataset)
# COLUMNS = ["date", "p (mbar)", "T (degC)", "Tpot (K)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)",
#            "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m³)", "wv (m/s)", "max. wv (m/s)", "wd (deg)",
#            "rain (mm)", "raining (s)", "SWDR (W/m²)", "PAR (µmol/m²/s)", "max. PAR (µmol/m²/s)", "Tlog (degC)"]

# # Path to the .npy file (update this to your file path)
# NPY_FILE_PATH = "./results/weather_336_96_QuLTSF_custom_nq10_ftM_sl336_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy"

# @app.route("/")
# def display_npy():
#     try:
#         # Check if file exists
#         if not os.path.exists(NPY_FILE_PATH):
#             return "Error: .npy file not found!"

#         # Load the .npy file
#         data = np.load(NPY_FILE_PATH)

#         # Convert only the first sample (96 time steps) into a DataFrame
#         df = pd.DataFrame(data[0], columns=COLUMNS)

#         # Fix the "date" column if it's in float format
#         if np.issubdtype(df["date"].dtype, np.number):
#             df["date"] = pd.to_datetime(df["date"], unit="D", origin="1970-01-01")

#         # Render as an HTML table
#         return render_template("table.html", tables=[df.to_html(classes="table table-bordered")], title="Weather Data")
    
#     except Exception as e:
#         return f"Error loading data: {e}"

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template
import numpy as np
import pandas as pd
import os

app = Flask(__name__, static_folder="static")

# Define column names based on your dataset (Adding "date" as the first column)
COLUMNS = ["date", "p (mbar)", "T (degC)", "Tpot (K)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)",
           "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m³)", "wv (m/s)", "max. wv (m/s)", "wd (deg)",
           "rain (mm)", "raining (s)", "SWDR (W/m²)", "PAR (µmol/m²/s)", "max. PAR (µmol/m²/s)", "Tlog (degC)"]

# Path to the .npy file (Update this to your correct path)
NPY_FILE_PATH = "./results\weather_48_96_DLinear_custom_nq5_ftM_sl48_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy"
# NPY_FILE_PATH = "./results/weather_336_96_QuLTSF_custom_nq10_ftM_sl336_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy"

@app.route("/")
def display_npy():
    try:
        # Check if file exists
        if not os.path.exists(NPY_FILE_PATH):
            return "Error: .npy file not found!"

        # Load the .npy file
        data = np.load(NPY_FILE_PATH)

        # Ensure data has the correct shape
        if data.shape[2] != len(COLUMNS):
            return f"Error: Data has {data.shape[2]} columns, but expected {len(COLUMNS)}."

        # Convert only the first sample (96 time steps) into a DataFrame
        df = pd.DataFrame(data[0], columns=COLUMNS)

        # Fix the "date" column if it's in float format
        if np.issubdtype(df["date"].dtype, np.number):
            df["date"] = pd.date_range(start="2025-04-07 00:00:00", periods=len(df), freq="10T")

        # Render as an HTML table
        return render_template("table.html", tables=[df.to_html(classes="table table-striped table-bordered")], title="Weather Data")

    except Exception as e:
        return f"Error loading data: {e}"

if __name__ == "__main__":
    app.run(debug=True)

