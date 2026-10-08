// Keep the current section when switching between the two homepage languages.
// The theme's smooth scrolling does not update the URL itself.
document.querySelectorAll('#site-nav a[href^="#"]').forEach(function (link) {
  link.addEventListener('click', function () {
    window.history.replaceState(null, '', link.hash);
  });
});

document.querySelectorAll('.language-switch').forEach(function (link) {
  link.addEventListener('click', function () {
    link.hash = window.location.hash;
  });
});
