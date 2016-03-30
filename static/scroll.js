function pageScroll() {
        window.scrollBy(0,50); // horizontal and vertical scroll increments
        scrolldelay = setTimeout('pageScroll()',100); // scrolls every 100 milliseconds
}