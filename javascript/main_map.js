const sidebar = document.querySelector(".sidebar");
const treecont = document.querySelector(".tree-container");
let treeslist = new Array();
let numTrees = 0;

const treeicn = L.icon({
    iconUrl: 'https://img.icons8.com/color/52/000000/deciduous-tree.png',
    // shadowUrl: 'https://img.icons8.com/bubbles/26/000000/deciduous-tree.png',

    iconSize:     [56, 56], // size of the icon
    // shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [24, 56], // point of the icon which will correspond to marker's location
    // shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

var map = L.map('canvas').setView([33.99893452860995, -118.48341822624205], 14);
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 18,
    }).addTo(map);

map.on('click', function(e) {
   numTrees++;
   L.marker(e.latlng, {icon: treeicn, draggable: true, markerId: 9999}).addTo(map)
    .bindPopup("Planter: " + '{{email}}' + "<br>Tree #" + numTrees);
   console.log(e);
   fetch("/tree", {
     method: 'post',
     body: JSON.stringify(e.latlng),
   });
});
//
// const popUp = (email, marker) =>{
//     marker.bindPopup(email + "\n Tree #" + numTrees);
// };
