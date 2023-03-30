// AOS
AOS.init({
  duration: 700,
  easing: "ease",
  once: true,
  disable: "mobile",
});

// Header Scroll
$(window).scroll(function () {
  if ($(this).scrollTop() > 25) {
    $(".header").addClass("sticky");
  } else {
    $(".header").removeClass("sticky");
  }
});

// Onload Modal
$(document).ready(function () {
  setTimeout(function () {
    $("#onloadModal").modal("show");
  }, 5000);
});
