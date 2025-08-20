function izracunaj() {
  var racun = document.getElementById("racunInput").value;
  
  racun = racun.replace("x", "*");
  racun = racun.replace("÷", "/");
  racun = racun.replace("^","**");

  document.getElementById("zgodovina").innerHTML += "<br>"+racun.slice(-15);
  document.getElementById("racunInput").value = eval(racun);
}

var gumbi = document.getElementsByClassName("grid-gumb")
for (var i = 0; i < gumbi.length; i++) {
  gumbi[i].onclick = gumb_click;
}

function gumb_click (){
  var vrednost = this.innerText;
  if (vrednost == "AC"){
    document.getElementById("racunInput").value = ""
  } else {
    document.getElementById("racunInput").value += vrednost;
  }
}

function backspace(){
  document.getElementById("racunInput").value = document.getElementById("racunInput").value.slice(0,-1);
}

document.getElementById('zgodovinaIzracunov').onclick = function() {
  document.getElementById('zgodovinaOkno').style.display = 'block';
  document.getElementById('ozadje').style.display = 'block'; // če uporabljaš zatemnitev
};

document.getElementById('zapriZgodovino').onclick = function() {
  document.getElementById('zgodovinaOkno').style.display = 'none';
  document.getElementById('ozadje').style.display = 'none'; // če uporabljaš zatemnitev
};

const so = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "÷", "x", "^"];
function handleKeyDown(e) {
  // Tipka je bila pritisnena
  console.log("Tipka", e.key);
  if(e.key == "Enter"){
    izracunaj();
  } else if(e.key == "Backspace"){
    backspace();
  } else if(so.indexOf(e.key) != -1){
    document.getElementById("racunInput").value += e.key;
  }
}
document.onkeydown = handleKeyDown;
document.getElementById("racunInput").onfocus  = function(){
  document.getElementById("racunInput").blur();
}
