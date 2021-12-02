jQuery(function ($) {
	'use strict';

    

    // Service Slider JS
	$('.service-slider').owlCarousel({
        center:true,
		loop:true,
		margin: 15,
		nav: true,
		dots: false,
		smartSpeed: 1000,
		autoplay:true,
		autoplayTimeout:4000,
        autoplayHoverPause:true,
        navText: [
            "<i class='bx bx-left-arrow-alt'></i>",
            "<i class='bx bx-right-arrow-alt'></i>"
        ],
		responsive:{
			0:{
				items:1,
			},
			600:{
				items:2,
			},
			1000:{
				items:3,
			}
		}
    });
    
    

}(jQuery));