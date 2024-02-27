jQuery(document).ready(function($) {

	'use strict';

        
        $(".menu-icon").click(function() {
          $(this).toggleClass("active");
          $(".overlay-menu").toggleClass("open");
        });

});
