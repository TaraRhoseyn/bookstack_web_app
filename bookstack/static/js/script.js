/* jshint esversion: 6 */

// Init Materialize components
$(document).ready(function () {
  $(".sidenav").sidenav();
  $(".button-collapse").sidenav();
  $(".collapsible").collapsible();
  $(".tooltipped").tooltip();
  $("select").formSelect();
});

// Remove or show more form content depending on if user has read book
// Credit: Stack Overflow
// Bug fix: use classList.toggle instead of if/else logic
$("#read_status").on("click", showFormContent);
function showFormContent(){
  document.getElementById('extra-content').classList.toggle("hidden");
}