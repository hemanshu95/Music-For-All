var _player = document.getElementById("player"),
	_playlist = document.getElementById("playlist");
//_player.loop=true;
_player.src = _playlist.querySelector("li").getAttribute("data-mp3");
_player.play();
var current_li=_playlist.querySelector("li");

function playlistItemClick(clickedElement) {
    var selected = _playlist.querySelector(".selected");
    if (selected) {
        selected.classList.remove("selected");
    }
    clickedElement.classList.add("selected");
    current_li=clickedElement;

    _player.src = clickedElement.getAttribute("data-mp3");
    _player.play();
}

_player.addEventListener('ended', function() {
      //  alert("OVERhello"+current_li.nextElementSibling.innerHTML);

   //this.currentTime = 0;
   if (current_li.nextElementSibling) {
    //alert("OVERhelloworld"+current_li.nextElementSibling);

        //this.currentSrc =current_li.nextElementSibling.getAttribute("data-mp3");
        current_li=current_li.nextElementSibling;

        //this.play();
        //playlistItemClick(selected.nextSibling);
    }
    else
    {
        current_li=_playlist.querySelector("li");
    }
    this.src =current_li.getAttribute("data-mp3");
    current_li.selected=true;
    this.load();
    this.play();
}, false);

_playlist.addEventListener("click", function (e) {
    if (e.target && e.target.nodeName === "LI") {
        playlistItemClick(e.target);
    }
});