/* jshint esversion: 6 */

// Init Materialize components
$(document).ready(function () {
  $(".sidenav").sidenav();
  $(".button-collapse").sidenav();
  $(".collapsible").collapsible();
  $(".tooltipped").tooltip();
  $("select").formSelect();
});

// Toggle form content shown or hidden
// Credit: Stack Overflow
// Bug fix: use classList.toggle instead of if/else logic
$("#read_status").on("click", showFormContent);
$("#edit_profile_btn").on("click", showFormContent);
function showFormContent(){
  document.getElementById('edit_profile_form').classList.toggle("hidden");
  
}