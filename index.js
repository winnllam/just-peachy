$(document).ready(function() {
  $("a").on('click', function(event) { // all links
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();
      var hash = this.hash;

      $('html, body').animate({ // animate to add smooth scroll
        scrollTop: $(hash).offset().top
      }, 650, function() { // (800) milliseconds

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    }
  });
});