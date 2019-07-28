const sidebar = document.querySelector(".sidebar");
const treecont = document.querySelector(".tree-container");
const leaderboard = document.querySelector(".leaderboard-container");
let treeslist = new Array();
let myemail = "";
let numTrees = 0;
let ifHomePage = "";

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
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    }).addTo(map);

const addTree = (index, email, latlng, bool) => {
  ifHomePage = bool;
  L.marker( latlng, {icon: treeicn} ).addTo(map)
   .bindPopup("Planted by " + email + "<br><center>on " + currDate() + "<br>Tree #" + index + "</center>");

  if(bool == "true"){
    addToMySide(index, email, latlng);
  } // add elements to the sidebar treeslist
}

const addToMySide = (index, email, latlng) => {
  latlng.lat = parseFloat(latlng.lat.toFixed(5));
  latlng.lng = parseFloat(latlng.lng.toFixed(5));
  const headerElements = document.getElementsByClassName("tree-container");
  var listElement = document.createElement("div");
  listElement.className += "tree-obj";
  var text = document.createElement("p");
  text.innerHTML = "Tree #" + index + ": [" + latlng.lat + " , " + latlng.lng + "]" +
                     "<br>on " + currDate();
  listElement.appendChild(text);
  treecont.appendChild(listElement);
  numTrees = index;
}

const addToLeaderboard = (index, username, num) => {
  if(ifHomePage == "false"){
    var boardElement = document.createElement("div");
    boardElement.className += "tree-obj";
    var text = document.createElement("p");
    text.className += "leaderboard-font";
    text.innerHTML = "#" + index + ":\xa0\xa0\xa0" + username + "\xa0\xa0\xa0 " + num + " trees";
    boardElement.appendChild(text);
    leaderboard.appendChild(boardElement);
  }
}

const addOtherTree = (email, latlng) => {
  latlng.lat = parseFloat(latlng.lat.toFixed(5));
  latlng.lng = parseFloat(latlng.lng.toFixed(5));
  console.log(latlng);

      L.marker( latlng, {icon: treeicn} ).addTo(map)
       .bindPopup("Planted by " + email + "<br><center>on " + currDate());
       // add elements to the sidebar treeslist
}

const updateTree = (size) =>{
  var side = document.getElementById("tree-container");   // Get the <ul> element with id="myList"
  if(size == 1){
    side.removeChild(side.childNodes[0]);
  }
}

const ifNoTrees = (size) => {
  var side = document.getElementById("tree-container");   // Get the <ul> element with id="myList"
  if(size == 0){
    var text = document.createElement("p");
    var listElement = document.createElement("div");
    listElement.className += "tree-obj";
    text.innerHTML = "No trees planted yet. <br>Click on the map to plant a tree at your desired location.";
    listElement.appendChild(text);
    side.appendChild(listElement);
  }
}

const currDate = () => {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  return mm + '/' + dd + '/' + yyyy;
  }

const setCurrEmail = (email) => {
  myemail = email;
  }

map.on('click', function(e) {
   numTrees++;
   addTree(numTrees, myemail, e.latlng, ifHomePage);
   if(ifHomePage == "true"){
     updateTree(numTrees);
   }
   var mydate = currDate();
   const treeData = {
      'coordinates': e.latlng,
      'number': numTrees,
      'date': mydate,
    }
   fetch("/tree", {
     method: 'post',
     body: JSON.stringify(treeData),
   });
});

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
