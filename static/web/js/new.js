$WIN = $(window);

// Add the User Agent to the <html>
// will be used for IE10 detection (Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0))
var doc = document.documentElement;
doc.setAttribute('data-useragent', navigator.userAgent);
   /* Preloader
    * -------------------------------------------------- */
function clPreloader() {        
    $("html").addClass('cl-preload');

    $WIN.on('load', function() {

        //force page scroll position to top at page refresh
        // $('html, body').animate({ scrollTop: 0 }, 'normal');

        // will first fade out the loading animation 
        $("#loader").fadeOut("slow", function() {
            // will fade out the whole DIV that covers the website.
            $("#preloader").delay(300).fadeOut("slow");
        }); 
        
        // for hero content animations 
        $("html").removeClass('cl-preload');
        $("html").addClass('cl-loaded');
    
    });
};


   /* Menu on Scrolldown
    * ------------------------------------------------------ */
function clMenuOnScrolldown() {
        
    var menuTrigger = $('.header-menu-toggle');

    $WIN.on('scroll', function() {

        if ($WIN.scrollTop() > 150) {
            menuTrigger.addClass('opaque');
        }
        else {
            menuTrigger.removeClass('opaque');
        }

    });
};


   /* OffCanvas Menu
    * ------------------------------------------------------ */
function clOffCanvas() {
    var menuTrigger     = $('.header-menu-toggle'),
        nav             = $('.header-nav'),
        closeButton     = nav.find('.header-nav__close'),
        siteBody        = $('body'),
        mainContents    = $('section, footer');

    // open-close menu by clicking on the menu icon
    menuTrigger.on('click', function(e){
        e.preventDefault();
        // menuTrigger.toggleClass('is-clicked');
        siteBody.toggleClass('menu-is-open');
    });

    // close menu by clicking the close button
    closeButton.on('click', function(e){
        e.preventDefault();
        menuTrigger.trigger('click');	
    });

    // close menu clicking outside the menu itself
    siteBody.on('click', function(e){
        if( !$(e.target).is('.header-nav, .header-nav__content, .header-menu-toggle, .header-menu-toggle span') ) {
            // menuTrigger.removeClass('is-clicked');
            siteBody.removeClass('menu-is-open');
        }
    });

};

  /* Smooth Scrolling
    * ------------------------------------------------------ */
function clSmoothScroll() {
    var scrollDuration = 800;

    $('.smoothscroll').on('click', function (e) {
        var target = this.hash,
        $target    = $(target);
        
            e.preventDefault();
            e.stopPropagation();

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, scrollDuration, 'swing').promise().done(function () {

            // check if menu is open
            if ($('body').hasClass('menu-is-open')) {
                $('.header-menu-toggle').trigger('click');
            }

            window.location.hash = target;
        });
    });

};



   /* Stat Counter
    * ------------------------------------------------------ */
function clStatCount() {
    
    var statSection = $(".about-stats"),
        stats = $(".stats__count");

    statSection.waypoint({

        handler: function(direction) {

            if (direction === "down") {

                stats.each(function () {
                    var $this = $(this);

                    $({ Counter: 0 }).animate({ Counter: $this.text() }, {
                        duration: 4000,
                        easing: 'swing',
                        step: function (curValue) {
                            $this.text(Math.ceil(curValue));
                        }
                    });
                });

            } 

            // trigger once only
            this.destroy();

        },

        offset: "90%"

    });
};


   /* Masonry
    * ---------------------------------------------------- */ 
function clMasonryFolio() {
    
    var containerBricks = $('.masonry');

    containerBricks.imagesLoaded(function () {
        containerBricks.masonry({
            itemSelector: '.masonry__brick',
            resize: true
        });
    });
};


   /* slick slider
    * ------------------------------------------------------ */
function clSlickSlider() {

    $('.clients').slick({
        arrows: false,
        dots: true,
        infinite: true,
        slidesToShow: 6,
        slidesToScroll: 2,
        //autoplay: true,
        pauseOnFocus: false,
        autoplaySpeed: 1000,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 5
                }
            },
            {
                breakpoint: 1000,
                settings: {
                    slidesToShow: 4
                }
            },
            {
                breakpoint: 800,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 500,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            }

        ]
    });

    $('.testimonials').slick({
        arrows: true,
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        adaptiveHeight: true,
        pauseOnFocus: false,
        autoplaySpeed: 1500,
        responsive: [
            {
                breakpoint: 900,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 800,
                settings: {
                    arrows: false,
                    dots: true
                }
            }
        ]
    });

};




   /* Placeholder Plugin Settings
    * ------------------------------------------------------ */
function clPlaceholder() {
    $('input, textarea, select').placeholder();  
};


/* Alert Boxes
* ------------------------------------------------------ */
var clAlertBoxes = function() {

    $('.alert-box').on('click', '.alert-box__close', function() {
        $(this).parent().fadeOut(500);
    }); 

};


   /* Contact Form
    * ------------------------------------------------------ */
function clContactForm() {
    
    /* local validation */
    $('#contactForm').validate({
    
        /* submit via ajax */
        submitHandler: function(form) {

            var sLoader = $('.submit-loader');

            $.ajax({

                type: "POST",
                url: "contacto/",
                data: $(form).serialize(),
                beforeSend: function() { 

                    sLoader.slideDown("slow");

                },
                success: function(msg) {

                    // Message was sent
                    if (msg != 'Error') {
                        sLoader.slideUp("slow"); 
                        $('.message-warning').fadeOut();
                        $('#contactForm').fadeOut();
                        $('.message-success').fadeIn();
                        document.getElementById('contactName').value = '';
                        document.getElementById('contactEmail').value = '';
                        document.getElementById('contactSubject').value = '';
                        document.getElementById('contactMessage').value = '';

                    }
                    // There was an error
                    else {
                        sLoader.slideUp("slow"); 
                        $('.message-warning').html(msg);
                        $('.message-warning').slideDown("slow");
                    }
                    $('#contactForm').fadeIn();

                },
                error: function() {

                    sLoader.slideUp("slow"); 
                    $('.message-warning').html("Something went wrong. Please try again.");
                    $('.message-warning').slideDown("slow");

                }

            });
        }

    });
};


   /* Animate On Scroll
    * ------------------------------------------------------ */
function clAOS() {
    
    AOS.init( {
        offset: 200,
        duration: 600,
        easing: 'ease-in-sine',
        delay: 300,
        once: true,
        disable: 'mobile'
    });

};


   /* Back to Top
    * ------------------------------------------------------ */
function clBackToTop() {
    
    var pxShow  = 500,         // height on which the button will show
    fadeInTime  = 400,         // how slow/fast you want the button to show
    fadeOutTime = 400,         // how slow/fast you want the button to hide
    scrollSpeed = 300,         // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'
    goTopButton = $(".go-top")
    
    // Show or hide the sticky footer button
    $(window).on('scroll', function() {
        if ($(window).scrollTop() >= pxShow) {
            goTopButton.fadeIn(fadeInTime);
        } else {
            goTopButton.fadeOut(fadeOutTime);
        }
    });
};

$(document).ready(function() {
    clPreloader();
    clMenuOnScrolldown();
    clOffCanvas();
    clStatCount();
    clMasonryFolio();
    clSlickSlider();
    clSmoothScroll();
    clPlaceholder();
    clAlertBoxes();
    clContactForm();
    clAOS();
    clBackToTop();
});