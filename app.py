from flask import Flask, render_template, request, abort
import pickle
import pandas as pd
import os

app = Flask(__name__)

# ---------------- Load model ----------------
with open("RF.pkl", "rb") as f:
    model = pickle.load(f)

# --------- FORM fields shown on index.html (keep your UI) ----------
FORM_FIELDS = [
    "i", "z", "modelFlux_z",
    "petroRad_g", "petroRad_r", "petroFlux_z",
    "petroR50_u", "petroR50_g", "petroR50_i", "petroR50_r",
]

# --------- Map form fields -> model features ----------
# Your model expects "u" (not "i"). Map it here.
# If the model expects more/other names, add mappings similarly.
FORM_TO_MODEL_MAP = {
    # model_feature : form_field
    "u": "i",            # <-- key fix (model expects 'u'; take value from 'i' input)
    # others default to same name
}

# Try to read the actual feature names the model expects (sklearn >= 1.0)
MODEL_FEATURES = list(getattr(model, "feature_names_in_", []))
if not MODEL_FEATURES:
    # If the model doesn't expose names, fall back to assuming same as form fields,
    # but apply the explicit mapping if present.
    MODEL_FEATURES = [k if k not in FORM_TO_MODEL_MAP else k for k in FORM_FIELDS]

# ---------------- Routes ----------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get-started")
def get_started():
    defaults = {
        "i": 16.813, "z": 16.59408, "modelFlux_z": 230.3376,
        "petroRad_g": 3.955328, "petroRad_r": 4.087168, "petroFlux_z": 201.0571,
        "petroR50_u": 1.613005, "petroR50_g": 1.766743,
        "petroR50_i": 1.74353, "petroR50_r": 1.784977
    }
    return render_template("index.html", features=FORM_FIELDS, defaults=defaults)

@app.route("/predict", methods=["POST"])
def predict():
    # Build a dict: model_feature -> float value from form
    row = {}
    for mf in MODEL_FEATURES:
        # which form field supplies this model feature?
        form_field = FORM_TO_MODEL_MAP.get(mf, mf)
        raw = request.form.get(form_field)
        if raw is None:
            abort(400, f"Missing input for '{form_field}' (needed for model feature '{mf}')")
        try:
            row[mf] = float(raw)
        except ValueError:
            abort(400, f"Invalid number for '{form_field}'")

    X = pd.DataFrame([row], columns=MODEL_FEATURES)

    pred = model.predict(X)
    pred_val = pred[0] if hasattr(pred, "__len__") else pred

    # Adjust mapping if your model already outputs strings
    label = "starforming" if int(pred_val) == 0 else "starbursting"

    return render_template("output.html", prediction=label)

if __name__ == "__main__":
    # Optional: if you don’t have /static/space.jpg, remove it from home.html or place a file there
    app.run(port=2222, debug=True)
