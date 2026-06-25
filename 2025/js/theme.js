/* global Pace */

(function($){
    "use strict";
    
    var $document = $(document),
        $window = $(window),
        $htmlBody = $('html, body'),
        $body = $('body'),
        $header = $('header'),
        $navbar = $('.navbar'),
        $navbarCollapse = $('.navbar-collapse'),
        $pageScrollLink = $('.page-scroll'),
        $scrollToTop = $('.scroll-to-top'),
        $galleryGrid = $('.gallery-grid'),
        navHeight = 80,
        navHeightShrink = 60;
      
    /** Detect mobile device */
    var isMobile = {
        Android: function(){
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function(){
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function(){
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function(){
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function(){
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function(){
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };
    
    
    /*
    * Window load
    */
   
    $window.on('load', function(){
        
        /** Bootstrap scrollspy */
        var ww = Math.max($window.width(), window.innerWidth),
            offset = ww > 992 ? navHeightShrink : navHeight;
            
        $body.scrollspy({    
            target: '#navigation',
            offset: offset
        });
    });
    
    
    /*
    * Document ready
    */
   
    $document.ready(function(){
        
        /*
        * Window scroll
        */

       $window.on('scroll', function(){
        if ($document.scrollTop() > navHeight){
            $scrollToTop.fadeIn();	
        }	
        else{
            $scrollToTop.fadeOut();	
        }	
    });
       
        
        
        /*
        * Window resize
        */
       
        $window.resize(function() {
            
            /** Bootstrap scrollspy */
            var dataScrollSpy = $body.data('bs.scrollspy'),
                ww = Math.max($window.width(), window.innerWidth),
                offset = ww > 992 ? navHeightShrink : navHeight;
        
            dataScrollSpy._config.offset = offset;
            $body.data('bs.scrollspy', dataScrollSpy);
            $body.scrollspy('refresh');
            
            
            /** Gallery grid */
            if ($.fn.isotope){
                $galleryGrid.isotope('layout');
            }
        });
        
        
        /** Page scroll */ 
        $pageScrollLink.on('click', function(e){
            var anchor = $(this),
                target = anchor.attr('href');
            pageScroll(target);
            e.preventDefault();
        });
        
        function pageScroll(target){
            var ww = Math.max($window.width(), window.innerWidth),
                    offset = ww > 992 ? navHeightShrink : navHeight;
            
            $htmlBody.stop().animate({
                scrollTop: $(target).offset().top - (offset - 1)
            }, 1000, 'easeInOutExpo');
            
            // Automatically retract the navigation after clicking on one of the menu items.
            $navbarCollapse.collapse('hide');
        };
        
        
        /** Counter number */
        if ($.fn.countTo){
            var $timer = $('.timer');
            $timer.one('inview', function(isInView){
                if(isInView){
                    $(this).countTo();
                }
            });
        }
        
        
        /** Pie Chart */
        if ($.fn.easyPieChart){
            var $pieChart = $('.pie-chart').find('.chart');
            $pieChart.easyPieChart({
                scaleColor: false,
                lineCap: 'butt',
                lineWidth: 10,
                size: 210,
                animate: 2000,
                easing: 'easeOutBounce',
                onStep: function(from, to, percent) {
                    $(this.el).find('.percent').text(Math.round(percent) + '%');
                }
            });
            
            $pieChart.one('inview', function(isInView){
                if(isInView){
                    $(this).data('easyPieChart').update($(this).data('percent-update'));
                }
            });
        }
        
        
        /** Carousel Custom - Init */
        if ($.fn.flickity){
            
            /** Section - About*/
            var $carouselAbout = $('#about').find('.carousel-custom');
            carouselCustom($carouselAbout);
            
            /** Section - Testimonial*/
            var $carouselTestimonial = $('#carousel-testimonial');
            carouselCustom($carouselTestimonial);
        }
        
        /** Carousel Custom */
        function carouselCustom($elem){
            var $carouselControl = $elem.closest('.carousel-custom-wrap').find('.carousel-custom-control'),
                $btnPrev = $carouselControl.find('.control-previous'),
                $btnNext = $carouselControl.find('.control-next');
                
            $elem.flickity({
                cellSelector: '.carousel-cell',
                cellAlign: 'left',
                contain: true,
                prevNextButtons: false,
                pageDots: $elem.data('pagedots'),
                draggable: $elem.data('draggable'),
                autoPlay: $elem.data('autoplay'),
                imagesLoaded: true,
                pauseAutoPlayOnHover: false
            });
            
            var flkty = $elem.data('flickity');
            $elem.find('.flickity-page-dots').on('mouseleave', function(){ 
                flkty.playPlayer(); 
            });
            
            $btnPrev.on('click', function(e){
                $elem.flickity('previous', true);
                e.preventDefault();
            });
            
            $btnNext.on('click', function(e){
                $elem.flickity('next', true);
                e.preventDefault();
            });
        }
        
        
        /** Countdown */
        if ($.fn.countdown){
            var $clock = $('#clock'),
                untilDate = $clock.data('until-date');

            $clock.countdown(untilDate, function(e){
                $(this).html(e.strftime(''
                    + '<div class="clock-item border-base-color border-bottom border-medium-thick d-inline-block mx-3 opacity-9-5 pb-3 px-3 px-sm-4 text-white"><div class="d-table h-100 w-100"><div class="d-table-cell align-middle text-center"><span class="d-block font-alt text-xs-large title-sm-medium title-extra-large-3">%D</span><span class="d-block font-alt letter-spacing-2 mt-3 text-uppercase text-sm-small title-medium">Days</span></div></div></div>'
                    + '<div class="clock-item border-base-color border-bottom border-medium-thick d-inline-block mx-3 opacity-9-5 pb-3 px-3 px-sm-4 text-white"><div class="d-table h-100 w-100"><div class="d-table-cell align-middle text-center"><span class="d-block font-alt text-xs-large title-sm-medium title-extra-large-3">%H</span><span class="d-block font-alt letter-spacing-2 mt-3 text-uppercase text-sm-small title-medium">Hr</span></div></div></div>'
                    + '<div class="clock-item border-base-color border-bottom border-medium-thick d-inline-block mt-4 mx-3 opacity-9-5 pb-3 px-3 px-sm-4 text-white"><div class="d-table h-100 w-100"><div class="d-table-cell align-middle text-center"><span class="d-block font-alt text-xs-large title-sm-medium title-extra-large-3">%M</span><span class="d-block font-alt letter-spacing-2 mt-3 text-uppercase text-sm-small title-medium">Min</span></div></div></div>'
                    + '<div class="clock-item border-base-color border-bottom border-medium-thick d-inline-block mt-4 mx-3 opacity-9-5 pb-3 px-3 px-sm-4 text-white"><div class="d-table h-100 w-100"><div class="d-table-cell align-middle text-center"><span class="d-block font-alt text-xs-large title-sm-medium title-extra-large-3">%S</span><span class="d-block font-alt letter-spacing-2 mt-3 text-uppercase text-sm-small title-medium">Sec</span></div></div></div>'));
            });
        }
        
        
        /** Gallery */
        if ($.fn.imagesLoaded && $.fn.isotope){
            $galleryGrid.imagesLoaded(function(){
                $galleryGrid.isotope({
                    itemSelector: '.item',
                    layoutMode: 'masonry'
                });
            });
        }
        
        
        /** Gallery filtering */
        if ($.fn.imagesLoaded && $.fn.isotope){
            var $gridSelectors = $('.gallery-filter').find('a');
            $gridSelectors.on('click', function(e){
                var selector = $(this).attr('data-filter');
                $galleryGrid.isotope({
                    filter: selector
                });            
                
                $gridSelectors.removeClass('disabled');
                $(this).addClass('disabled');
                
                e.preventDefault();
            });
        }
        
        
        /** Gallery - Magnific popup */
        if ($.fn.magnificPopup){
            $galleryGrid.magnificPopup({
                delegate: 'a',
                type: 'image',
                mainClass: 'mfp-fade',
                gallery:{
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0,2],
                    tPrev: 'Previous',
                    tNext: 'Next',
                    tCounter: '<span class="mfp-counter-curr">%curr%</span> of <span class="mfp-counter-total">%total%</span>'
                }
            });
            
            var $popupTrigger = $('.popup-trigger'),
                $popupTriggerClose = $('.popup-trigger-close');
        
            $popupTrigger.on('click', function(e){
                $.magnificPopup.open({
                    items: {
                        src: $(this).closest('.popup-container').find('.popup-content')
                    },
                    type: 'inline',
                    fixedContentPos: true,
                    closeOnContentClick: false,
                    callbacks: {
                        open: function () {
                            $('.mfp-wrap').addClass('popup-wrap');
                        },
                        close: function () {
                            $('.mfp-wrap').removeClass('popup-wrap');
                        }
                    }
                });
                
                e.preventDefault();
            });
            
            $popupTriggerClose.on('click', function(e){
                $.magnificPopup.close();
                e.preventDefault();
            });
        }
        
        
        /** BG Parallax */
        if (typeof ScrollMagic !== 'undefined'){
            var selector = '#home-bg-parallax';
            
            // Init controller
            var controller = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: 'onEnter', duration: '200%'}});
        
            // Build scenes
            new ScrollMagic.Scene({triggerElement: selector})
                    .setTween(selector + ' > .bg-parallax', {y: '80%', ease: Linear.easeNone})
                    .addTo(controller);
        }
        
        
        /** BG Slideshow */
        if ($.fn.flexslider){
            var $bgSlideshow = $('#home-bg-slideshow').find('.flexslider');
            $bgSlideshow.flexslider({
                selector: '.slides > .bg-cover',
                easing: 'linear',
                slideshowSpeed: 3700,
                controlNav: false,
                directionNav: false,
                keyboard: false,
                pauseOnAction: true,
                touch: false,
                after: function(slider){
                    if (!slider.playing){
                        slider.play();
                    }
                }
            });
        }
        
        
        /** BG Video - Vimeo */
        if ($.fn.vimeo_player){
            var $bgndVideo = $('#bgndVideoVimeo');
            if (!isMobile.any()){
                $bgndVideo.vimeo_player({
                    containment: 'self',
                    autoPlay: true,
                    mute: true,
                    showControls: false,
                    quality: 'medium',
                    opacity: 1,
                    loop: true,
                    startAt: 0
                });
            }
            else{
                $bgndVideo.hide();
                $bgndVideo.parent().css('background-image', 'url("' + $bgndVideo.data('video-poster') + '")');
            }
        }
        
        
        /** BG Video - YouTube */
        if ($.fn.YTPlayer){
            var $bgndVideo = $('#bgndVideoYouTube');
            if (!isMobile.any()){
                $bgndVideo.YTPlayer({
                    containment: 'self',
                    autoPlay: true,
                    mute: true,
                    showControls: false,
                    quality: 'medium',
                    opacity: 1,
                    loop: true,
                    startAt: 0
                });
            }
            else{
                $bgndVideo.hide();
                $bgndVideo.parent().css('background-image', 'url("' + $bgndVideo.data('video-poster') + '")');
            }
        }
        
            
        /** Contact form */
        var $contactForm = $('#form-contact'),
            $btnContactForm = $('#btn-form-contact');
        
        $btnContactForm.on('click', function(e){
            $contactForm.validate();
            if ($contactForm.valid()){
                send_mail($contactForm, $btnContactForm);
            }
            e.preventDefault();
        });
        
        // Send mail
        function send_mail($form, $btnForm){
            var defaultMessage = $btnForm.html(),
                sendingMessage = 'Loading...',
                errorMessage = 'Error Sending!',
                okMessage = 'Email Sent!';
            
            $btnForm.html(sendingMessage);
            
            $.ajax({
                url: $form.attr('action'),
                type: 'post',
                dataType: 'json',
                data: $form.serialize(),
                success: function(data){
                    if (data === true){
                        $btnForm.html(okMessage);
                        $form.find('input[type="text"], input[type="email"], textarea').val('');
                    }
                    else{
                        $btnForm.html(errorMessage);
                    }

                    setTimeout(function(){
                        $btnForm.html(defaultMessage);
                    }, 3000);
                },
                error: function(xhr, err){
                    $btnForm.html(errorMessage);

                    setTimeout(function(){
                        $btnForm.html(defaultMessage);
                    }, 3000);
                }
            });
        }
    });
})(jQuery);