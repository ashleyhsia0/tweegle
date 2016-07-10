"use strict";

$(document).ready(function () {
    var contentHeight = $('#left-col').height();
    var sidebarHeight = $('#right-col').height();

    if (contentHeight > sidebarHeight) {
        $('#right-col').height(contentHeight);
    } else {
        $('#right-col').height(sidebarHeight);
    }
});