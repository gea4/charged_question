function pageScroll() {
        window.scrollBy(0,1); // horizontal and vertical scroll increments
        scrolldelay = setTimeout('pageScroll()',80); // scrolls every 100 milliseconds
        if($(window).scrollTop() + $(window).height() >= $(document).height()) {
        	$("html, body").animate({ scrollTop: 0 }, 600);
        	location.reload();
        }
}