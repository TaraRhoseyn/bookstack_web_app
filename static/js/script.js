/* jshint esversion: 6 */

$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".button-collapse").sideNav();
  });

$("#read_status").on("click", showFormContent);

// Remove or show more form content depending on if user has read book
// Credit: Stack Overflow
function showFormContent(){

  var formContent = document.getElementById('extra-content')

  if (formContent.style.display == "none") {
    formContent.style.display = 'block';
  } else {
    formContent.style.display = "none";
  }
}