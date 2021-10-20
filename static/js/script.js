/* jshint esversion: 6 */

$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".button-collapse").sideNav();
  });

$("#read_status").on("click", showFormContent);

// Remove or show more form content depending on if user has read book
// Credit: Stack Overflow
// Bug fix: use classList.toggle instead of if/else logic
function showFormContent(){
  document.getElementById('extra-content').classList.toggle("hidden");
}