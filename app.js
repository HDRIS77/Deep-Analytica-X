const globe = Globe()

(document.getElementById('globe'))

.globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')

.backgroundColor('#0b0f1a')

.pointsData(events)

.pointAltitude('size')

.pointColor('color')

.pointRadius(0.2)

.onPointClick(point => {

alert(point.title)

})

globe.controls().autoRotate = true
globe.controls().autoRotateSpeed = 0.5
