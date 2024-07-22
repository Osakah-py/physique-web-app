// ---------------------------------Fonctions générales--------------------------------------------------------

function toggleFunction() {
  // $('#navDemo').toggleClass('w3-show');
  $('#navDemo').slideToggle();
}

// requêt ajax pour compléter un tableau
function remplir_tableau(categorie, table, btn) {
  $.ajax({
    type: 'GET',
    url: "./ajax/",
    data: {"categorie": categorie},
    success: function (response) {
              array = response['documents'];
              let indiceStart = parseInt(table.attr('max')) + 1; //On récupère le précédent indice max
              for (let i = 0; i < array.length; i++) {
                var indice = indiceStart + i;
                // Split de la chaîne "fichiers" pour traiter chaque fichier séparément
                var fichiers = array[i]['fichiers'].split('\n');
                // str correspondra après la boucle au html contenant toutes les colonnes de fichiers
                str="";
                for (let j = 0; j < fichiers.length; j++) {
                  str += '<td style="vertical-align:middle; horizontal-align:middle; text-align: center;"><a href="https://physique.mp2i-champo.fr/' + fichiers[j] + '"><span class="icon-pdf"></span> </a></td>';
                }
                if (array[i]['visible']) {
                  table.append('<tr class="ajax-' + categorie + '"><td>'+ indice + "</td><td>" + array[i]['title'] + "</td>" + str + "</tr>");
                } else {
                  table.append('<tr style="opacity:50%" class="ajax-' + categorie + '"><td>'+ indice + "</td><td>" + array[i]['title'] + "</td>" + str + "</tr>");
                }
                
              }
              btn.find('button').eq(0).html('Afficher moins <i class="fa fa-caret-up"></i>');
              table.append(btn);
    },
    error: function (error){
      console.log(error);
    }, 
  })
}

// ---------------------------------Gestion des événements--------------------------------------------------------
$(function() {
  
  // fonction afficher plus / afficher moins 
  $('.display-more').on('click', function () {
    var btnTr = $(this).parents('tr').eq(0);
    
    if (btnTr.attr("id") == "ajaxed") { // ON ne fait que une requête ajax par bouton
      var elt = $('.ajax-' + categorie);
      elt.toggleClass('w3-hide');
      var representant = elt.eq(0)
      
      if (representant.hasClass('w3-hide')) {
        $(this).html('Afficher plus <i class="fa fa-caret-down"></i>');
      }
      else{
        $(this).html('Afficher moins <i class="fa fa-caret-up"></i>');
        $('html, body').animate({
          scrollTop: representant.offset().top - 50
        }, 500);
      }
    }
    else {
      btnTr.attr("id","ajaxed"); // Indique qu'on aura plus besoin de faire de requête ajax pour ce bouton
      var table = btnTr.parents('tbody').eq(0); // On récoupère le tableau de la catégorie associée
      categorie = table.attr("id");
      remplir_tableau(categorie, table,btnTr);
    }
  })

    //placer les éléments d'un tableau en ordre décroissant/croissant
    $('i.sort').on('click', function() { 
        var table = $(this).parents('tbody').eq(0);
        var indices = table.find('tr:gt(0)').toArray().reverse();
        // On creer une execption pour le bouton 'afficher plus'
        var except = indices[indices.length - 1];
        // On déplace chaque élément à la fin du tableau
        for (var i = 0; i < indices.length; i++) {
          if ($(indices[i]).has('button').length) {
            except = indices[i];
          }
          table.append(indices[i]);
          }
        table.append(except);
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