import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

st.title("🌍 Global Monitor")

st.markdown("Live Global Events Map")

# جلب بيانات الزلازل
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

response = requests.get(url)
data = response.json()

points = []

for eq in data["features"]:

    lat = eq["geometry"]["coordinates"][1]
    lng = eq["geometry"]["coordinates"][0]
    mag = eq["properties"]["mag"]
    place = eq["properties"]["place"]

    points.append({
        "lat": lat,
        "lng": lng,
        "size": mag,
        "label": place
    })

points_json = json.dumps(points)

html = f"""

<head>

<script src="https://unpkg.com/three"></script>
<script src="https://unpkg.com/globe.gl"></script>

<style>

body {{
margin:0;
background:#0a0f1f;
color:white;
}}

#globe {{
width:100%;
height:90vh;
}}

.topbar {{

position:absolute;
top:10px;
left:20px;
z-index:10;

}}

.tension {{

padding:6px 12px;
border:1px solid #00ff9c;
border-radius:10px;
color:#00ff9c;

}}

</style>

</head>

<body>

<div class="topbar">

<h2>GLOBAL MONITOR</h2>

<div class="tension">
GLOBAL TENSION: LOW
</div>

</div>

<div id="globe"></div>

<script>

const events = {points_json}

const globe = Globe()

(document.getElementById('globe'))

.globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')

.backgroundColor('#0a0f1f')

.pointsData(events)

.pointAltitude(d => d.size/10)

.pointColor(() => "red")

.pointRadius(0.3)

.onPointClick(d => alert(d.label))

globe.controls().autoRotate = true
globe.controls().autoRotateSpeed = 0.4

</script>

</body>

"""

st.components.v1.html(html, height=800, scrolling=False)
