$(function() {

    //placer les éléments d'un tableau en ordre décroissant/croissant
    $('i.sort').on('click', function() { 
        var table = $(this).parents('tbody').eq(0);
        var indices = table.find('tr:gt(0)').toArray().reverse();
        // On déplace chaque élément à la fin du tableau
        for (var i = 0; i < indices.length; i++) {
            table.append(indices[i]);
          }
    });

    //Change le style de la barre de navigation quand on scroll
    $(window).on('scroll', function() {
        var navbar = $('#myNavbar');
        // en dessous de 100 px on affiche le 'fond' de la navbar
        if ($(window).scrollTop() > 100) {
          navbar.addClass("w3-card w3-animate-opacity w3-white")
        } else {
          navbar.removeClass("w3-card w3-animate-opacity w3-white")
        }
    });
});