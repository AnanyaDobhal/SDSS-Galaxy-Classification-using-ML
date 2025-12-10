{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8c8d3364-6333-468c-8a68-3b5ffdf59e36",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import json\n",
    "import pickle\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import requests\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "169e2a65-d384-47f3-aca0-3ad3171abdf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "#load the trained model\n",
    "with open('RF.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fa93c921-9b95-4469-9e4a-a4aa3e1243b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"home.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9a17a451-3d9c-4b10-b243-57d5fd979196",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/submit', methods=['POST'])\n",
    "def submit():\n",
    "    # Read input values from the form (preserves order)\n",
    "    input_feature = [float(x) for x in request.form.values()]\n",
    "\n",
    "    # Feature names MUST match training order\n",
    "    names = [\n",
    "        'i', 'z', 'modelFlux_z',\n",
    "        'petroRad_g', 'petroRad_r', 'petroFlux_z',\n",
    "        'petroR50_u', 'petroR50_g', 'petroR50_i', 'petroR50_r'\n",
    "    ]\n",
    "\n",
    "    # Debug checks\n",
    "    print(\"Number of columns in names:\", len(names))\n",
    "    print(\"Number of columns in input_feature:\", len(input_feature))\n",
    "    print(\"Column names:\", names)\n",
    "\n",
    "    # Create DataFrame\n",
    "    data = pd.DataFrame([input_feature], columns=names)\n",
    "\n",
    "    # Make prediction\n",
    "    prediction = model.predict(data)\n",
    "\n",
    "    # Render output\n",
    "    if prediction == 0:\n",
    "        print(prediction)\n",
    "        return render_template('output.html', prediction='starforming')\n",
    "    else:\n",
    "        return render_template('output.html', prediction='starbursting')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "437658a1-d21c-4efd-941e-aa8577b64af2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:2222\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(port=2222, debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b4439bf-7959-4f1f-9c6a-007e03cc7479",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
