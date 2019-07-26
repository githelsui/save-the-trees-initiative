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

const map = L.map('canvas').setView([33.99893452860995, -118.48341822624205], 14);

const addTree = (index, email, latlng) => {
  latlng.lat = parseFloat(latlng.lat.toFixed(5));
  latlng.lng = parseFloat(latlng.lng.toFixed(5));
  console.log(latlng);
  mapLink =
      '<a href="http://openstreetmap.org">OpenStreetMap</a>';
  L.tileLayer(
      'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; ' + mapLink + ' Contributors',
      maxZoom: 18,
      }).addTo(map);

      L.marker( latlng, {icon: treeicn} ).addTo(map)
       .bindPopup("Planter: " + email + "<br>Tree #" + index);
       // add elements to the sidebar treeslist
       var listElement = document.createElement("div");
       listElement.className += "tree-obj";
       var text = document.createElement("p");
       text.innerHTML = "Tree #" + index + ": " + email + ": [" + latlng.lat + " , " + latlng.lng + "]";
       listElement.appendChild(text);
       treecont.appendChild(listElement);
       numTrees = index;
}


//
// const popUp = (email, marker) =>{
//     marker.bindPopup(email + "\n Tree #" + numTrees);
// };
