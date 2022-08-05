xmlHttp = new XMLHttpRequest();

function sendPlayer() {
var nameM = document.getElementById("playername").value;
    if (xmlHttp.readyState == 0 || xmlHttp.readyState == 4) {
        var p = "/stats?playername=" + nameM;
        xmlHttp.open('GET', p, true);
        xmlHttp.onreadystatechange = readPlayer;
        xmlHttp.send(null);
    }
}

function readPlayer() {
    document.getElementById("resp").innerHTML = this.responseText;
}

function onEnter(keyCode) {
if (event.keyCode == 13) {
        sendPlayer();
    }
}
