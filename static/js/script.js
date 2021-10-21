/* jshint esversion: 6 */

$(document).ready(function () {
  // Init Materialize components
  $(".sidenav").sidenav;
  $(".button-collapse").sidenav();
  $(".collapsible").collapsible();
  $(".tooltipped").tooltip();
  $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
  });
});

// Remove or show more form content depending on if user has read book
// Credit: Stack Overflow
// Bug fix: use classList.toggle instead of if/else logic
$("#read_status").on("click", showFormContent);
function showFormContent(){
  document.getElementById('extra-content').classList.toggle("hidden");
}