//  Owl Carousel Function
$(function() {

	if ( $('.owl-2').length > 0 ) {
        $('.owl-2').owlCarousel({
            center: false,
            items: 1,
            loop: false,
            stagePadding: 0,
            margin: 20,
            smartSpeed: 1200,
            autoplay: true,
            nav: true,
            dots: true,
            pauseOnHover: false,
            responsive:{
                600:{
                    margin: 20,
                    nav: true,
                  items: 2
                },
                1000:{
                    margin: 20,
                    stagePadding: 0,
                    nav: true,
                  items: 3
                }
            }
        });            
    }

})

// Message Function
setTimeout(function(){
  $("#message").fadeOut('slow')
}, 4000)

