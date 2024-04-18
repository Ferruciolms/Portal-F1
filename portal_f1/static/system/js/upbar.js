(function() {
    if ($('#layout-sidenav').hasClass('sidenav-horizontal') || window.layoutHelpers.isSmallScreen()) {
        return;
    }
    try {
        window.layoutHelpers._getSetting("Rtl")
        window.layoutHelpers.setCollapsed(
            localStorage.getItem('layoutCollapsed') === 'true',
            false
        );
    } catch (e) {}
})();
$(function() {
    $('#layout-sidenav').each(function() {
        new SideNav(this, {
            orientation: $(this).hasClass('sidenav-horizontal') ? 'horizontal' : 'vertical'
        });
    });
    $('body').on('click', '.layout-sidenav-toggle', function(e) {
        e.preventDefault();
        window.layoutHelpers.toggleCollapsed();
        if (!window.layoutHelpers.isSmallScreen()) {
            try {
                localStorage.setItem('layoutCollapsed', String(window.layoutHelpers.isCollapsed()));
            } catch (e) {}
        }
    });
});
$(document).ready(function() {
    $("#pcoded").pcodedmenu({
        themelayout: 'horizontal',
        MenuTrigger: 'hover',
        SubMenuTrigger: 'hover',
    });
});
