window.onscroll = function() {
  stick()
};

var navbar = document.getElementById("navi");
var sticky = navbar.offsetTop;

function stick() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
// MODAL
var modal = document.getElementById('box');
var img = $('.photo');
var modalImg = $("#img");

$('.photo').click(function() {
  modal.style.display = "block";
  var newSrc = this.src;
  modalImg.attr('src', newSrc);
});

window.onclick = function(event) { // click outside modal
  if (event.target == modal) {
    modal.style.display = "none";
  }
}