"use strict";

var myApp = angular.module("myApp", []);

// Replace Angular notation due to Jinja having same mustache indicators
myApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});