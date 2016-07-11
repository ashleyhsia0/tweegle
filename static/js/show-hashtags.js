"use strict";

$('li#people-tab').on('click', function() {
    $('#hashtags-bar').hide();
});

$('li#tweets-tab').on('click', function() {
    $('#hashtags-bar').show();
});