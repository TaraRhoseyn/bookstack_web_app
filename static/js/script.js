/* jshint esversion: 6 */

$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".button-collapse").sideNav();
  });


$("#read_status").on("click", toggleDropdown);

// Remove or show more form content depending on if user has read book
function toggleDropdown(){

  var dropdown = document.getElementById('extra-content')

  if (dropdown.style.display == "none") {
    dropdown.style.display = 'block';
  } else {
    dropdown.style.display = "none";
  }
}