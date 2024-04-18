 $(document).ready(function () {
  $(".customer-logos").slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [
      {
        breakpoint: 1250,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  });


});


