function scaleCaptcha(elementWidth) {
    // Width of the reCAPTCHA element, in pixels
    var reCaptchaWidth = 300;
    // Get the containing element's width
      var containerWidth = $('.container').width();
    
    // Only scale the reCAPTCHA if it won't fit
    // inside the container
    if(reCaptchaWidth > containerWidth) {
      // Calculate the scale
      var captchaScale = containerWidth / reCaptchaWidth;
      // Apply the transformation
      $('.g-recaptcha').css({
        'transform':'scale('+captchaScale+')'
      });
    }
}
  
  $(function() { 
   
    // Initialize scaling
    scaleCaptcha();
    
    // Update scaling on window resize
    // Uses jQuery throttle plugin to limit strain on the browser
    $(window).resize( $.throttle( 100, scaleCaptcha ) );
    
  });