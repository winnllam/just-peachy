var modal = document.getElementById('box');
var img = $('.pic');
var modalImg = $("#img");
var captionText = document.getElementById("caption");
$('.pic').click(function() {
  modal.style.display = "block";
  var newSrc = this.src;
  modalImg.attr('src', newSrc);
  captionText.innerHTML = this.alt;
});

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
  modal.style.display = "none";
}