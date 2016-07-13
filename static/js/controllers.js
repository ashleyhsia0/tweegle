"use strict";

myApp.controller('myController', function ($scope) {
    $scope.slicedTwoUsers = [];
    while ($scope.users.length) {
        $scope.slicedTwoUsers.push($scope.users.splice(0, 2));
    }
});

