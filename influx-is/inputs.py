# -----------------------------------------------
# specify your InfluxDB details
influx_bucket = "gtc"
token = "EpDlIhrGqCwHSjzbCNcwYc0YcNTDT0l0gq5nXpwmcHEmZL_8PIazFcI38oJ52m4wCVOxOWuPUFdGKifV3zN_4g=="
influx_url = "http://localhost:8086"
org_id = "a51b5da644fbc997"

# -----------------------------------------------
# specify devices to process (from a local folder or S3 bucket)
devices = ["gtc/67DC524E"]

# -----------------------------------------------
# specify DBC paths and a list of signals to process ([]: include all signals)
dbc_paths = ["/work/BancoDePruebas.dbc"]
signals = []

# specify resampling frequency ("": no resampling)
res = "1S"

# -----------------------------------------------
# specify whether to load data from S3 (and add server details if relevant)
s3 = True
key = "bancodepruebas"
secret = "bancodepruebas"
endpoint = "http://161.72.123.165:9000"  # e.g. http://s3.us-east-1.amazonaws.com or http://192.168.0.1:9000
cert = "/etc/ssl/certs/ca-certificates.crt"  # if MinIO + TLS, add path to cert and update utils.py/setup_fs to verify

# -----------------------------------------------
# if dynamic = True, data is loaded dynamically based on most recent data in InfluxDB - else default_start is used
dynamic = True
default_start = "2022-01-01 00:00:00"
days_offset = None  # offsets data to start at 'today - days_offset'. Set to None to use original timestamps

# if you're using data encryption, you can add the password below
pw = {"default": "password"}

# if you need to process multi-frame data, set tp_type to "uds", "j1939" or "nmea"
tp_type = ""
