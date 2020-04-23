var modal = document.getElementById('box');
var img = $('.card-img-top');
var modalImg = $("#img");
$('.card-img-top').click(function() {
  modal.style.display = "block";
  var newSrc = this.src;
  modalImg.attr('src', newSrc);
});

window.onclick = function(event) { // click outside modal
  if (event.target == modal) {
    modal.style.display = "none";
  }
}