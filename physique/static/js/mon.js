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

});