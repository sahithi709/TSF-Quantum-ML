from flask import Flask, render_template
import numpy as np
import pandas as pd
import os

app = Flask(__name__, static_folder="static")

# Column names from the dataset
COLUMNS = [
    "date", "p (mbar)", "T (degC)", "Tpot (K)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)",
    "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m³)", "wv (m/s)", "max. wv (m/s)", "wd (deg)",
    "rain (mm)", "raining (s)", "SWDR (W/m²)", "PAR (µmol/m²/s)", "max. PAR (µmol/m²/s)", "Tlog (degC)"
]

# Path to the .npy file
NPY_FILE_PATH = "./results/weather_336_96_QuLTSF_custom_nq10_ftM_sl336_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy"

@app.route("/")
def display_npy():
    try:
        if not os.path.exists(NPY_FILE_PATH):
            return "Error: .npy file not found!"

        data = np.load(NPY_FILE_PATH)

        if data.shape[2] != len(COLUMNS):
            return f"Error: Data has {data.shape[2]} columns, but expected {len(COLUMNS)}."

        df = pd.DataFrame(data[0], columns=COLUMNS)

        # Convert numeric date to datetime
        if np.issubdtype(df["date"].dtype, np.number):
            df["date"] = pd.date_range(start="2025-04-07 00:00:00", periods=len(df), freq="10T")

        return render_template("table.html", tables=[df.to_html(classes="table table-striped table-bordered", index=False)], title="Weather Data")

    except Exception as e:
        return f"Error loading data: {e}"

if __name__ == "__main__":
    app.run(debug=True)
